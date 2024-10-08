# Generated from CompiladorPedro.g4 by ANTLR 4.13.2
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
        4,1,38,177,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,3,0,37,8,0,1,0,3,0,40,8,0,
        1,0,1,0,1,1,4,1,45,8,1,11,1,12,1,46,1,2,4,2,50,8,2,11,2,12,2,51,
        1,3,1,3,1,3,1,3,5,3,58,8,3,10,3,12,3,61,9,3,1,3,1,3,1,4,1,4,1,4,
        1,4,1,4,1,4,3,4,71,8,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,
        6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,96,8,8,1,8,
        1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,3,9,116,8,9,1,10,1,10,1,10,1,10,1,10,5,10,123,8,10,10,10,12,
        10,126,9,10,1,11,1,11,1,11,1,11,1,11,5,11,133,8,11,10,11,12,11,136,
        9,11,1,12,1,12,1,12,1,12,1,12,1,12,3,12,144,8,12,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,3,13,155,8,13,1,13,1,13,1,13,1,13,
        5,13,161,8,13,10,13,12,13,164,9,13,1,14,1,14,1,15,1,15,1,16,4,16,
        171,8,16,11,16,12,16,172,1,16,1,16,1,16,1,172,1,26,17,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,30,32,0,3,1,0,18,20,1,0,10,15,1,0,
        33,35,180,0,34,1,0,0,0,2,44,1,0,0,0,4,49,1,0,0,0,6,53,1,0,0,0,8,
        70,1,0,0,0,10,72,1,0,0,0,12,77,1,0,0,0,14,83,1,0,0,0,16,89,1,0,0,
        0,18,115,1,0,0,0,20,117,1,0,0,0,22,127,1,0,0,0,24,143,1,0,0,0,26,
        154,1,0,0,0,28,165,1,0,0,0,30,167,1,0,0,0,32,170,1,0,0,0,34,36,5,
        16,0,0,35,37,3,2,1,0,36,35,1,0,0,0,36,37,1,0,0,0,37,39,1,0,0,0,38,
        40,3,4,2,0,39,38,1,0,0,0,39,40,1,0,0,0,40,41,1,0,0,0,41,42,5,17,
        0,0,42,1,1,0,0,0,43,45,3,6,3,0,44,43,1,0,0,0,45,46,1,0,0,0,46,44,
        1,0,0,0,46,47,1,0,0,0,47,3,1,0,0,0,48,50,3,8,4,0,49,48,1,0,0,0,50,
        51,1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,5,1,0,0,0,53,54,7,0,0,
        0,54,59,5,36,0,0,55,56,5,1,0,0,56,58,5,36,0,0,57,55,1,0,0,0,58,61,
        1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,62,1,0,0,0,61,59,1,0,0,0,
        62,63,5,2,0,0,63,7,1,0,0,0,64,71,3,10,5,0,65,71,3,12,6,0,66,71,3,
        14,7,0,67,71,3,16,8,0,68,71,3,18,9,0,69,71,3,32,16,0,70,64,1,0,0,
        0,70,65,1,0,0,0,70,66,1,0,0,0,70,67,1,0,0,0,70,68,1,0,0,0,70,69,
        1,0,0,0,71,9,1,0,0,0,72,73,5,36,0,0,73,74,5,3,0,0,74,75,3,20,10,
        0,75,76,5,2,0,0,76,11,1,0,0,0,77,78,5,21,0,0,78,79,5,4,0,0,79,80,
        5,36,0,0,80,81,5,5,0,0,81,82,5,2,0,0,82,13,1,0,0,0,83,84,5,22,0,
        0,84,85,5,4,0,0,85,86,3,20,10,0,86,87,5,5,0,0,87,88,5,2,0,0,88,15,
        1,0,0,0,89,90,5,23,0,0,90,91,3,26,13,0,91,92,5,24,0,0,92,95,3,4,
        2,0,93,94,5,25,0,0,94,96,3,4,2,0,95,93,1,0,0,0,95,96,1,0,0,0,96,
        97,1,0,0,0,97,98,5,26,0,0,98,17,1,0,0,0,99,100,5,27,0,0,100,101,
        3,26,13,0,101,102,5,28,0,0,102,103,3,4,2,0,103,104,5,29,0,0,104,
        116,1,0,0,0,105,106,5,30,0,0,106,107,5,36,0,0,107,108,5,3,0,0,108,
        109,3,20,10,0,109,110,5,31,0,0,110,111,3,20,10,0,111,112,5,28,0,
        0,112,113,3,4,2,0,113,114,5,32,0,0,114,116,1,0,0,0,115,99,1,0,0,
        0,115,105,1,0,0,0,116,19,1,0,0,0,117,124,3,22,11,0,118,119,5,6,0,
        0,119,123,3,22,11,0,120,121,5,7,0,0,121,123,3,22,11,0,122,118,1,
        0,0,0,122,120,1,0,0,0,123,126,1,0,0,0,124,122,1,0,0,0,124,125,1,
        0,0,0,125,21,1,0,0,0,126,124,1,0,0,0,127,134,3,24,12,0,128,129,5,
        8,0,0,129,133,3,24,12,0,130,131,5,9,0,0,131,133,3,24,12,0,132,128,
        1,0,0,0,132,130,1,0,0,0,133,136,1,0,0,0,134,132,1,0,0,0,134,135,
        1,0,0,0,135,23,1,0,0,0,136,134,1,0,0,0,137,144,5,37,0,0,138,144,
        5,36,0,0,139,140,5,4,0,0,140,141,3,20,10,0,141,142,5,5,0,0,142,144,
        1,0,0,0,143,137,1,0,0,0,143,138,1,0,0,0,143,139,1,0,0,0,144,25,1,
        0,0,0,145,146,6,13,-1,0,146,147,3,20,10,0,147,148,3,28,14,0,148,
        149,3,20,10,0,149,155,1,0,0,0,150,151,5,4,0,0,151,152,3,26,13,0,
        152,153,5,5,0,0,153,155,1,0,0,0,154,145,1,0,0,0,154,150,1,0,0,0,
        155,162,1,0,0,0,156,157,10,1,0,0,157,158,3,30,15,0,158,159,3,26,
        13,2,159,161,1,0,0,0,160,156,1,0,0,0,161,164,1,0,0,0,162,160,1,0,
        0,0,162,163,1,0,0,0,163,27,1,0,0,0,164,162,1,0,0,0,165,166,7,1,0,
        0,166,29,1,0,0,0,167,168,7,2,0,0,168,31,1,0,0,0,169,171,9,0,0,0,
        170,169,1,0,0,0,171,172,1,0,0,0,172,173,1,0,0,0,172,170,1,0,0,0,
        173,174,1,0,0,0,174,175,5,2,0,0,175,33,1,0,0,0,16,36,39,46,51,59,
        70,95,115,122,124,132,134,143,154,162,172
    ]

class CompiladorPedroParser ( Parser ):

    grammarFileName = "CompiladorPedro.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "';'", "'='", "'('", "')'", "'+'", 
                     "'-'", "'*'", "'/'", "'=='", "'!='", "'<'", "'>'", 
                     "'<='", "'>='", "'begin'", "'end'", "'int'", "'float'", 
                     "'string'", "'input'", "'output'", "'if'", "'then'", 
                     "'else'", "'endif'", "'while'", "'do'", "'endwhile'", 
                     "'for'", "'to'", "'endfor'", "'and'", "'or'", "'not'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "BEGIN", "END", "INT", "FLOAT", "STRING", "INPUT", 
                      "OUTPUT", "IF", "THEN", "ELSE", "ENDIF", "WHILE", 
                      "DO", "ENDWHILE", "FOR", "TO", "ENDFOR", "AND", "OR", 
                      "NOT", "ID", "NUM", "WS" ]

    RULE_programa = 0
    RULE_declaracoes = 1
    RULE_comandos = 2
    RULE_declaracao = 3
    RULE_comando = 4
    RULE_atribuicao = 5
    RULE_entrada = 6
    RULE_saida = 7
    RULE_condicional = 8
    RULE_repeticao = 9
    RULE_expressao_aritmetica = 10
    RULE_expressao_multiplicativa = 11
    RULE_expressao_unaria = 12
    RULE_expressao_logica = 13
    RULE_operador_relacional = 14
    RULE_operador_logico = 15
    RULE_erro_comando = 16

    ruleNames =  [ "programa", "declaracoes", "comandos", "declaracao", 
                   "comando", "atribuicao", "entrada", "saida", "condicional", 
                   "repeticao", "expressao_aritmetica", "expressao_multiplicativa", 
                   "expressao_unaria", "expressao_logica", "operador_relacional", 
                   "operador_logico", "erro_comando" ]

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
    BEGIN=16
    END=17
    INT=18
    FLOAT=19
    STRING=20
    INPUT=21
    OUTPUT=22
    IF=23
    THEN=24
    ELSE=25
    ENDIF=26
    WHILE=27
    DO=28
    ENDWHILE=29
    FOR=30
    TO=31
    ENDFOR=32
    AND=33
    OR=34
    NOT=35
    ID=36
    NUM=37
    WS=38

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(CompiladorPedroParser.BEGIN, 0)

        def END(self):
            return self.getToken(CompiladorPedroParser.END, 0)

        def declaracoes(self):
            return self.getTypedRuleContext(CompiladorPedroParser.DeclaracoesContext,0)


        def comandos(self):
            return self.getTypedRuleContext(CompiladorPedroParser.ComandosContext,0)


        def getRuleIndex(self):
            return CompiladorPedroParser.RULE_programa

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

        localctx = CompiladorPedroParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(CompiladorPedroParser.BEGIN)
            self.state = 36
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 35
                self.declaracoes()


            self.state = 39
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 38
                self.comandos()


            self.state = 41
            self.match(CompiladorPedroParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracoesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorPedroParser.DeclaracaoContext)
            else:
                return self.getTypedRuleContext(CompiladorPedroParser.DeclaracaoContext,i)


        def getRuleIndex(self):
            return CompiladorPedroParser.RULE_declaracoes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracoes" ):
                listener.enterDeclaracoes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracoes" ):
                listener.exitDeclaracoes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracoes" ):
                return visitor.visitDeclaracoes(self)
            else:
                return visitor.visitChildren(self)




    def declaracoes(self):

        localctx = CompiladorPedroParser.DeclaracoesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaracoes)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 43
                    self.declaracao()

                else:
                    raise NoViableAltException(self)
                self.state = 46 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorPedroParser.ComandoContext)
            else:
                return self.getTypedRuleContext(CompiladorPedroParser.ComandoContext,i)


        def getRuleIndex(self):
            return CompiladorPedroParser.RULE_comandos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandos" ):
                listener.enterComandos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandos" ):
                listener.exitComandos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComandos" ):
                return visitor.visitComandos(self)
            else:
                return visitor.visitChildren(self)




    def comandos(self):

        localctx = CompiladorPedroParser.ComandosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_comandos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 48
                    self.comando()

                else:
                    raise NoViableAltException(self)
                self.state = 51 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CompiladorPedroParser.ID)
            else:
                return self.getToken(CompiladorPedroParser.ID, i)

        def INT(self):
            return self.getToken(CompiladorPedroParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CompiladorPedroParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(CompiladorPedroParser.STRING, 0)

        def getRuleIndex(self):
            return CompiladorPedroParser.RULE_declaracao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao" ):
                listener.enterDeclaracao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao" ):
                listener.exitDeclaracao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracao" ):
                return visitor.visitDeclaracao(self)
            else:
                return visitor.visitChildren(self)




    def declaracao(self):

        localctx = CompiladorPedroParser.DeclaracaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaracao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1835008) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 54
            self.match(CompiladorPedroParser.ID)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 55
                self.match(CompiladorPedroParser.T__0)
                self.state = 56
                self.match(CompiladorPedroParser.ID)
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 62
            self.match(CompiladorPedroParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CompiladorPedroParser.RULE_comando

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ComandoAtribuicaoContext(ComandoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CompiladorPedroParser.ComandoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atribuicao(self):
            return self.getTypedRuleContext(CompiladorPedroParser.AtribuicaoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoAtribuicao" ):
                listener.enterComandoAtribuicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoAtribuicao" ):
                listener.exitComandoAtribuicao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComandoAtribuicao" ):
                return visitor.visitComandoAtribuicao(self)
            else:
                return visitor.visitChildren(self)


    class ComandoEntradaContext(ComandoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CompiladorPedroParser.ComandoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def entrada(self):
            return self.getTypedRuleContext(CompiladorPedroParser.EntradaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoEntrada" ):
                listener.enterComandoEntrada(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoEntrada" ):
                listener.exitComandoEntrada(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComandoEntrada" ):
                return visitor.visitComandoEntrada(self)
            else:
                return visitor.visitChildren(self)


    class ComandoCondicionalContext(ComandoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CompiladorPedroParser.ComandoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def condicional(self):
            return self.getTypedRuleContext(CompiladorPedroParser.CondicionalContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoCondicional" ):
                listener.enterComandoCondicional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoCondicional" ):
                listener.exitComandoCondicional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComandoCondicional" ):
                return visitor.visitComandoCondicional(self)
            else:
                return visitor.visitChildren(self)


    class ComandoErroContext(ComandoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CompiladorPedroParser.ComandoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def erro_comando(self):
            return self.getTypedRuleContext(CompiladorPedroParser.Erro_comandoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoErro" ):
                listener.enterComandoErro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoErro" ):
                listener.exitComandoErro(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComandoErro" ):
                return visitor.visitComandoErro(self)
            else:
                return visitor.visitChildren(self)


    class ComandoSaidaContext(ComandoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CompiladorPedroParser.ComandoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def saida(self):
            return self.getTypedRuleContext(CompiladorPedroParser.SaidaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoSaida" ):
                listener.enterComandoSaida(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoSaida" ):
                listener.exitComandoSaida(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComandoSaida" ):
                return visitor.visitComandoSaida(self)
            else:
                return visitor.visitChildren(self)


    class ComandoRepeticaoContext(ComandoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CompiladorPedroParser.ComandoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def repeticao(self):
            return self.getTypedRuleContext(CompiladorPedroParser.RepeticaoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoRepeticao" ):
                listener.enterComandoRepeticao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoRepeticao" ):
                listener.exitComandoRepeticao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComandoRepeticao" ):
                return visitor.visitComandoRepeticao(self)
            else:
                return visitor.visitChildren(self)



    def comando(self):

        localctx = CompiladorPedroParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_comando)
        try:
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = CompiladorPedroParser.ComandoAtribuicaoContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.atribuicao()
                pass

            elif la_ == 2:
                localctx = CompiladorPedroParser.ComandoEntradaContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.entrada()
                pass

            elif la_ == 3:
                localctx = CompiladorPedroParser.ComandoSaidaContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 66
                self.saida()
                pass

            elif la_ == 4:
                localctx = CompiladorPedroParser.ComandoCondicionalContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 67
                self.condicional()
                pass

            elif la_ == 5:
                localctx = CompiladorPedroParser.ComandoRepeticaoContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 68
                self.repeticao()
                pass

            elif la_ == 6:
                localctx = CompiladorPedroParser.ComandoErroContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 69
                self.erro_comando()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtribuicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CompiladorPedroParser.ID, 0)

        def expressao_aritmetica(self):
            return self.getTypedRuleContext(CompiladorPedroParser.Expressao_aritmeticaContext,0)


        def getRuleIndex(self):
            return CompiladorPedroParser.RULE_atribuicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtribuicao" ):
                listener.enterAtribuicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtribuicao" ):
                listener.exitAtribuicao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtribuicao" ):
                return visitor.visitAtribuicao(self)
            else:
                return visitor.visitChildren(self)




    def atribuicao(self):

        localctx = CompiladorPedroParser.AtribuicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_atribuicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(CompiladorPedroParser.ID)
            self.state = 73
            self.match(CompiladorPedroParser.T__2)
            self.state = 74
            self.expressao_aritmetica()
            self.state = 75
            self.match(CompiladorPedroParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntradaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INPUT(self):
            return self.getToken(CompiladorPedroParser.INPUT, 0)

        def ID(self):
            return self.getToken(CompiladorPedroParser.ID, 0)

        def getRuleIndex(self):
            return CompiladorPedroParser.RULE_entrada

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntrada" ):
                listener.enterEntrada(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntrada" ):
                listener.exitEntrada(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntrada" ):
                return visitor.visitEntrada(self)
            else:
                return visitor.visitChildren(self)




    def entrada(self):

        localctx = CompiladorPedroParser.EntradaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_entrada)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(CompiladorPedroParser.INPUT)
            self.state = 78
            self.match(CompiladorPedroParser.T__3)
            self.state = 79
            self.match(CompiladorPedroParser.ID)
            self.state = 80
            self.match(CompiladorPedroParser.T__4)
            self.state = 81
            self.match(CompiladorPedroParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SaidaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OUTPUT(self):
            return self.getToken(CompiladorPedroParser.OUTPUT, 0)

        def expressao_aritmetica(self):
            return self.getTypedRuleContext(CompiladorPedroParser.Expressao_aritmeticaContext,0)


        def getRuleIndex(self):
            return CompiladorPedroParser.RULE_saida

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSaida" ):
                listener.enterSaida(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSaida" ):
                listener.exitSaida(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSaida" ):
                return visitor.visitSaida(self)
            else:
                return visitor.visitChildren(self)




    def saida(self):

        localctx = CompiladorPedroParser.SaidaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_saida)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(CompiladorPedroParser.OUTPUT)
            self.state = 84
            self.match(CompiladorPedroParser.T__3)
            self.state = 85
            self.expressao_aritmetica()
            self.state = 86
            self.match(CompiladorPedroParser.T__4)
            self.state = 87
            self.match(CompiladorPedroParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(CompiladorPedroParser.IF, 0)

        def expressao_logica(self):
            return self.getTypedRuleContext(CompiladorPedroParser.Expressao_logicaContext,0)


        def THEN(self):
            return self.getToken(CompiladorPedroParser.THEN, 0)

        def comandos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorPedroParser.ComandosContext)
            else:
                return self.getTypedRuleContext(CompiladorPedroParser.ComandosContext,i)


        def ENDIF(self):
            return self.getToken(CompiladorPedroParser.ENDIF, 0)

        def ELSE(self):
            return self.getToken(CompiladorPedroParser.ELSE, 0)

        def getRuleIndex(self):
            return CompiladorPedroParser.RULE_condicional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicional" ):
                listener.enterCondicional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicional" ):
                listener.exitCondicional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicional" ):
                return visitor.visitCondicional(self)
            else:
                return visitor.visitChildren(self)




    def condicional(self):

        localctx = CompiladorPedroParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(CompiladorPedroParser.IF)
            self.state = 90
            self.expressao_logica(0)
            self.state = 91
            self.match(CompiladorPedroParser.THEN)
            self.state = 92
            self.comandos()
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 93
                self.match(CompiladorPedroParser.ELSE)
                self.state = 94
                self.comandos()


            self.state = 97
            self.match(CompiladorPedroParser.ENDIF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepeticaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(CompiladorPedroParser.WHILE, 0)

        def expressao_logica(self):
            return self.getTypedRuleContext(CompiladorPedroParser.Expressao_logicaContext,0)


        def DO(self):
            return self.getToken(CompiladorPedroParser.DO, 0)

        def comandos(self):
            return self.getTypedRuleContext(CompiladorPedroParser.ComandosContext,0)


        def ENDWHILE(self):
            return self.getToken(CompiladorPedroParser.ENDWHILE, 0)

        def FOR(self):
            return self.getToken(CompiladorPedroParser.FOR, 0)

        def ID(self):
            return self.getToken(CompiladorPedroParser.ID, 0)

        def expressao_aritmetica(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorPedroParser.Expressao_aritmeticaContext)
            else:
                return self.getTypedRuleContext(CompiladorPedroParser.Expressao_aritmeticaContext,i)


        def TO(self):
            return self.getToken(CompiladorPedroParser.TO, 0)

        def ENDFOR(self):
            return self.getToken(CompiladorPedroParser.ENDFOR, 0)

        def getRuleIndex(self):
            return CompiladorPedroParser.RULE_repeticao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepeticao" ):
                listener.enterRepeticao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepeticao" ):
                listener.exitRepeticao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepeticao" ):
                return visitor.visitRepeticao(self)
            else:
                return visitor.visitChildren(self)




    def repeticao(self):

        localctx = CompiladorPedroParser.RepeticaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_repeticao)
        try:
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.match(CompiladorPedroParser.WHILE)
                self.state = 100
                self.expressao_logica(0)
                self.state = 101
                self.match(CompiladorPedroParser.DO)
                self.state = 102
                self.comandos()
                self.state = 103
                self.match(CompiladorPedroParser.ENDWHILE)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.match(CompiladorPedroParser.FOR)
                self.state = 106
                self.match(CompiladorPedroParser.ID)
                self.state = 107
                self.match(CompiladorPedroParser.T__2)
                self.state = 108
                self.expressao_aritmetica()
                self.state = 109
                self.match(CompiladorPedroParser.TO)
                self.state = 110
                self.expressao_aritmetica()
                self.state = 111
                self.match(CompiladorPedroParser.DO)
                self.state = 112
                self.comandos()
                self.state = 113
                self.match(CompiladorPedroParser.ENDFOR)
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


    class Expressao_aritmeticaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao_multiplicativa(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorPedroParser.Expressao_multiplicativaContext)
            else:
                return self.getTypedRuleContext(CompiladorPedroParser.Expressao_multiplicativaContext,i)


        def getRuleIndex(self):
            return CompiladorPedroParser.RULE_expressao_aritmetica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao_aritmetica" ):
                listener.enterExpressao_aritmetica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao_aritmetica" ):
                listener.exitExpressao_aritmetica(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressao_aritmetica" ):
                return visitor.visitExpressao_aritmetica(self)
            else:
                return visitor.visitChildren(self)




    def expressao_aritmetica(self):

        localctx = CompiladorPedroParser.Expressao_aritmeticaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expressao_aritmetica)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.expressao_multiplicativa()
            self.state = 124
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 122
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [6]:
                        self.state = 118
                        self.match(CompiladorPedroParser.T__5)
                        self.state = 119
                        self.expressao_multiplicativa()
                        pass
                    elif token in [7]:
                        self.state = 120
                        self.match(CompiladorPedroParser.T__6)
                        self.state = 121
                        self.expressao_multiplicativa()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 126
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expressao_multiplicativaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao_unaria(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorPedroParser.Expressao_unariaContext)
            else:
                return self.getTypedRuleContext(CompiladorPedroParser.Expressao_unariaContext,i)


        def getRuleIndex(self):
            return CompiladorPedroParser.RULE_expressao_multiplicativa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao_multiplicativa" ):
                listener.enterExpressao_multiplicativa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao_multiplicativa" ):
                listener.exitExpressao_multiplicativa(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressao_multiplicativa" ):
                return visitor.visitExpressao_multiplicativa(self)
            else:
                return visitor.visitChildren(self)




    def expressao_multiplicativa(self):

        localctx = CompiladorPedroParser.Expressao_multiplicativaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expressao_multiplicativa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.expressao_unaria()
            self.state = 134
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 132
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [8]:
                        self.state = 128
                        self.match(CompiladorPedroParser.T__7)
                        self.state = 129
                        self.expressao_unaria()
                        pass
                    elif token in [9]:
                        self.state = 130
                        self.match(CompiladorPedroParser.T__8)
                        self.state = 131
                        self.expressao_unaria()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 136
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expressao_unariaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(CompiladorPedroParser.NUM, 0)

        def ID(self):
            return self.getToken(CompiladorPedroParser.ID, 0)

        def expressao_aritmetica(self):
            return self.getTypedRuleContext(CompiladorPedroParser.Expressao_aritmeticaContext,0)


        def getRuleIndex(self):
            return CompiladorPedroParser.RULE_expressao_unaria

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao_unaria" ):
                listener.enterExpressao_unaria(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao_unaria" ):
                listener.exitExpressao_unaria(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressao_unaria" ):
                return visitor.visitExpressao_unaria(self)
            else:
                return visitor.visitChildren(self)




    def expressao_unaria(self):

        localctx = CompiladorPedroParser.Expressao_unariaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expressao_unaria)
        try:
            self.state = 143
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.match(CompiladorPedroParser.NUM)
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.match(CompiladorPedroParser.ID)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 139
                self.match(CompiladorPedroParser.T__3)
                self.state = 140
                self.expressao_aritmetica()
                self.state = 141
                self.match(CompiladorPedroParser.T__4)
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


    class Expressao_logicaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao_aritmetica(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorPedroParser.Expressao_aritmeticaContext)
            else:
                return self.getTypedRuleContext(CompiladorPedroParser.Expressao_aritmeticaContext,i)


        def operador_relacional(self):
            return self.getTypedRuleContext(CompiladorPedroParser.Operador_relacionalContext,0)


        def expressao_logica(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorPedroParser.Expressao_logicaContext)
            else:
                return self.getTypedRuleContext(CompiladorPedroParser.Expressao_logicaContext,i)


        def operador_logico(self):
            return self.getTypedRuleContext(CompiladorPedroParser.Operador_logicoContext,0)


        def getRuleIndex(self):
            return CompiladorPedroParser.RULE_expressao_logica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao_logica" ):
                listener.enterExpressao_logica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao_logica" ):
                listener.exitExpressao_logica(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressao_logica" ):
                return visitor.visitExpressao_logica(self)
            else:
                return visitor.visitChildren(self)



    def expressao_logica(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CompiladorPedroParser.Expressao_logicaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expressao_logica, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 146
                self.expressao_aritmetica()
                self.state = 147
                self.operador_relacional()
                self.state = 148
                self.expressao_aritmetica()
                pass

            elif la_ == 2:
                self.state = 150
                self.match(CompiladorPedroParser.T__3)
                self.state = 151
                self.expressao_logica(0)
                self.state = 152
                self.match(CompiladorPedroParser.T__4)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 162
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CompiladorPedroParser.Expressao_logicaContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expressao_logica)
                    self.state = 156
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 157
                    self.operador_logico()
                    self.state = 158
                    self.expressao_logica(2) 
                self.state = 164
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Operador_relacionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CompiladorPedroParser.RULE_operador_relacional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperador_relacional" ):
                listener.enterOperador_relacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperador_relacional" ):
                listener.exitOperador_relacional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperador_relacional" ):
                return visitor.visitOperador_relacional(self)
            else:
                return visitor.visitChildren(self)




    def operador_relacional(self):

        localctx = CompiladorPedroParser.Operador_relacionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_operador_relacional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 64512) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Operador_logicoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(CompiladorPedroParser.AND, 0)

        def OR(self):
            return self.getToken(CompiladorPedroParser.OR, 0)

        def NOT(self):
            return self.getToken(CompiladorPedroParser.NOT, 0)

        def getRuleIndex(self):
            return CompiladorPedroParser.RULE_operador_logico

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperador_logico" ):
                listener.enterOperador_logico(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperador_logico" ):
                listener.exitOperador_logico(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperador_logico" ):
                return visitor.visitOperador_logico(self)
            else:
                return visitor.visitChildren(self)




    def operador_logico(self):

        localctx = CompiladorPedroParser.Operador_logicoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_operador_logico)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 60129542144) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Erro_comandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CompiladorPedroParser.RULE_erro_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterErro_comando" ):
                listener.enterErro_comando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitErro_comando" ):
                listener.exitErro_comando(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitErro_comando" ):
                return visitor.visitErro_comando(self)
            else:
                return visitor.visitChildren(self)




    def erro_comando(self):

        localctx = CompiladorPedroParser.Erro_comandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_erro_comando)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170 
            self._errHandler.sync(self)
            _alt = 1+1
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1+1:
                    self.state = 169
                    self.matchWildcard()

                else:
                    raise NoViableAltException(self)
                self.state = 172 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

            self.state = 174
            self.match(CompiladorPedroParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[13] = self.expressao_logica_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expressao_logica_sempred(self, localctx:Expressao_logicaContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




