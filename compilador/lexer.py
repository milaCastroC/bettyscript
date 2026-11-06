from tokens import Token, ErrorLexico

#Implementación BettyScript
TIPOS = {"SEIS_SEMESTRES", "DEUDA_DE_PATRICIA", "CHISME", "BOOLEAN"}
SIMBOLOS = {";", "(", ")", "{", "}", "[", "]", "/", "=", "!", "."}
OPERADORES = {"+", "-", "*", ">", "<"}
OPERADORES_DOBLES = ("==", "!=", "<=", ">=")
PALABRAS_RESERVADAS = {"MOSCORROFIO", "SI_DON_ARMANDO_GRITA", "AHORA_SI", "PERDONEME_PERO_DISCULPEME", "NI_POR_EL_CHIRAS", "Y_ADEMAS_FLUIDEZ_MAMI", "SI_NO_ES_ESTO_ES_AQUELLO", "FREDDY_ANUNCIA", "MAQUILLAR_BALANCE", "EL_DIABLO_ES_PUERCO", "AY_MARCE"}
BOOLEANOS = {"TAN_DIVINO", "PELITEÑIDA"}
COMENTARIO = "OJO_PUES"
COMENTARIO_ABRE = "CARTA_DE_ARMANDO"
COMENTARIO_CIERRA = "SALUDOS_CORDIALES"

def tokenizar(texto):

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
                    raise ErrorLexico(f"Error NaN: Decimal mal formado", row, col)
                
                while i < len(texto) and texto[i].isdigit():
                    i += 1

                if i < len(texto) and texto[i].isdigit():
                    raise ErrorLexico(f"Error NaN: Decimal mal formado", row, col)
                
                tokens.append(Token("DEUDA_DE_PATRICIA", texto[inicio:i], row, col))
            else:
                tokens.append(Token("NUMERO", texto[inicio:i], row, col))
            col += len(texto[inicio:i])
        elif c == "'":
            inicio = i
            inicio_col = col
            i += 1

            while i < len(texto) and texto[i] not in ("'", "\n"):
                i += 1

            if i == len(texto) or texto[i] == "\n":
                raise ErrorLexico(f"Cadena sin cerrar", row, col)
            
            i += 1
            tokens.append(Token("CHISME", texto[inicio:i], row, col))
            col += len(texto[inicio:i])
        elif c.isalpha():
            inicio = i
            while i < len(texto) and (texto[i].isalnum() or texto[i] == "_"):
                i += 1
            palabra = texto[inicio:i]
            if palabra in TIPOS:
                tokens.append(Token("TIPO", palabra, row, col))
            elif palabra in PALABRAS_RESERVADAS:
                tokens.append(Token("PALABRA_RESERVADA", palabra, row, col))
            elif palabra in BOOLEANOS:
                tokens.append(Token("BOOLEANO", palabra, row, col))
            elif palabra == COMENTARIO:
                while i < len(texto) and texto[i] != "\n":
                    i += 1
            elif palabra == COMENTARIO_ABRE:
                row0, col0 = row, col
                col += len(palabra)
                cerrado = False
                while i < len(texto):
                    if texto.startswith(COMENTARIO_CIERRA, i):
                        i += len(COMENTARIO_CIERRA)
                        col += len(COMENTARIO_CIERRA)
                        cerrado = True
                        break
                    if texto[i] == "\n":
                        row += 1
                        col = 1
                    else:
                        col += 1
                    i += 1
                if not cerrado:
                    raise ErrorLexico(f"Comentario sin cerrar", row0, col0)
                continue
              
            else:
                tokens.append(Token("IDENTIFICADOR", texto[inicio:i], row, col))
            
           
            col+=len(palabra)
        
        elif texto.startswith (OPERADORES_DOBLES, i):
            tokens.append(Token("OPERADOR DOBLE", texto[i:i+2], row, col))
            i += 2
            col += 2

        elif c in SIMBOLOS:
            if c == ";":
                tokens.append(Token("FIN_LINEA", c, row, col))
            elif c == "=":
                tokens.append(Token("IGUAL_ASIGNACION", c, row, col))
            else:
                tokens.append(Token("SIMBOLO", c, row, col))
            i += 1
            col += 1
        elif c in OPERADORES:
            tokens.append(Token("OPERADOR", c, row, col))
            i += 1
            col += 1
        else:
            raise ErrorLexico(f"Carácter inesperado '{c}'", row, col)

    tokens.append(Token("EOF", "", row, col))
    return tokens

# try:
#     print("\n------------------Válido 1 - Simple------------------")
#     for token in tokenizar("SEIS_SEMESTRES total = a + 7 * 9;"):
#         print(token)

#     print("\n------------------Válido 2 - Sin espacios------------------")
#     for token in tokenizar("chismecito='BettyScript';"):
#         print(token)

#     print("\n------------------Válido 3 - Dos líneas y comentario------------------")
#     for token in tokenizar("CHISME saludo = 'hola'; OJO_PUES comentario\nDEUDA_DE_PATRICIA precio = 3.14;"):
#         print(token)

#     # print("\n------------------Inválido 1 - Carácter que no existe------------------")
#     # print(tokenizar("@SEIS_SEMESTRES35.865BFJSDH"))
    
#     print("\n------------------Inválido 2 - Decimal incorrecto------------------")
#     for token in tokenizar("double x = 12.544.7"):
#         print(token)

#     print("\n------------------Inválido 3 - Error segunda línea------------------")
#     for token in tokenizar("SEIS_SEMESTRES edad = 5;\nCHISME saludo = 'hola"):
#         print(token)

# except SyntaxError as e:
#     print(e)
