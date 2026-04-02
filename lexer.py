import ply.lex as lex
import sys

# List of token names.
# This is always required
tokens = (
    'IF',
    'THEN',
    'ELSE',
    'ID',
    'NUMBER',
    'RELOP',
)

# Reserved words
reserved = {
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
}

# RELOP map for attributes
relop_map = {
    '<': 'LT',
    '<=': 'LE',
    '=': 'EQ',
    '<>': 'NE',
    '>': 'GT',
    '>=': 'GE',
}

# Symbol table simulation
symbol_table = {}
next_pointer = 1

def get_symbol_pointer(lexem):
    global next_pointer
    if lexem not in symbol_table:
        symbol_table[lexem] = next_pointer
        next_pointer += 1
    return symbol_table[lexem]

# ID token rule
def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'ID')    # Check for reserved words
    return t

# NUMBER token rule
def t_NUMBER(t):
    r'\d+(\.\d+)?([eE][+-]?\d+)?'
    return t

# RELOP token rule
def t_RELOP(t):
    r'<=|>=|<>|<|>|='
    t.value = relop_map.get(t.value)
    return t

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t\r\n'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

def run_lexer(data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        
        token_name = tok.type.lower()
        attribute_value = '-'
        
        if tok.type == 'ID':
            token_name = 'id'
            attribute_value = f"pointer to table entry {get_symbol_pointer(tok.value)}"
        elif tok.type == 'NUMBER':
            token_name = 'number'
            attribute_value = f"pointer to table entry {get_symbol_pointer(tok.value)}"
        elif tok.type == 'RELOP':
            token_name = 'relop'
            attribute_value = tok.value
        elif tok.type in ['IF', 'THEN', 'ELSE']:
            attribute_value = '-'
            
        print(f"<{token_name}, {attribute_value}>")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            data = f.read()
    else:
        data = "if x <= 10.0 then x = 100"
    
    run_lexer(data)
