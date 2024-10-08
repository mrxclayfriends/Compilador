grammar CompiladorPedro;

// Regras do programa
programa      : BEGIN declaracoes? comandos? END;
declaracoes   : (declaracao)+;
comandos      : (comando)+;

// Tipos de declaração de variáveis
declaracao
  : (INT | FLOAT | STRING) ID (',' ID)* ';';

// Comandos
comando       : atribuicao   # ComandoAtribuicao
              | entrada      # ComandoEntrada
              | saida        # ComandoSaida
              | condicional  # ComandoCondicional
              | repeticao    # ComandoRepeticao
              | erro_comando  # ComandoErro;

// Atribuição
atribuicao    : ID '=' expressao_aritmetica ';';

// Comando de entrada e saída
entrada       : INPUT '(' ID ')' ';';
saida         : OUTPUT '(' expressao_aritmetica ')' ';';

// Estruturas condicionais e de repetição
condicional   : IF expressao_logica THEN comandos (ELSE comandos)? ENDIF;
repeticao     : WHILE expressao_logica DO comandos ENDWHILE
              | FOR ID '=' expressao_aritmetica TO expressao_aritmetica DO comandos ENDFOR;

// Expressões aritméticas
expressao_aritmetica
  : expressao_multiplicativa (('+' expressao_multiplicativa) | ('-' expressao_multiplicativa))*;

// Expressões multiplicativas
expressao_multiplicativa
  : expressao_unaria (('*' expressao_unaria) | ('/' expressao_unaria))*;

// Expressões unárias
expressao_unaria
  : NUM
  | ID
  | '(' expressao_aritmetica ')';

// Expressões lógicas 
expressao_logica 
  : expressao_aritmetica operador_relacional expressao_aritmetica
  | '(' expressao_logica ')'
  | expressao_logica operador_logico expressao_logica;

// Operadores
operador_relacional : '==' | '!=' | '<' | '>' | '<=' | '>='; 
operador_logico      : AND | OR | NOT;

// Token para comandos malformados
erro_comando
  : .+? ';' ;  // Captura qualquer comando que não esteja correto até o ponto e vírgula

// Tokens
BEGIN         : 'begin';
END           : 'end';
INT           : 'int';
FLOAT         : 'float';
STRING        : 'string';
INPUT         : 'input';
OUTPUT        : 'output';
IF            : 'if';
THEN          : 'then';
ELSE          : 'else';
ENDIF         : 'endif';
WHILE         : 'while';
DO            : 'do';
ENDWHILE      : 'endwhile';
FOR           : 'for';
TO            : 'to';
ENDFOR        : 'endfor';
AND           : 'and';
OR            : 'or';
NOT           : 'not';

// Identificadores e números
ID            : [a-zA-Z_][a-zA-Z_0-9]*;
NUM           : [0-9]+ ('.' [0-9]+)?;
WS            : [ \t\n\r]+ -> skip;
