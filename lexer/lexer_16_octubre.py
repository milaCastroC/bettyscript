#Implementación BettyScript
TIPOS = {"SEIS_SEMESTRES", "DEUDA_DE_PATRICIA", "CHISME", "BOOLEAN"}
SIMBOLOS = {";", "(", ")", "{", "}", "[", "]", "/", "=", "<", ">", "!"}
OPERADORES = {"+", "-", "*"}
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

            if i < len(texto) and texto[i] == ".":
                i += 1

                if i == len(texto) or not texto[i].isdigit():
                    raise SyntaxError(f"Error NaN: Decimal mal formado en línea {row}, columna{col}")
                
                while i < len(texto) and texto[i].isdigit():
                    i += 1

                if i < len(texto) and texto[i].isdigit():
                    raise SyntaxError(f"Error NaN: Decimal mal formado en línea {row}, columna{col}")
                
                tokens.append(("DEUDA_DE_PATRICIA", texto[inicio:i], row, col))
            else:
                tokens.append(("NUMERO", texto[inicio:i], row, col))
            col += len(texto[inicio:i])
        elif c == "'":
            inicio = i
            inicio_col = col
            i += 1

            while i < len(texto) and texto[i] not in ("'", "\n"):
                i += 1

            if i == len(texto) or texto[i] == "\n":
                raise SyntaxError(f"Error léxico: cadena sin cerrar en línea {row}, columna{inicio_col}")
            
            i += 1
            tokens.append(("CHISME", texto[inicio:i], row, col))
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
        elif c in OPERADORES:
            tokens.append(("OPERADOR", c, row, col))
            i += 1
            col += 1
        else:
            raise SyntaxError(f"Error léxico: carácter inesperado '{c}' en línea {row}, columna {col}")
    
    return tokens

try:
    print("Válido 1 - Simple")
    print(lexer("SEIS_SEMESTRES total = a + 7 * 9;"))
    print("Válido 2 - Sin espacios")
    print(lexer("chismecito='BettyScript';"))
    print("Válido 3 - Dos líneas y comentario")
    print(lexer("CHISME saludo = 'hola'; OJO_PUES comentario\nDEUDA_DE_PATRICIA precio = 3.14;"))
    # print("Inválido 1 - Carácter que no existe")
    # print(lexer("@SEIS_SEMESTRES35.865BFJSDH"))
    print("Inválido 2 - Decimal incorrecto")
    print(lexer("double x = 12.544"))
    print("Inválido 3 - Error segunda línea")
    print(lexer("SEIS_SEMESTRES edad = 5;\nCHISME saludo = 'hola"))
    
except SyntaxError as e:
    print(e)
