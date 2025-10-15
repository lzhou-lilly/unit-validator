grammar UnitLang;

// Parser rules, keep first character non-cap
entrypoint
    : expr
    ;

expr
    : UNIT                    #unit_expr
    | expr expr               #multi_expr
    | expr PER_OP expr        #per_expr
    | LEFT_BR expr RIGHT_BR   #group_expr
    | expr POWER_OP NUMBER    #power_expr
    ;

// Lexer rules, keep first character cap
LEFT_BR: '(';
RIGHT_BR: ')';

POWER_OP: '^';

PER_OP: '/' | 'per';

NUMBER
    : [+-]? ( [0-9]+ ('.' [0-9]*)? | '.' [0-9]+ )
    ;

UNIT
    : [a-zA-Z_][a-zA-Z_0-9]*
    ;

WS
    : [ \t\n\r]+ -> skip
    ;
