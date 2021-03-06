
# Reserved words
reserved = {
  'Program': 'PROGRAM',
  'main': 'MAIN',
  'var': 'VAR',
  'int': 'INT',
  'float': 'FLOAT',
  'char': 'CHAR',
  'bool': 'BOOL',
  'function': 'FUNCTION',
  'void': 'VOID',
  'return': 'RETURN',
  'read': 'READ',
  'print': 'PRINT',
  'if': 'IF',
  'then': 'THEN',
  'else': 'ELSE',
  'while': 'WHILE',
  'do': 'DO',
  'from': 'FROM',
  'to': 'TO',
  'break': 'BREAK'
}

# Token list
tokens = [
  'ID', 'CTE_INT', 'CTE_FLOAT', 'CTE_CHAR', 'CTE_BOOL', 'STRING',
  'IS_EQUAL', 'IS_NOT_EQUAL', 'LESS_THAN_OR_EQUAL', 'MORE_THAN_OR_EQUAL'
] + list(reserved.values())

literals = "+-*/%$!?&=<>()[]{}|.,:;"

# Simple tokens
t_IS_EQUAL = r'=='
t_IS_NOT_EQUAL = r'!='
t_LESS_THAN_OR_EQUAL = r'<='
t_MORE_THAN_OR_EQUAL = r'>='
t_STRING = r'\".*\"'

# Function tokens
def t_CTE_FLOAT(t):
  r'\-?\d+\.\d+'
  t.value = float(t.value)
  return t

def t_CTE_INT(t):
  r'\-?\d+'
  t.value = int(t.value)
  return t

def t_CTE_CHAR(t):
  r'\'.\''
  t.value = t.value[1]
  return t

def t_CTE_BOOL(t):
  r'(true|false)'
  t.value = (t.value == "true")
  return t

def t_ID(t):
  r'[a-zA-Z_][a-zA-Z0-9_]*'
  t.type = reserved.get(t.value, 'ID')
  return t

# Ignored characters and tokens
t_ignore = ' \t'
t_ignore_COMMENT = r'%%.*'

# Track line number
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

# Error handling
def t_error(t):
  # raise Exception(f'({t.lineno}:{t.lexpos}) Illegal character! -> {t.value[0]}')
  print(f'({t.lineno}:{t.lexpos}) Illegal character! -> {t.value[0]}')
  t.lexer.skip(1)
