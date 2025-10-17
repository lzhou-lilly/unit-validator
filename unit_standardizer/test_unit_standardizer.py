import re

import pytest

from .unit_standardizer import UnitStandardizer

UNIT_STANDARDIZER = UnitStandardizer(
    units={
        "time": {
            "millisecond": ["ms"],
            "second": ["s", "sec"],
            "minute": ["m", "min"],
            "hour": ["h", "hr"],
            "day": ["d"],
            "week": ["w", "wk"],
            "month": ["m", "mo", "mon"],
            "year": ["y", "yr"],
        },
        "length": {
            "angstrom": ["a"],
            "picometer": ["pm"],
            "nanometer": ["nm"],
            "micrometer": ["um"],
            "millimeter": ["mm"],
            "inch": ["in"],
            "meter": ["m"],
            "decimeter": ["dm"],
            "centimeter": ["cm"],
        },
        "mass": {
            "picogram": ["pg"],
            "nanogram": ["ng"],
            "microgram": ["ug"],
            "milligram": ["mg"],
            "gram": ["g"],
            "ounce": ["oz"],
            "pound": ["lb"],
            "kilogram": ["kg"],
        },
        "molarity": {
            "picomolar": ["pM"],
            "nanomolar": ["nM"],
            "micromolar": ["uM"],
            "millimolar": ["mM"],
            "molar": ["M"],
        },
        "volume": {
            "liter": ["L"],
            "nanoliter": ["nL"],
            "microliter": ["uL"],
            "milliliter": ["mL"],
            "picoliter": ["pL"],
            "pint(US)": ["pt"],
            "quart(US)": ["qt"],
            "gallon(US)": ["gal"],
        },
        "temperature": {
            "Celsius": ["C", "degree Celsius", "deg C", "°C"],
            "Fahrenheit": ["F", "degree Fahrenheit", "deg F", "°F"],
            "Kelvin": ["K"],
        },
        "basepair": {
            "basepair": ["bp"],
            "kilo basepair": ["kbp"],
            "mega basepair": ["mbp"],
            "giga basepair": ["gbp"],
        },
        "arbitrary unit": {
            "international unit": ["IU"],
        },
        "count": {
            "colony forming unit": ["cfu"],
            "plaque forming unit": ["pfu"],
        },
        "ratio": {
            "percent by weight": ["wt%"],
            "percent by volume": ["vol%"],
            "percent by mole": ["mole%"],
        },
        "pressure": {
            "pascal": ["Pa"],
            "bar": ["bar"],
            "millimeter mercury": ["mmHg"],
        },
    },
)


def test_unit_standardizer_raises_when_units_duplicate() -> None:
    with pytest.raises(ValueError, match=re.escape("Duplicated unit found: m")):
        UnitStandardizer(
            units={
                "length": {
                    "m": [],
                    "km": [],
                },
                "time": {
                    "s": [],
                    "m": [],  # should have used min
                    "h": [],
                },
            }
        )


@pytest.mark.parametrize(
    "unit",
    [
        "kilo basepair/second",
        "quart(US)/hour",
        "percent by weight",
    ],
)
def test_unit_standardizer(unit: str) -> None:
    validation_errors = UNIT_STANDARDIZER.check(unit)
    assert validation_errors == []


def test_unit_standardizer_returns_errors_on_aliased_units() -> None:
    validation_errors = UNIT_STANDARDIZER.check("mmHg/s")
    assert validation_errors == [
        "⚠️ Aliased unit: mmHg ['millimeter mercury']",
        "⚠️ Aliased unit: s ['second']",
    ]


def test_unit_standardizer_returns_errors_on_unknown_units() -> None:
    validation_errors = UNIT_STANDARDIZER.check("quart(BR)/s")
    assert validation_errors == [
        "❓ Unknown unit: quart(BR)",
        "⚠️ Aliased unit: s ['second']",
    ]
