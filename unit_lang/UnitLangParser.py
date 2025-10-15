# Generated from UnitLang.g4 by ANTLR 4.13.2
import sys

from antlr4 import *

if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,
        1,
        7,
        28,
        2,
        0,
        7,
        0,
        2,
        1,
        7,
        1,
        1,
        0,
        1,
        0,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        3,
        1,
        13,
        8,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        5,
        1,
        23,
        8,
        1,
        10,
        1,
        12,
        1,
        26,
        9,
        1,
        1,
        1,
        0,
        1,
        2,
        2,
        0,
        2,
        0,
        0,
        29,
        0,
        4,
        1,
        0,
        0,
        0,
        2,
        12,
        1,
        0,
        0,
        0,
        4,
        5,
        3,
        2,
        1,
        0,
        5,
        1,
        1,
        0,
        0,
        0,
        6,
        7,
        6,
        1,
        -1,
        0,
        7,
        13,
        5,
        6,
        0,
        0,
        8,
        9,
        5,
        1,
        0,
        0,
        9,
        10,
        3,
        2,
        1,
        0,
        10,
        11,
        5,
        2,
        0,
        0,
        11,
        13,
        1,
        0,
        0,
        0,
        12,
        6,
        1,
        0,
        0,
        0,
        12,
        8,
        1,
        0,
        0,
        0,
        13,
        24,
        1,
        0,
        0,
        0,
        14,
        15,
        10,
        4,
        0,
        0,
        15,
        23,
        3,
        2,
        1,
        5,
        16,
        17,
        10,
        3,
        0,
        0,
        17,
        18,
        5,
        4,
        0,
        0,
        18,
        23,
        3,
        2,
        1,
        4,
        19,
        20,
        10,
        1,
        0,
        0,
        20,
        21,
        5,
        3,
        0,
        0,
        21,
        23,
        5,
        5,
        0,
        0,
        22,
        14,
        1,
        0,
        0,
        0,
        22,
        16,
        1,
        0,
        0,
        0,
        22,
        19,
        1,
        0,
        0,
        0,
        23,
        26,
        1,
        0,
        0,
        0,
        24,
        22,
        1,
        0,
        0,
        0,
        24,
        25,
        1,
        0,
        0,
        0,
        25,
        3,
        1,
        0,
        0,
        0,
        26,
        24,
        1,
        0,
        0,
        0,
        3,
        12,
        22,
        24,
    ]


class UnitLangParser(Parser):
    grammarFileName = "UnitLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "'('", "')'", "'^'"]

    symbolicNames = [
        "<INVALID>",
        "LEFT_BR",
        "RIGHT_BR",
        "POWER_OP",
        "PER_OP",
        "NUMBER",
        "UNIT",
        "WS",
    ]

    RULE_entrypoint = 0
    RULE_expr = 1

    ruleNames = ["entrypoint", "expr"]

    EOF = Token.EOF
    LEFT_BR = 1
    RIGHT_BR = 2
    POWER_OP = 3
    PER_OP = 4
    NUMBER = 5
    UNIT = 6
    WS = 7

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(
            self, self.atn, self.decisionsToDFA, self.sharedContextCache
        )
        self._predicates = None

    class EntrypointContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(UnitLangParser.ExprContext, 0)

        def getRuleIndex(self):
            return UnitLangParser.RULE_entrypoint

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterEntrypoint"):
                listener.enterEntrypoint(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitEntrypoint"):
                listener.exitEntrypoint(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitEntrypoint"):
                return visitor.visitEntrypoint(self)
            return visitor.visitChildren(self)

    def entrypoint(self):
        localctx = UnitLangParser.EntrypointContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_entrypoint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return UnitLangParser.RULE_expr

        def copyFrom(self, ctx: ParserRuleContext):
            super().copyFrom(ctx)

    class Unit_exprContext(ExprContext):
        def __init__(self, parser, ctx: ParserRuleContext):  # actually a UnitLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def UNIT(self):
            return self.getToken(UnitLangParser.UNIT, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterUnit_expr"):
                listener.enterUnit_expr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitUnit_expr"):
                listener.exitUnit_expr(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitUnit_expr"):
                return visitor.visitUnit_expr(self)
            return visitor.visitChildren(self)

    class Per_exprContext(ExprContext):
        def __init__(self, parser, ctx: ParserRuleContext):  # actually a UnitLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(UnitLangParser.ExprContext)
            return self.getTypedRuleContext(UnitLangParser.ExprContext, i)

        def PER_OP(self):
            return self.getToken(UnitLangParser.PER_OP, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterPer_expr"):
                listener.enterPer_expr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitPer_expr"):
                listener.exitPer_expr(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitPer_expr"):
                return visitor.visitPer_expr(self)
            return visitor.visitChildren(self)

    class Power_exprContext(ExprContext):
        def __init__(self, parser, ctx: ParserRuleContext):  # actually a UnitLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(UnitLangParser.ExprContext, 0)

        def POWER_OP(self):
            return self.getToken(UnitLangParser.POWER_OP, 0)

        def NUMBER(self):
            return self.getToken(UnitLangParser.NUMBER, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterPower_expr"):
                listener.enterPower_expr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitPower_expr"):
                listener.exitPower_expr(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitPower_expr"):
                return visitor.visitPower_expr(self)
            return visitor.visitChildren(self)

    class Group_exprContext(ExprContext):
        def __init__(self, parser, ctx: ParserRuleContext):  # actually a UnitLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LEFT_BR(self):
            return self.getToken(UnitLangParser.LEFT_BR, 0)

        def expr(self):
            return self.getTypedRuleContext(UnitLangParser.ExprContext, 0)

        def RIGHT_BR(self):
            return self.getToken(UnitLangParser.RIGHT_BR, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterGroup_expr"):
                listener.enterGroup_expr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitGroup_expr"):
                listener.exitGroup_expr(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitGroup_expr"):
                return visitor.visitGroup_expr(self)
            return visitor.visitChildren(self)

    class Multi_exprContext(ExprContext):
        def __init__(self, parser, ctx: ParserRuleContext):  # actually a UnitLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(UnitLangParser.ExprContext)
            return self.getTypedRuleContext(UnitLangParser.ExprContext, i)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterMulti_expr"):
                listener.enterMulti_expr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitMulti_expr"):
                listener.exitMulti_expr(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitMulti_expr"):
                return visitor.visitMulti_expr(self)
            return visitor.visitChildren(self)

    def expr(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = UnitLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                localctx = UnitLangParser.Unit_exprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 7
                self.match(UnitLangParser.UNIT)
            elif token in [1]:
                localctx = UnitLangParser.Group_exprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 8
                self.match(UnitLangParser.LEFT_BR)
                self.state = 9
                self.expr(0)
                self.state = 10
                self.match(UnitLangParser.RIGHT_BR)
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 24
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 2, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 22
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input, 1, self._ctx)
                    if la_ == 1:
                        localctx = UnitLangParser.Multi_exprContext(
                            self, UnitLangParser.ExprContext(self, _parentctx, _parentState)
                        )
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 14
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException

                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 15
                        self.expr(5)

                    elif la_ == 2:
                        localctx = UnitLangParser.Per_exprContext(
                            self, UnitLangParser.ExprContext(self, _parentctx, _parentState)
                        )
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 16
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException

                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 17
                        self.match(UnitLangParser.PER_OP)
                        self.state = 18
                        self.expr(4)

                    elif la_ == 3:
                        localctx = UnitLangParser.Power_exprContext(
                            self, UnitLangParser.ExprContext(self, _parentctx, _parentState)
                        )
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 19
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException

                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 20
                        self.match(UnitLangParser.POWER_OP)
                        self.state = 21
                        self.match(UnitLangParser.NUMBER)

                self.state = 26
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 2, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    def sempred(self, localctx: RuleContext, ruleIndex: int, predIndex: int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        return pred(localctx, predIndex)

    def expr_sempred(self, localctx: ExprContext, predIndex: int):
        if predIndex == 0:
            return self.precpred(self._ctx, 4)

        if predIndex == 1:
            return self.precpred(self._ctx, 3)

        if predIndex == 2:
            return self.precpred(self._ctx, 1)
