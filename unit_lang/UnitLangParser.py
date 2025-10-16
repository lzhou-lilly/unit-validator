# Generated from UnitLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,6,24,2,0,7,0,2,1,7,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,5,1,19,8,1,10,1,12,1,22,9,1,1,1,0,1,2,2,0,2,0,0,
        24,0,4,1,0,0,0,2,6,1,0,0,0,4,5,3,2,1,0,5,1,1,0,0,0,6,7,6,1,-1,0,
        7,8,5,5,0,0,8,20,1,0,0,0,9,10,10,3,0,0,10,11,5,2,0,0,11,19,3,2,1,
        4,12,13,10,2,0,0,13,14,5,3,0,0,14,19,3,2,1,3,15,16,10,1,0,0,16,17,
        5,1,0,0,17,19,5,4,0,0,18,9,1,0,0,0,18,12,1,0,0,0,18,15,1,0,0,0,19,
        22,1,0,0,0,20,18,1,0,0,0,20,21,1,0,0,0,21,3,1,0,0,0,22,20,1,0,0,
        0,2,18,20
    ]

class UnitLangParser ( Parser ):

    grammarFileName = "UnitLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'^'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "POW_OP", "MUL_OP", "PER_OP", "NUMBER", 
                      "UNIT", "WS" ]

    RULE_entrypoint = 0
    RULE_expr = 1

    ruleNames =  [ "entrypoint", "expr" ]

    EOF = Token.EOF
    POW_OP=1
    MUL_OP=2
    PER_OP=3
    NUMBER=4
    UNIT=5
    WS=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class EntrypointContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(UnitLangParser.ExprContext,0)


        def getRuleIndex(self):
            return UnitLangParser.RULE_entrypoint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntrypoint" ):
                listener.enterEntrypoint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntrypoint" ):
                listener.exitEntrypoint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntrypoint" ):
                return visitor.visitEntrypoint(self)
            else:
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return UnitLangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Unit_exprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a UnitLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def UNIT(self):
            return self.getToken(UnitLangParser.UNIT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnit_expr" ):
                listener.enterUnit_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnit_expr" ):
                listener.exitUnit_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnit_expr" ):
                return visitor.visitUnit_expr(self)
            else:
                return visitor.visitChildren(self)


    class Per_exprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a UnitLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(UnitLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(UnitLangParser.ExprContext,i)

        def PER_OP(self):
            return self.getToken(UnitLangParser.PER_OP, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPer_expr" ):
                listener.enterPer_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPer_expr" ):
                listener.exitPer_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPer_expr" ):
                return visitor.visitPer_expr(self)
            else:
                return visitor.visitChildren(self)


    class Pow_exprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a UnitLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(UnitLangParser.ExprContext,0)

        def POW_OP(self):
            return self.getToken(UnitLangParser.POW_OP, 0)
        def NUMBER(self):
            return self.getToken(UnitLangParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPow_expr" ):
                listener.enterPow_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPow_expr" ):
                listener.exitPow_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPow_expr" ):
                return visitor.visitPow_expr(self)
            else:
                return visitor.visitChildren(self)


    class Mul_exprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a UnitLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(UnitLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(UnitLangParser.ExprContext,i)

        def MUL_OP(self):
            return self.getToken(UnitLangParser.MUL_OP, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMul_expr" ):
                listener.enterMul_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMul_expr" ):
                listener.exitMul_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul_expr" ):
                return visitor.visitMul_expr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = UnitLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = UnitLangParser.Unit_exprContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 7
            self.match(UnitLangParser.UNIT)
            self._ctx.stop = self._input.LT(-1)
            self.state = 20
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 18
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        localctx = UnitLangParser.Mul_exprContext(self, UnitLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 9
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 10
                        self.match(UnitLangParser.MUL_OP)
                        self.state = 11
                        self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = UnitLangParser.Per_exprContext(self, UnitLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 12
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 13
                        self.match(UnitLangParser.PER_OP)
                        self.state = 14
                        self.expr(3)
                        pass

                    elif la_ == 3:
                        localctx = UnitLangParser.Pow_exprContext(self, UnitLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 15
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 16
                        self.match(UnitLangParser.POW_OP)
                        self.state = 17
                        self.match(UnitLangParser.NUMBER)
                        pass

             
                self.state = 22
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         




