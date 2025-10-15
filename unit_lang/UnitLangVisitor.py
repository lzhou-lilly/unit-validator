# Generated from UnitLang.g4 by ANTLR 4.13.2
from antlr4 import *

if "." in __name__:
    from .UnitLangParser import UnitLangParser
else:
    from UnitLangParser import UnitLangParser

# This class defines a complete generic visitor for a parse tree produced by UnitLangParser.


class UnitLangVisitor(ParseTreeVisitor):
    # Visit a parse tree produced by UnitLangParser#entrypoint.
    def visitEntrypoint(self, ctx: UnitLangParser.EntrypointContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by UnitLangParser#unit_expr.
    def visitUnit_expr(self, ctx: UnitLangParser.Unit_exprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by UnitLangParser#per_expr.
    def visitPer_expr(self, ctx: UnitLangParser.Per_exprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by UnitLangParser#power_expr.
    def visitPower_expr(self, ctx: UnitLangParser.Power_exprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by UnitLangParser#group_expr.
    def visitGroup_expr(self, ctx: UnitLangParser.Group_exprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by UnitLangParser#multi_expr.
    def visitMulti_expr(self, ctx: UnitLangParser.Multi_exprContext):
        return self.visitChildren(ctx)


del UnitLangParser
