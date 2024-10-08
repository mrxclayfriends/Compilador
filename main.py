import sys
from antlr4 import FileStream, CommonTokenStream
from antlr4.tree.Tree import TerminalNodeImpl
from CompiladorPedroLexer import CompiladorPedroLexer
from CompiladorPedroParser import CompiladorPedroParser

class Node:
    def __init__(self, key, var_type=None):
        self.key = key
        self.var_type = var_type  # Armazena o tipo da variável
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, key, var_type=None):
        if not root:
            return Node(key, var_type)
        elif key < root.key:
            root.left = self.insert(root.left, key, var_type)
        else:
            root.right = self.insert(root.right, key, var_type)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def rotate_right(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

class SemanticAnalyzer:
    def __init__(self):
        self.symbol_tree = None  # Árvore AVL para armazenar variáveis
        self.errors = []  # Lista para armazenar erros
        self.unique_declarations = []  # Lista para armazenar declarações únicas

    def visit_programa(self, ctx):
        if ctx.declaracoes():
            self.visit_declaracoes(ctx.declaracoes())
        if ctx.comandos():
            self.visit_comandos(ctx.comandos())

    def visit_declaracoes(self, ctx):
        for decl in ctx.declaracao():
            self.visit_declaracao(decl)

    def visit_declaracao(self, ctx):
        var_type = ctx.getChild(0).getText()  # Tipo da variável
        declared_vars = []

        for i in range(1, ctx.getChildCount() - 1, 2):
            var_name = ctx.getChild(i).getText()
            if self.symbol_tree and self.search_avl(self.symbol_tree, var_name):
                self.errors.append(f"Erro: Variável '{var_name}' já declarada como tipo '{var_type}'.")
            else:
                declared_vars.append(var_name)
                self.symbol_tree = self.insert_to_avl(self.symbol_tree, var_name, var_type)

        # Adiciona as variáveis à lista de declarações únicas
        self.unique_declarations.extend(declared_vars)

    def insert_to_avl(self, root, key, var_type):
        avl_tree = AVLTree()
        return avl_tree.insert(root, key, var_type)

    def search_avl(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search_avl(root.left, key)
        return self.search_avl(root.right, key)

    def visit_comandos(self, ctx):
        for comando in ctx.comando():
            self.visit_comando(comando)

    def visit_comando(self, ctx):
        if isinstance(ctx, CompiladorPedroParser.ComandoAtribuicaoContext):
            self.visit_atribuicao(ctx)
        elif isinstance(ctx, CompiladorPedroParser.ComandoEntradaContext):
            self.visit_entrada(ctx)
        elif isinstance(ctx, CompiladorPedroParser.ComandoSaidaContext):
            self.visit_saida(ctx)
        elif isinstance(ctx, CompiladorPedroParser.ComandoCondicionalContext):
            self.visit_condicional(ctx)
        elif isinstance(ctx, CompiladorPedroParser.ComandoRepeticaoContext):
            self.visit_repeticao(ctx)
        else:
            error_message = f"Erro: Comando não reconhecido ou inválido: '{ctx.getText()}'."
            self.errors.append(error_message)

    def visit_atribuicao(self, ctx):
        var_name = ctx.getChild(0).getText()  # ID da variável
        if not self.search_avl(self.symbol_tree, var_name):
            self.errors.append(f"Erro: Variável '{var_name}' usada antes de ser declarada.")
            return

        expr_type = self.visit_expressao_aritmetica(ctx.expressao_aritmetica())
        var_type = self.get_var_type(var_name)  # Método para obter o tipo da variável
        if expr_type == "indefinido":
            self.errors.append(f"Erro: A expressão para a variável '{var_name}' é indefinida.")
        elif expr_type != var_type:
            self.errors.append(f"Erro: Tipo incompatível na atribuição para '{var_name}'. Esperado: '{var_type}', recebido: '{expr_type}'.")

    def get_var_type(self, var_name):
        node = self.search_avl(self.symbol_tree, var_name)
        return node.var_type if node else None

    def visit_expressao_aritmetica(self, ctx):
        if ctx.getChildCount() == 1:
            if ctx.NUM():
                return "float" if '.' in ctx.NUM().getText() else "int"
            elif ctx.ID():
                var_name = ctx.ID().getText()
                if not self.search_avl(self.symbol_tree, var_name):
                    self.errors.append(f"Erro: Variável '{var_name}' usada antes de ser declarada.")
                    return "indefinido"
                return self.get_var_type(var_name)

        left_type = self.visit_expressao_aritmetica(ctx.getChild(0))
        right_type = self.visit_expressao_aritmetica(ctx.getChild(2)) if ctx.getChildCount() > 2 else None
        
        if left_type == "float" or right_type == "float":
            return "float"
        if left_type == "int" and right_type == "int":
            return "int"
        return "indefinido"

    def visit_entrada(self, ctx):
        var_name = ctx.ID().getText()
        if not self.search_avl(self.symbol_tree, var_name):
            self.errors.append(f"Erro: Variável '{var_name}' não foi declarada antes da entrada.")
        else:
            print(f"Entrada recebida para a variável '{var_name}'.")

    def visit_saida(self, ctx):
        if ctx.getChildCount() == 5:  # Verifica se o formato do comando é correto
            expr = ctx.getChild(2)  # Expressão aritmética
            expr_type = self.visit_expressao_aritmetica(expr)
            
            if expr_type == "indefinido":
                self.errors.append("Erro: Expressão inválida na saída.")
            else:
                print(f"Saída: {expr.getText()} = {expr_type}")
        else:
            self.errors.append("Erro: Comando de saída mal formado.")

    def visit_condicional(self, ctx):
        condition_type = self.visit_expressao_logica(ctx.expressao_logica())
        if condition_type != "bool":
            self.errors.append(f"Erro: Condição deve ser do tipo booleano, mas recebeu '{condition_type}'.")

        self.visit_comandos(ctx.comandos())

    def visit_repeticao(self, ctx):
        condition_type = self.visit_expressao_logica(ctx.expressao_logica())
        if condition_type != "bool":
            self.errors.append(f"Erro: Condição deve ser do tipo booleano, mas recebeu '{condition_type}'.")

        self.visit_comandos(ctx.comandos())

    def visit_expressao_logica(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit_expressao_aritmetica(ctx.getChild(0))

        left_type = self.visit_expressao_aritmetica(ctx.getChild(0))
        right_type = self.visit_expressao_aritmetica(ctx.getChild(2)) if ctx.getChildCount() > 2 else None
        
        if left_type == "bool" and right_type == "bool":
            return "bool"
        return "indefinido"

class ASTPrinter:
    def print_ast(self, ctx, level=0):
        if ctx is None:
            return

        indent = "  " * level
        if isinstance(ctx, TerminalNodeImpl):
            print(f"{indent}{ctx.getText()}")
        else:
            print(f"{indent}{ctx.__class__.__name__}: {ctx.getText() if ctx.getText() else ''}")
            for child in ctx.children:
                if isinstance(child, TerminalNodeImpl):
                    print(f"{indent}  {child.getText()}")
                else:
                    self.print_ast(child, level + 1)

# =======================
# Função para ler e exibir os tokens
# =======================
def print_tokens(lexer):
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    print("Tokens extraídos:")
    for token in token_stream.tokens:
        if token.type >= 0 and token.type < len(lexer.symbolicNames):
            token_nome = lexer.symbolicNames[token.type]
            print(f"Token número: {token.type:<2} Texto: '{token.text}'")
        else:
            print(f"Token : {token.type} Texto: '{token.text}'")
    return token_stream

# =======================
# Função principal
# =======================
def main():
    input_file = "exemplo.txt"  # Substitua pelo seu arquivo
    try:
        input_stream = FileStream(input_file, encoding='utf-8')
    except IOError:
        print(f"Erro ao abrir o arquivo {input_file}")
        return

    lexer = CompiladorPedroLexer(input_stream)
    token_stream = print_tokens(lexer)
    parser = CompiladorPedroParser(token_stream)
    tree = parser.programa()

    analyzer = SemanticAnalyzer()
    analyzer.visit_programa(tree)

    # Impressão da árvore sintática
    printer = ASTPrinter()
    printer.print_ast(tree)

    # Mostrar erros se houver
    if analyzer.errors:
        print("\nErros encontrados:")
        for error in analyzer.errors:
            print(error)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    # Mantém o terminal aberto
    input("Pressione Enter para sair...")
