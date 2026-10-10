#Implementación BettyScript
TIPOS = {"SEIS_SEMESTRES", "DEUDA_DE_PATRICIA", "CHISME", "BOOLEAN"}
SIMBOLOS = {";", "(", ")", "{", "}", "[", "]", "+", "-", "*", "/", "=", "<", ">", "!"}
COMENTARIO = "OJO_PUES"

def lexer(texto):

    tokens = []
    i = 0
    col = 1
    row = 1

    while i < len(texto):
        c = texto[i]

        if c == " ":
            i += 1
            col += 1
        elif c == "\n":
            col = 1
            row += 1
            i += 1
        elif c.isdigit():
            inicio = i
            while i < len(texto) and texto[i].isdigit():
                i += 1
            tokens.append(("NUMERO", texto[inicio:i], row, col))
            col += len(texto[inicio:i])
        elif c.isalpha():
            inicio = i
            while i < len(texto) and (texto[i].isalnum() or texto[i] == "_"):
                i += 1
            palabra = texto[inicio:i]
            if palabra in TIPOS:
                tokens.append(("TIPO", palabra, row, col))
            elif palabra == COMENTARIO:
                while i < len(texto) and texto[i] != "\n":
                    i += 1
              
            else:
                tokens.append(("IDENTIFICADOR", texto[inicio:i], row, col))
            
           
            col+=len(palabra)
            
        elif c in SIMBOLOS:
            if c == ";":
                tokens.append(("FIN", c, row, col))
            elif c == "=":
                tokens.append(("IGUAL_ASIGNACION", c, row, col))
            else:
                tokens.append(("SIMBOLO", c, row, col))
            i += 1
            col += 1
        else:
            raise SyntaxError(f"Error léxico: carácter inesperado '{c}' en línea {row}, columna {col}")
    
    return tokens

try:
    print(lexer("SEIS_SEMESTRES edad = 5@;\nOJO_PUES Este es un comentario\nDEUDA_DE_PATRICIA deuda = 100;"))
except SyntaxError as e:
    print(e)
