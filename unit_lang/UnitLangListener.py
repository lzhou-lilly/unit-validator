# Generated from UnitLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .UnitLangParser import UnitLangParser
else:
    from UnitLangParser import UnitLangParser

# This class defines a complete listener for a parse tree produced by UnitLangParser.
class UnitLangListener(ParseTreeListener):

    # Enter a parse tree produced by UnitLangParser#entrypoint.
    def enterEntrypoint(self, ctx:UnitLangParser.EntrypointContext):
        pass

    # Exit a parse tree produced by UnitLangParser#entrypoint.
    def exitEntrypoint(self, ctx:UnitLangParser.EntrypointContext):
        pass


    # Enter a parse tree produced by UnitLangParser#unit_expr.
    def enterUnit_expr(self, ctx:UnitLangParser.Unit_exprContext):
        pass

    # Exit a parse tree produced by UnitLangParser#unit_expr.
    def exitUnit_expr(self, ctx:UnitLangParser.Unit_exprContext):
        pass


    # Enter a parse tree produced by UnitLangParser#per_expr.
    def enterPer_expr(self, ctx:UnitLangParser.Per_exprContext):
        pass

    # Exit a parse tree produced by UnitLangParser#per_expr.
    def exitPer_expr(self, ctx:UnitLangParser.Per_exprContext):
        pass


    # Enter a parse tree produced by UnitLangParser#pow_expr.
    def enterPow_expr(self, ctx:UnitLangParser.Pow_exprContext):
        pass

    # Exit a parse tree produced by UnitLangParser#pow_expr.
    def exitPow_expr(self, ctx:UnitLangParser.Pow_exprContext):
        pass


    # Enter a parse tree produced by UnitLangParser#mul_expr.
    def enterMul_expr(self, ctx:UnitLangParser.Mul_exprContext):
        pass

    # Exit a parse tree produced by UnitLangParser#mul_expr.
    def exitMul_expr(self, ctx:UnitLangParser.Mul_exprContext):
        pass



del UnitLangParser