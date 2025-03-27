grammar MiGramatica;

// Reglas de inicio
programa: sentencia* EOF;

// Sentencias
sentencia
    : asignacion
    | forLoop
    ;

// Asignaciones (Ej: x = 5;)
asignacion: ID '=' expresion ';' ;

// Bucle for (Ej: for (i = 0; i < 3; i = i + 1) { x = x + 2; })
forLoop: 'for' '(' inicializacion ';' condicion ';' actualizacion ')' '{' sentencia* '}' ;

// Inicialización, condición y actualización del for
inicializacion: ID '=' expresion ;
condicion: expresion op=('<' | '>' | '==' | '!=') expresion ;
actualizacion: ID '=' expresion ;

// Expresiones matemáticas
expresion
    : expresion op=('+' | '-') expresion  # AddSub
    | expresion op=('*' | '/') expresion  # MulDiv
    | INT                                  # Int
    | ID                                   # Variable
    | '(' expresion ')'                    # Parens
    ;

// Tokens
ID  : [a-zA-Z_][a-zA-Z_0-9]* ;
INT : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;
