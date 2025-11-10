grammar Grammar;

program: (statement NEWLINE)* EOF;

statement: assing|print|if_statement|for_statement;

//Definimos la asignacion
assing: ID '=' expr;

//Definimos print
print:'print''('expr')';

//Definimos if_statement
if_statement: 'if''('expr')' block;

//Definimos for_statement
for_statement: 'for''('assing';'expr';'assing')' block;

//Definimos un block
block: '{'(statement NEWLINE)*'}';

//Definimos expr
expr: expr op=('*'|'/') expr
    | expr op=('+'|'-') expr
    | expr op=('>'|'<'|'>='|'<=') expr
    | expr op=('=='|'!=') expr
    | ID
    | '('expr')'
    ;

//Definimos elementos finales
ID: [-zA-Z][a-zA-Z_0-9]*;
NEWLINE: [\n];
WS: [\t]-> skip;
SEMI: ';';