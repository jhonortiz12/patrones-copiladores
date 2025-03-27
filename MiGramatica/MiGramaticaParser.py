# Generated from MiGramatica.g4 by ANTLR 4.13.1
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
        4,1,18,91,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,4,0,20,8,0,11,0,12,0,21,1,0,1,0,1,1,1,1,3,
        1,28,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,42,
        8,2,10,2,12,2,45,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,
        1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,72,8,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,86,8,7,10,
        7,12,7,89,9,7,1,7,0,1,14,8,0,2,4,6,8,10,12,14,0,1,1,0,8,11,91,0,
        19,1,0,0,0,2,27,1,0,0,0,4,29,1,0,0,0,6,48,1,0,0,0,8,52,1,0,0,0,10,
        56,1,0,0,0,12,60,1,0,0,0,14,71,1,0,0,0,16,17,3,2,1,0,17,18,5,1,0,
        0,18,20,1,0,0,0,19,16,1,0,0,0,20,21,1,0,0,0,21,19,1,0,0,0,21,22,
        1,0,0,0,22,23,1,0,0,0,23,24,5,0,0,1,24,1,1,0,0,0,25,28,3,4,2,0,26,
        28,3,12,6,0,27,25,1,0,0,0,27,26,1,0,0,0,28,3,1,0,0,0,29,30,5,2,0,
        0,30,31,5,3,0,0,31,32,3,6,3,0,32,33,5,1,0,0,33,34,3,8,4,0,34,35,
        5,1,0,0,35,36,3,10,5,0,36,37,5,4,0,0,37,43,5,5,0,0,38,39,3,2,1,0,
        39,40,5,1,0,0,40,42,1,0,0,0,41,38,1,0,0,0,42,45,1,0,0,0,43,41,1,
        0,0,0,43,44,1,0,0,0,44,46,1,0,0,0,45,43,1,0,0,0,46,47,5,6,0,0,47,
        5,1,0,0,0,48,49,5,16,0,0,49,50,5,7,0,0,50,51,3,14,7,0,51,7,1,0,0,
        0,52,53,3,14,7,0,53,54,7,0,0,0,54,55,3,14,7,0,55,9,1,0,0,0,56,57,
        5,16,0,0,57,58,5,7,0,0,58,59,3,14,7,0,59,11,1,0,0,0,60,61,5,16,0,
        0,61,62,5,7,0,0,62,63,3,14,7,0,63,13,1,0,0,0,64,65,6,7,-1,0,65,66,
        5,3,0,0,66,67,3,14,7,0,67,68,5,4,0,0,68,72,1,0,0,0,69,72,5,16,0,
        0,70,72,5,17,0,0,71,64,1,0,0,0,71,69,1,0,0,0,71,70,1,0,0,0,72,87,
        1,0,0,0,73,74,10,7,0,0,74,75,5,12,0,0,75,86,3,14,7,8,76,77,10,6,
        0,0,77,78,5,13,0,0,78,86,3,14,7,7,79,80,10,5,0,0,80,81,5,14,0,0,
        81,86,3,14,7,6,82,83,10,4,0,0,83,84,5,15,0,0,84,86,3,14,7,5,85,73,
        1,0,0,0,85,76,1,0,0,0,85,79,1,0,0,0,85,82,1,0,0,0,86,89,1,0,0,0,
        87,85,1,0,0,0,87,88,1,0,0,0,88,15,1,0,0,0,89,87,1,0,0,0,6,21,27,
        43,71,85,87
    ]

class MiGramaticaParser ( Parser ):

    grammarFileName = "MiGramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'for'", "'('", "')'", "'{'", "'}'", 
                     "'='", "'>'", "'<'", "'=='", "'!='", "'*'", "'/'", 
                     "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "INT", "WS" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_forStmt = 2
    RULE_inicializacion = 3
    RULE_condicion = 4
    RULE_actualizacion = 5
    RULE_asignacion = 6
    RULE_expresion = 7

    ruleNames =  [ "programa", "sentencia", "forStmt", "inicializacion", 
                   "condicion", "actualizacion", "asignacion", "expresion" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    ID=16
    INT=17
    WS=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiGramaticaParser.EOF, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiGramaticaParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(MiGramaticaParser.SentenciaContext,i)


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = MiGramaticaParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.sentencia()
                self.state = 17
                self.match(MiGramaticaParser.T__0)
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2 or _la==16):
                    break

            self.state = 23
            self.match(MiGramaticaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forStmt(self):
            return self.getTypedRuleContext(MiGramaticaParser.ForStmtContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(MiGramaticaParser.AsignacionContext,0)


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia" ):
                return visitor.visitSentencia(self)
            else:
                return visitor.visitChildren(self)




    def sentencia(self):

        localctx = MiGramaticaParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.forStmt()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.asignacion()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_forStmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ForLoopContext(ForStmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ForStmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def inicializacion(self):
            return self.getTypedRuleContext(MiGramaticaParser.InicializacionContext,0)

        def condicion(self):
            return self.getTypedRuleContext(MiGramaticaParser.CondicionContext,0)

        def actualizacion(self):
            return self.getTypedRuleContext(MiGramaticaParser.ActualizacionContext,0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiGramaticaParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(MiGramaticaParser.SentenciaContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForLoop" ):
                listener.enterForLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForLoop" ):
                listener.exitForLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForLoop" ):
                return visitor.visitForLoop(self)
            else:
                return visitor.visitChildren(self)



    def forStmt(self):

        localctx = MiGramaticaParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            localctx = MiGramaticaParser.ForLoopContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(MiGramaticaParser.T__1)
            self.state = 30
            self.match(MiGramaticaParser.T__2)
            self.state = 31
            self.inicializacion()
            self.state = 32
            self.match(MiGramaticaParser.T__0)
            self.state = 33
            self.condicion()
            self.state = 34
            self.match(MiGramaticaParser.T__0)
            self.state = 35
            self.actualizacion()
            self.state = 36
            self.match(MiGramaticaParser.T__3)
            self.state = 37
            self.match(MiGramaticaParser.T__4)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==16:
                self.state = 38
                self.sentencia()
                self.state = 39
                self.match(MiGramaticaParser.T__0)
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 46
            self.match(MiGramaticaParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InicializacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiGramaticaParser.ID, 0)

        def expresion(self):
            return self.getTypedRuleContext(MiGramaticaParser.ExpresionContext,0)


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_inicializacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInicializacion" ):
                listener.enterInicializacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInicializacion" ):
                listener.exitInicializacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInicializacion" ):
                return visitor.visitInicializacion(self)
            else:
                return visitor.visitChildren(self)




    def inicializacion(self):

        localctx = MiGramaticaParser.InicializacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_inicializacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(MiGramaticaParser.ID)
            self.state = 49
            self.match(MiGramaticaParser.T__6)
            self.state = 50
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiGramaticaParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(MiGramaticaParser.ExpresionContext,i)


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_condicion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicion" ):
                listener.enterCondicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicion" ):
                listener.exitCondicion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicion" ):
                return visitor.visitCondicion(self)
            else:
                return visitor.visitChildren(self)




    def condicion(self):

        localctx = MiGramaticaParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_condicion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.expresion(0)
            self.state = 53
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3840) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 54
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActualizacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiGramaticaParser.ID, 0)

        def expresion(self):
            return self.getTypedRuleContext(MiGramaticaParser.ExpresionContext,0)


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_actualizacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActualizacion" ):
                listener.enterActualizacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActualizacion" ):
                listener.exitActualizacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActualizacion" ):
                return visitor.visitActualizacion(self)
            else:
                return visitor.visitChildren(self)




    def actualizacion(self):

        localctx = MiGramaticaParser.ActualizacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_actualizacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(MiGramaticaParser.ID)
            self.state = 57
            self.match(MiGramaticaParser.T__6)
            self.state = 58
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_asignacion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignContext(AsignacionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.AsignacionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiGramaticaParser.ID, 0)
        def expresion(self):
            return self.getTypedRuleContext(MiGramaticaParser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def asignacion(self):

        localctx = MiGramaticaParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_asignacion)
        try:
            localctx = MiGramaticaParser.AssignContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(MiGramaticaParser.ID)
            self.state = 61
            self.match(MiGramaticaParser.T__6)
            self.state = 62
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_expresion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class DivContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiGramaticaParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(MiGramaticaParser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiv" ):
                listener.enterDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiv" ):
                listener.exitDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDiv" ):
                return visitor.visitDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiGramaticaParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(MiGramaticaParser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)


    class SubContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiGramaticaParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(MiGramaticaParser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSub" ):
                listener.enterSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSub" ):
                listener.exitSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSub" ):
                return visitor.visitSub(self)
            else:
                return visitor.visitChildren(self)


    class VariableContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiGramaticaParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class MulContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiGramaticaParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(MiGramaticaParser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMul" ):
                listener.enterMul(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMul" ):
                listener.exitMul(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul" ):
                return visitor.visitMul(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self):
            return self.getTypedRuleContext(MiGramaticaParser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(MiGramaticaParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiGramaticaParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expresion, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                localctx = MiGramaticaParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 65
                self.match(MiGramaticaParser.T__2)
                self.state = 66
                self.expresion(0)
                self.state = 67
                self.match(MiGramaticaParser.T__3)
                pass
            elif token in [16]:
                localctx = MiGramaticaParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 69
                self.match(MiGramaticaParser.ID)
                pass
            elif token in [17]:
                localctx = MiGramaticaParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 70
                self.match(MiGramaticaParser.INT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 87
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 85
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = MiGramaticaParser.MulContext(self, MiGramaticaParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 73
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 74
                        self.match(MiGramaticaParser.T__11)
                        self.state = 75
                        self.expresion(8)
                        pass

                    elif la_ == 2:
                        localctx = MiGramaticaParser.DivContext(self, MiGramaticaParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 76
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 77
                        self.match(MiGramaticaParser.T__12)
                        self.state = 78
                        self.expresion(7)
                        pass

                    elif la_ == 3:
                        localctx = MiGramaticaParser.AddContext(self, MiGramaticaParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 79
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 80
                        self.match(MiGramaticaParser.T__13)
                        self.state = 81
                        self.expresion(6)
                        pass

                    elif la_ == 4:
                        localctx = MiGramaticaParser.SubContext(self, MiGramaticaParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 82
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 83
                        self.match(MiGramaticaParser.T__14)
                        self.state = 84
                        self.expresion(5)
                        pass

             
                self.state = 89
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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
        self._predicates[7] = self.expresion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         




