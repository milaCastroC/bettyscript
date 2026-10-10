#Implementación BettyScript
def lexer(texto):

    tokens = []
    i = 0
    col = 1
    row = 1

    while i < len(texto):
        c = texto[i]

        if c == " ":
            i += 1
        elif c == "\n":
            col = 1
            row += 1
            i += 1
        elif c.isdigit():
            inicio = i
            while i < len(texto) and texto[i].isdigit():
                i += 1
            tokens.append(("NUMERO", texto[inicio:i], row, col))
            col += 1
        elif c.isalpha():
            inicio = i
            while i < len(texto) and texto[i].isalpha():
                i += 1
            tokens.append(("IDENTIFICADOR", texto[inicio:i], row, col))
            col+=1
        elif c == ";":
            tokens.append(("SIMBOLO", c, row, col))
            i += 1
            col += 1
        else:
            raise SyntaxError(f"Carácter inesperado '{c}' {row} {col}")
    
    return tokens

try:
    print(lexer("cadena;\ncadena"))
except SyntaxError as e:
    print(e)
