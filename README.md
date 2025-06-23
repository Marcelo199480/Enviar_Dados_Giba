#arquivo .style.yapf na raiz do projeto

[style]
based_on_style = pep8

# Limite de comprimento de linha
COLUMN_LIMIT = 88

# Indentação
INDENT_WIDTH = 4
USE_TABS = False

# Quebra de linha em coleções
SPLIT_BEFORE_EXPRESSION_AFTER_OPENING_PAREN = True
SPLIT_BEFORE_FIRST_ARGUMENT = True
SPLIT_BEFORE_NAMED_ASSIGNS = True
SPLIT_BEFORE_DICT_SET_GENERATOR = True
SPLIT_COMPLEX_COMPREHENSION = True

# Fechamento de coleções
DEDENT_CLOSING_BRACKETS = True
COALESCE_BRACKETS = False

# Vírgula ao final de coleções
ALLOW_MULTILINE_LAMBDAS = False
EACH_DICT_ENTRY_ON_SEPARATE_LINE = True

# Espaçamento
SPACES_AROUND_POWER_OPERATOR = True
SPACES_AROUND_DEFAULT_OR_NAMED_ASSIGN = True
SPACES_BEFORE_COMMENT = 2

#- **based_on_style = pep8**  
#  Usa o estilo PEP8 como base para as demais configurações.
#
#- **COLUMN_LIMIT = 88**  
#  Define o comprimento máximo de cada linha antes de quebrar (default do Black).
#
#- **INDENT_WIDTH = 4**  
#  Define a largura da indentação (4 espaços por nível).
#
#- **USE_TABS = False**  
#  Usa espaços ao invés de tabulações para indentar.
#
#- **SPLIT_BEFORE_EXPRESSION_AFTER_OPENING_PAREN = True**  
#  Quebra a linha logo após o parêntese de abertura em expressões longas.
#
#- **SPLIT_BEFORE_FIRST_ARGUMENT = True**  
#  Quebra a linha antes do primeiro argumento em chamadas de função longas.
#
#- **SPLIT_BEFORE_NAMED_ASSIGNS = True**  
#  Quebra a linha antes de argumentos nomeados em chamadas de função.
#
#- **SPLIT_BEFORE_DICT_SET_GENERATOR = True**  
#  Quebra a linha antes de um gerador de dicionário ou conjunto.
#
#- **SPLIT_COMPLEX_COMPREHENSION = True**  
#  Quebra compreensões (list/dict/set comprehensions) complexas em várias linhas.
#
#- **DEDENT_CLOSING_BRACKETS = True**  
#  Fecha colchetes, chaves ou parênteses alinhados com a linha de abertura, não com o conteúdo interno.
#
#- **COALESCE_BRACKETS = False**  
#  Não tenta juntar várias coleções aninhadas em uma única linha.
#
#- **ALLOW_MULTILINE_LAMBDAS = False**  
#  Não permite que lambdas sejam divididas em várias linhas.
#
#- **EACH_DICT_ENTRY_ON_SEPARATE_LINE = True**  
#  Cada entrada de dicionário fica em uma linha separada.
#
#- **SPACES_AROUND_POWER_OPERATOR = True**  
#  Adiciona espaços ao redor do operador de potência (`**`).
#
#- **SPACES_AROUND_DEFAULT_OR_NAMED_ASSIGN = True**  
#  Adiciona espaços ao redor de `=` em argumentos nomeados ou valores padrão.
#
#- **SPACES_BEFORE_COMMENT = 2**  
#  Garante dois espaços antes de comentários em linha.
