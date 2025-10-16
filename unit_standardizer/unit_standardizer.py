from functools import cached_property

from antlr4 import CommonTokenStream, InputStream
from unit_lang.UnitLangLexer import UnitLangLexer
from unit_lang.UnitLangParser import UnitLangParser


class UnitStandardizer:
    def __init__(self, units: dict[str, dict[str, list[str]]]) -> None:
        self.units = units
        self._validate_unit_uniqueness(units)  # access the property to trigger its uniqueness check

    @cached_property
    def unit_set(self) -> set[str]:
        unit_set = set()
        for base_unit_group in self.units.values():
            for base_unit in base_unit_group:
                unit_set.add(base_unit)
        return unit_set

    @cached_property
    def alias_to_canonical_unit_map(self) -> dict[str, list[str]]:
        alias_to_canonical_unit_map: dict[str, list[str]] = {}
        for base_unit_group in self.units.values():
            for base_unit, aliases in base_unit_group.items():
                for alias in aliases:
                    alias_to_canonical_unit_map[alias] = alias_to_canonical_unit_map.get(alias, [])
                    alias_to_canonical_unit_map[alias].append(base_unit)
        return alias_to_canonical_unit_map

    def check(self, unit: str) -> list[str]:
        """Parse and standardize a unit expression using ANTLR parser."""
        input_stream = InputStream(unit)
        lexer = UnitLangLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = UnitLangParser(token_stream)

        tree = parser.entrypoint()
        expr_ctx = tree.expr()

        # Process the parse tree like a recursive formula parser
        return self._check_subtree(expr_ctx)

    ##########
    # helpers
    ##########
    def _validate_unit_uniqueness(self, units: dict[str, dict[str, list[str]]]) -> None:
        # check unit uniqueness across groups
        unit_set = set()
        for base_unit_group in units.values():
            for base_unit in base_unit_group:
                if base_unit in unit_set:
                    raise ValueError(f"Duplicated unit found: {base_unit}")
                unit_set.add(base_unit)

    def _check_subtree(self, ctx: UnitLangParser.ExprContext) -> list[str]:
        """Raise when unknown unit is found; or alias is found."""
        validation_errors: list[str] = []
        # Unit
        if isinstance(ctx, UnitLangParser.Unit_exprContext):
            unit_text = ctx.UNIT().getText()
            if unit_text not in self.unit_set:
                if unit_text in self.alias_to_canonical_unit_map:
                    validation_errors.append(
                        f"Please avoid aliased unit: {unit_text},"
                        f" use canonical unit: {self.alias_to_canonical_unit_map[unit_text]}"
                    )
                else:
                    validation_errors.append(f"Unknown unit: {unit_text}")

        # Multiplication: expr * expr (when no PER_OP and multiple expr)
        elif isinstance(ctx, UnitLangParser.Mul_exprContext):  # noqa: SIM114
            validation_errors.extend(self._check_subtree(ctx.expr(0)))
            validation_errors.extend(self._check_subtree(ctx.expr(1)))

        # Division: expr PER_OP expr
        elif isinstance(ctx, UnitLangParser.Per_exprContext):
            validation_errors.extend(self._check_subtree(ctx.expr(0)))
            validation_errors.extend(self._check_subtree(ctx.expr(1)))

        # Power: expr POW_OP NUMBER (for future implementation)
        elif isinstance(ctx, UnitLangParser.Pow_exprContext):
            validation_errors.extend(self._check_subtree(ctx.expr(0)))
        else:
            raise NotImplementedError(f"Unhandled expression type: {type(ctx)}")
        return validation_errors

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
