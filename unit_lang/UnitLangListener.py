# Generated from UnitLang.g4 by ANTLR 4.13.2
from antlr4 import *

if "." in __name__:
    from .UnitLangParser import UnitLangParser
else:
    from UnitLangParser import UnitLangParser


# This class defines a complete listener for a parse tree produced by UnitLangParser.
class UnitLangListener(ParseTreeListener):
    # Enter a parse tree produced by UnitLangParser#entrypoint.
    def enterEntrypoint(self, ctx: UnitLangParser.EntrypointContext):
        pass

    # Exit a parse tree produced by UnitLangParser#entrypoint.
    def exitEntrypoint(self, ctx: UnitLangParser.EntrypointContext):
        pass

    # Enter a parse tree produced by UnitLangParser#unit_expr.
    def enterUnit_expr(self, ctx: UnitLangParser.Unit_exprContext):
        pass

    # Exit a parse tree produced by UnitLangParser#unit_expr.
    def exitUnit_expr(self, ctx: UnitLangParser.Unit_exprContext):
        pass

    # Enter a parse tree produced by UnitLangParser#per_expr.
    def enterPer_expr(self, ctx: UnitLangParser.Per_exprContext):
        pass

    # Exit a parse tree produced by UnitLangParser#per_expr.
    def exitPer_expr(self, ctx: UnitLangParser.Per_exprContext):
        pass

    # Enter a parse tree produced by UnitLangParser#power_expr.
    def enterPower_expr(self, ctx: UnitLangParser.Power_exprContext):
        pass

    # Exit a parse tree produced by UnitLangParser#power_expr.
    def exitPower_expr(self, ctx: UnitLangParser.Power_exprContext):
        pass

    # Enter a parse tree produced by UnitLangParser#group_expr.
    def enterGroup_expr(self, ctx: UnitLangParser.Group_exprContext):
        pass

    # Exit a parse tree produced by UnitLangParser#group_expr.
    def exitGroup_expr(self, ctx: UnitLangParser.Group_exprContext):
        pass

    # Enter a parse tree produced by UnitLangParser#multi_expr.
    def enterMulti_expr(self, ctx: UnitLangParser.Multi_exprContext):
        pass

    # Exit a parse tree produced by UnitLangParser#multi_expr.
    def exitMulti_expr(self, ctx: UnitLangParser.Multi_exprContext):
        pass


del UnitLangParser
