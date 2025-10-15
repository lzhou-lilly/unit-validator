# This test should lives outside of the Unit language auto generated folder

import pytest
from antlr4 import CommonTokenStream, InputStream
from unit_lang.UnitLangLexer import UnitLangLexer
from unit_lang.UnitLangParser import UnitLangParser


@pytest.mark.parametrize(
    "unit_str",
    [
        "km",
        "N m/s",
        "m^2/h",
        "$/person/visit",
        "$/(person visit)",
    ],
)
def test_unit_lang(unit_str: str) -> None:
    input_stream = InputStream(unit_str)
    lexer = UnitLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = UnitLangParser(token_stream)

    # smoke test, if it runs, it is good
    parser.entrypoint()
