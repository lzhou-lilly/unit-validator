# Generated from UnitLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .UnitLangParser import UnitLangParser
else:
    from UnitLangParser import UnitLangParser

# This class defines a complete generic visitor for a parse tree produced by UnitLangParser.

class UnitLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by UnitLangParser#entrypoint.
    def visitEntrypoint(self, ctx:UnitLangParser.EntrypointContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by UnitLangParser#unit_expr.
    def visitUnit_expr(self, ctx:UnitLangParser.Unit_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by UnitLangParser#per_expr.
    def visitPer_expr(self, ctx:UnitLangParser.Per_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by UnitLangParser#pow_expr.
    def visitPow_expr(self, ctx:UnitLangParser.Pow_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by UnitLangParser#mul_expr.
    def visitMul_expr(self, ctx:UnitLangParser.Mul_exprContext):
        return self.visitChildren(ctx)



del UnitLangParser