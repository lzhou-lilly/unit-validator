grammar UnitLang;

// Parser rules, keep first character non-cap
entrypoint
    : expr
    ;

expr
    : UNIT                    #unit_expr
    | expr MUL_OP expr        #mul_expr
    | expr PER_OP expr        #per_expr
    | expr POW_OP NUMBER      #pow_expr
    ;

// Lexer rules, keep first character cap
POW_OP: '^';

MUL_OP: '*';

PER_OP: '/';

NUMBER
    : [+-]? ( [0-9]+ ('.' [0-9]*)? | '.' [0-9]+ )
    ;

UNIT
    : [a-zA-Z_][a-zA-Z_0-9() ]*[a-zA-Z_0-9()]  // Multi-char unit with spaces
    | [a-zA-Z_]                            // Single char unit
    ;

WS
    : [ \t\n\r]+ -> skip
    ;
