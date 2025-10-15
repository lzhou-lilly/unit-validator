from functools import cached_property

from antlr4 import CommonTokenStream, InputStream
from unit_lang.UnitLangLexer import UnitLangLexer
from unit_lang.UnitLangParser import UnitLangParser


class UnitStandardizer:
    def __init__(self, units: list[dict[str, float | int]]) -> None:
        self.units = units
        self._validate_unit_uniqueness(units)

    @cached_property
    def unit_to_base_unit_map(self) -> dict[str, tuple[float | int, str]]:
        # build unit_to_base_unit_map
        unit_to_base_unit_map: dict[str, tuple[float | int, str]] = {}
        for base_unit_group in self.units:
            base_unit = None
            for unit, factor in base_unit_group.items():
                if factor == 1:
                    if base_unit is not None:
                        raise ValueError("multiple base units in a group")
                    base_unit = unit
            if base_unit is None:
                raise ValueError("no base unit in a group")
            for unit, factor in base_unit_group.items():
                unit_to_base_unit_map[unit] = (factor, base_unit)
        return unit_to_base_unit_map

    def standardize(self, unit: str) -> tuple[float | int, str]:
        """Parse and standardize a unit expression using ANTLR parser."""
        input_stream = InputStream(unit)
        lexer = UnitLangLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = UnitLangParser(token_stream)

        tree = parser.entrypoint()
        expr_ctx = tree.expr()

        # Process the parse tree like a recursive formula parser
        factor, unit_power_counter = self._process_subtree(expr_ctx)
        # Construct the standardized unit string
        return (factor, self._compose_standard_unit(unit_power_counter))

    ##########
    # helpers
    ##########
    def _validate_unit_uniqueness(self, units: list[dict[str, float | int]]) -> None:
        # check unit uniqueness across groups
        unit_set = set()
        for base_unit_group in units:
            for unit in base_unit_group:
                if unit in unit_set:
                    raise ValueError(f"Duplicated unit found: {unit}")
                unit_set.add(unit)

    def _process_subtree(  # noqa: C901
        self, ctx: UnitLangParser.ExprContext
    ) -> tuple[float | int, dict[str, int]]:
        # The return tuple is (factor, unit_power_counter)
        """Process expression context using labeled alternatives."""
        # Simple unit: UNIT
        if isinstance(ctx, UnitLangParser.Unit_exprContext):
            unit_text = ctx.UNIT().getText()
            if unit_text not in self.unit_to_base_unit_map:
                raise ValueError(f"Unknown unit: {unit_text}")
            factor, base_unit = self.unit_to_base_unit_map[unit_text]
            return (factor, {base_unit: 1})

        # Multiplication: expr expr (when no PER_OP and multiple expr)
        if isinstance(ctx, UnitLangParser.Multi_exprContext):
            left_factor, left_unit_power_counter = self._process_subtree(ctx.expr(0))
            right_factor, right_unit_power_counter = self._process_subtree(ctx.expr(1))
            combined_factor = left_factor * right_factor
            combined_unit_power_counter = left_unit_power_counter.copy()
            # power rule, add exponents for multiplication
            for unit, power in right_unit_power_counter.items():
                combined_unit_power_counter[unit] = combined_unit_power_counter.get(unit, 0) + power
            # remove zero power units
            for unit, power in list(combined_unit_power_counter.items()):
                if power == 0:
                    del combined_unit_power_counter[unit]
            return (combined_factor, combined_unit_power_counter)

        # Division: expr PER_OP expr
        if isinstance(ctx, UnitLangParser.Per_exprContext):
            left_factor, left_unit_power_counter = self._process_subtree(ctx.expr(0))
            right_factor, right_unit_power_counter = self._process_subtree(ctx.expr(1))
            combined_factor = left_factor / right_factor
            combined_unit_power_counter = left_unit_power_counter.copy()
            # power rule, subtract exponents for division
            for unit, power in right_unit_power_counter.items():
                combined_unit_power_counter[unit] = combined_unit_power_counter.get(unit, 0) - power
            # remove zero power units
            for unit, power in list(combined_unit_power_counter.items()):
                if power == 0:
                    del combined_unit_power_counter[unit]
            return (combined_factor, combined_unit_power_counter)

        # Parentheses: LEFT_BR expr RIGHT_BR
        if isinstance(ctx, UnitLangParser.Group_exprContext):
            return self._process_subtree(ctx.expr(0))

        # Power: expr POWER_OP NUMBER (for future implementation)
        if isinstance(ctx, UnitLangParser.Power_exprContext):
            base_factor, base_unit_power_counter = self._process_subtree(ctx.expr(0))
            power = int(ctx.NUMBER().getText())
            powered_factor = base_factor**power
            powered_unit_power_counter = {
                unit: exp * power for unit, exp in base_unit_power_counter.items()
            }
            return (powered_factor, powered_unit_power_counter)

        raise NotImplementedError(f"Unhandled expression type: {type(ctx)}")

    def _compose_standard_unit(self, unit_power_counter: dict[str, int]) -> str:
        numerator_parts = []
        denominator_parts = []
        for unit, power in sorted(unit_power_counter.items()):
            if power > 0 and power != 1:
                numerator_parts.append(f"{unit}^{power}")
            elif power == 1:
                numerator_parts.append(unit)
            elif power < 0 and power != -1:
                denominator_parts.append(f"{unit}^{-power}")
            elif power == -1:
                denominator_parts.append(unit)
        standardized_unit = " ".join(numerator_parts)
        if len(denominator_parts) == 1:
            standardized_unit += "/" + denominator_parts[0]
        elif len(denominator_parts) > 1:
            standardized_unit += "/(" + " ".join(denominator_parts) + ")"
        return standardized_unit
