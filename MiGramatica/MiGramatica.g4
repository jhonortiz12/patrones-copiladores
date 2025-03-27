grammar MiGramatica;

// Regla principal: múltiples sentencias
programa: (sentencia ';')+ EOF ;

// Sentencias posibles
sentencia
    : forStmt
    | asignacion
    ;

// Regla para `for`
forStmt
    : 'for' '(' inicializacion ';' condicion ';' actualizacion ')' '{' (sentencia ';')* '}' # ForLoop
    ;


// Inicialización del `for`
inicializacion
    : ID '=' expresion
    ;

// Condición dentro del `for`
condicion
    : expresion op=('>' | '<' | '==' | '!=') expresion
    ;

// Actualización del `for`
actualizacion
    : ID '=' expresion
    ;

// Asignaciones generales
asignacion
    : ID '=' expresion # Assign
    ;

// Expresiones matemáticas con precedencia adecuada
expresion
    : expresion '*' expresion            # Mul
    | expresion '/' expresion            # Div
    | expresion '+' expresion            # Add
    | expresion '-' expresion            # Sub
    | '(' expresion ')'                  # Parens
    | ID                                 # Variable
    | INT                                # Int
    ;

// Reglas léxicas
ID  : [a-zA-Z_][a-zA-Z_0-9]* ;  // Identificadores
INT : [0-9]+ ;                  // Números enteros
WS  : [ \t\r\n]+ -> skip ;      // Espacios en blanco ignorados
