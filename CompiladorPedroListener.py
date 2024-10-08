# Generated from CompiladorPedro.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CompiladorPedroParser import CompiladorPedroParser
else:
    from CompiladorPedroParser import CompiladorPedroParser

# This class defines a complete listener for a parse tree produced by CompiladorPedroParser.
class CompiladorPedroListener(ParseTreeListener):

    # Enter a parse tree produced by CompiladorPedroParser#programa.
    def enterPrograma(self, ctx:CompiladorPedroParser.ProgramaContext):
        pass

    # Exit a parse tree produced by CompiladorPedroParser#programa.
    def exitPrograma(self, ctx:CompiladorPedroParser.ProgramaContext):
        pass


    # Enter a parse tree produced by CompiladorPedroParser#declaracoes.
    def enterDeclaracoes(self, ctx:CompiladorPedroParser.DeclaracoesContext):
        pass

    # Exit a parse tree produced by CompiladorPedroParser#declaracoes.
    def exitDeclaracoes(self, ctx:CompiladorPedroParser.DeclaracoesContext):
        pass


    # Enter a parse tree produced by CompiladorPedroParser#comandos.
    def enterComandos(self, ctx:CompiladorPedroParser.ComandosContext):
        pass

    # Exit a parse tree produced by CompiladorPedroParser#comandos.
    def exitComandos(self, ctx:CompiladorPedroParser.ComandosContext):
        pass


    # Enter a parse tree produced by CompiladorPedroParser#declaracao.
    def enterDeclaracao(self, ctx:CompiladorPedroParser.DeclaracaoContext):
        pass

    # Exit a parse tree produced by CompiladorPedroParser#declaracao.
    def exitDeclaracao(self, ctx:CompiladorPedroParser.DeclaracaoContext):
        pass


    # Enter a parse tree produced by CompiladorPedroParser#ComandoAtribuicao.
    def enterComandoAtribuicao(self, ctx:CompiladorPedroParser.ComandoAtribuicaoContext):
        pass

    # Exit a parse tree produced by CompiladorPedroParser#ComandoAtribuicao.
    def exitComandoAtribuicao(self, ctx:CompiladorPedroParser.ComandoAtribuicaoContext):
        pass


    # Enter a parse tree produced by CompiladorPedroParser#ComandoEntrada.
    def enterComandoEntrada(self, ctx:CompiladorPedroParser.ComandoEntradaContext):
        pass

    # Exit a parse tree produced by CompiladorPedroParser#ComandoEntrada.
    def exitComandoEntrada(self, ctx:CompiladorPedroParser.ComandoEntradaContext):
        pass


    # Enter a parse tree produced by CompiladorPedroParser#ComandoSaida.
    def enterComandoSaida(self, ctx:CompiladorPedroParser.ComandoSaidaContext):
        pass

    # Exit a parse tree produced by CompiladorPedroParser#ComandoSaida.
    def exitComandoSaida(self, ctx:CompiladorPedroParser.ComandoSaidaContext):
        pass


    # Enter a parse tree produced by CompiladorPedroParser#ComandoCondicional.
    def enterComandoCondicional(self, ctx:CompiladorPedroParser.ComandoCondicionalContext):
        pass

    # Exit a parse tree produced by CompiladorPedroParser#ComandoCondicional.
    def exitComandoCondicional(self, ctx:CompiladorPedroParser.ComandoCondicionalContext):
        pass


    # Enter a parse tree produced by CompiladorPedroParser#ComandoRepeticao.
    def enterComandoRepeticao(self, ctx:CompiladorPedroParser.ComandoRepeticaoContext):
        pass

    # Exit a parse tree produced by CompiladorPedroParser#ComandoRepeticao.
    def exitComandoRepeticao(self, ctx:CompiladorPedroParser.ComandoRepeticaoContext):
        pass


    # Enter a parse tree produced by CompiladorPedroParser#ComandoErro.
    def enterComandoErro(self, ctx:CompiladorPedroParser.ComandoErroContext):
        pass

    # Exit a parse tree produced by CompiladorPedroParser#ComandoErro.
    def exitComandoErro(self, ctx:CompiladorPedroParser.ComandoErroContext):
        pass


    # Enter a parse tree produced by CompiladorPedroParser#atribuicao.
    def enterAtribuicao(self, ctx:CompiladorPedroParser.AtribuicaoContext):
        pass

    # Exit a parse tree produced by CompiladorPedroParser#atribuicao.
    def exitAtribuicao(self, ctx:CompiladorPedroParser.AtribuicaoContext):
        pass


    # Enter a parse tree produced by CompiladorPedroParser#entrada.
    def enterEntrada(self, ctx:CompiladorPedroParser.EntradaContext):
        pass

    # Exit a parse tree produced by CompiladorPedroParser#entrada.
    def exitEntrada(self, ctx:CompiladorPedroParser.EntradaContext):
        pass


    # Enter a parse tree produced by CompiladorPedroParser#saida.
    def enterSaida(self, ctx:CompiladorPedroParser.SaidaContext):
        pass

    # Exit a parse tree produced by CompiladorPedroParser#saida.
    def exitSaida(self, ctx:CompiladorPedroParser.SaidaContext):
        pass


    # Enter a parse tree produced by CompiladorPedroParser#condicional.
    def enterCondicional(self, ctx:CompiladorPedroParser.CondicionalContext):
        pass

    # Exit a parse tree produced by CompiladorPedroParser#condicional.
    def exitCondicional(self, ctx:CompiladorPedroParser.CondicionalContext):
        pass


    # Enter a parse tree produced by CompiladorPedroParser#repeticao.
    def enterRepeticao(self, ctx:CompiladorPedroParser.RepeticaoContext):
        pass

    # Exit a parse tree produced by CompiladorPedroParser#repeticao.
    def exitRepeticao(self, ctx:CompiladorPedroParser.RepeticaoContext):
        pass


    # Enter a parse tree produced by CompiladorPedroParser#expressao_aritmetica.
    def enterExpressao_aritmetica(self, ctx:CompiladorPedroParser.Expressao_aritmeticaContext):
        pass

    # Exit a parse tree produced by CompiladorPedroParser#expressao_aritmetica.
    def exitExpressao_aritmetica(self, ctx:CompiladorPedroParser.Expressao_aritmeticaContext):
        pass


    # Enter a parse tree produced by CompiladorPedroParser#expressao_multiplicativa.
    def enterExpressao_multiplicativa(self, ctx:CompiladorPedroParser.Expressao_multiplicativaContext):
        pass

    # Exit a parse tree produced by CompiladorPedroParser#expressao_multiplicativa.
    def exitExpressao_multiplicativa(self, ctx:CompiladorPedroParser.Expressao_multiplicativaContext):
        pass


    # Enter a parse tree produced by CompiladorPedroParser#expressao_unaria.
    def enterExpressao_unaria(self, ctx:CompiladorPedroParser.Expressao_unariaContext):
        pass

    # Exit a parse tree produced by CompiladorPedroParser#expressao_unaria.
    def exitExpressao_unaria(self, ctx:CompiladorPedroParser.Expressao_unariaContext):
        pass


    # Enter a parse tree produced by CompiladorPedroParser#expressao_logica.
    def enterExpressao_logica(self, ctx:CompiladorPedroParser.Expressao_logicaContext):
        pass

    # Exit a parse tree produced by CompiladorPedroParser#expressao_logica.
    def exitExpressao_logica(self, ctx:CompiladorPedroParser.Expressao_logicaContext):
        pass


    # Enter a parse tree produced by CompiladorPedroParser#operador_relacional.
    def enterOperador_relacional(self, ctx:CompiladorPedroParser.Operador_relacionalContext):
        pass

    # Exit a parse tree produced by CompiladorPedroParser#operador_relacional.
    def exitOperador_relacional(self, ctx:CompiladorPedroParser.Operador_relacionalContext):
        pass


    # Enter a parse tree produced by CompiladorPedroParser#operador_logico.
    def enterOperador_logico(self, ctx:CompiladorPedroParser.Operador_logicoContext):
        pass

    # Exit a parse tree produced by CompiladorPedroParser#operador_logico.
    def exitOperador_logico(self, ctx:CompiladorPedroParser.Operador_logicoContext):
        pass


    # Enter a parse tree produced by CompiladorPedroParser#erro_comando.
    def enterErro_comando(self, ctx:CompiladorPedroParser.Erro_comandoContext):
        pass

    # Exit a parse tree produced by CompiladorPedroParser#erro_comando.
    def exitErro_comando(self, ctx:CompiladorPedroParser.Erro_comandoContext):
        pass



del CompiladorPedroParser