import pytest

from .unit_standardizer import UnitStandardizer

UNIT_STANDARDIZER = UnitStandardizer(
    base_units=[
        {  # length
            "m": 1,
            "km": 1000,
        },
        {  # time
            "s": 1,
            "min": 60,
            "h": 3600,
        },
        {  # force
            "N": 1,
            "kN": 1000,
        },
    ]
)


@pytest.mark.parametrize(
    ("unit", "expected_factor", "expected_base_unit"),
    [
        ("km/s", 1000, "m/s"),
        ("m/s ", 1, "m/s"),
        ("km/h", 1000 / 3600, "m/s"),
    ],
)
def test_unit_standardizer(unit: str, expected_factor: float, expected_base_unit: str) -> None:
    assert UNIT_STANDARDIZER.standardize(unit) == (expected_factor, expected_base_unit)


def test_unit_standardizer_raises_error() -> None:
    with pytest.raises(ValueError, match="Unknown unit: Nm"):
        UNIT_STANDARDIZER.standardize("Nm/s")
