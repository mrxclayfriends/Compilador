# Generated from CompiladorPedro.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CompiladorPedroParser import CompiladorPedroParser
else:
    from CompiladorPedroParser import CompiladorPedroParser

# This class defines a complete generic visitor for a parse tree produced by CompiladorPedroParser.

class CompiladorPedroVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CompiladorPedroParser#programa.
    def visitPrograma(self, ctx:CompiladorPedroParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorPedroParser#declaracoes.
    def visitDeclaracoes(self, ctx:CompiladorPedroParser.DeclaracoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorPedroParser#comandos.
    def visitComandos(self, ctx:CompiladorPedroParser.ComandosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorPedroParser#declaracao.
    def visitDeclaracao(self, ctx:CompiladorPedroParser.DeclaracaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorPedroParser#ComandoAtribuicao.
    def visitComandoAtribuicao(self, ctx:CompiladorPedroParser.ComandoAtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorPedroParser#ComandoEntrada.
    def visitComandoEntrada(self, ctx:CompiladorPedroParser.ComandoEntradaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorPedroParser#ComandoSaida.
    def visitComandoSaida(self, ctx:CompiladorPedroParser.ComandoSaidaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorPedroParser#ComandoCondicional.
    def visitComandoCondicional(self, ctx:CompiladorPedroParser.ComandoCondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorPedroParser#ComandoRepeticao.
    def visitComandoRepeticao(self, ctx:CompiladorPedroParser.ComandoRepeticaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorPedroParser#ComandoErro.
    def visitComandoErro(self, ctx:CompiladorPedroParser.ComandoErroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorPedroParser#atribuicao.
    def visitAtribuicao(self, ctx:CompiladorPedroParser.AtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorPedroParser#entrada.
    def visitEntrada(self, ctx:CompiladorPedroParser.EntradaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorPedroParser#saida.
    def visitSaida(self, ctx:CompiladorPedroParser.SaidaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorPedroParser#condicional.
    def visitCondicional(self, ctx:CompiladorPedroParser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorPedroParser#repeticao.
    def visitRepeticao(self, ctx:CompiladorPedroParser.RepeticaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorPedroParser#expressao_aritmetica.
    def visitExpressao_aritmetica(self, ctx:CompiladorPedroParser.Expressao_aritmeticaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorPedroParser#expressao_multiplicativa.
    def visitExpressao_multiplicativa(self, ctx:CompiladorPedroParser.Expressao_multiplicativaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorPedroParser#expressao_unaria.
    def visitExpressao_unaria(self, ctx:CompiladorPedroParser.Expressao_unariaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorPedroParser#expressao_logica.
    def visitExpressao_logica(self, ctx:CompiladorPedroParser.Expressao_logicaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorPedroParser#operador_relacional.
    def visitOperador_relacional(self, ctx:CompiladorPedroParser.Operador_relacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorPedroParser#operador_logico.
    def visitOperador_logico(self, ctx:CompiladorPedroParser.Operador_logicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorPedroParser#erro_comando.
    def visitErro_comando(self, ctx:CompiladorPedroParser.Erro_comandoContext):
        return self.visitChildren(ctx)



del CompiladorPedroParser