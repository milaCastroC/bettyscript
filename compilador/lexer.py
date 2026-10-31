#Implementación BettyScript
TIPOS = {"SEIS_SEMESTRES", "DEUDA_DE_PATRICIA", "CHISME", "BOOLEAN"}
SIMBOLOS = {";", "(", ")", "{", "}", "[", "]", "/", "=", "<", ">", "!", "."}
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
            elif palabra in PALABRAS_RESERVADAS:
                tokens.append(("PALABRA_RESERVADA", palabra, row, col))
            elif palabra in BOOLEANOS:
                tokens.append(("BOOLEANO", palabra, row, col))
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
                    raise SyntaxError(f"Error léxico en línea {row0}, columna {col0}: comentario sin cerrar")
                continue
              
            else:
                tokens.append(("IDENTIFICADOR", texto[inicio:i], row, col))
            
           
            col+=len(palabra)
        
        elif texto.startswith (OPERADORES_DOBLES, i):
            tokens.append(("OPERADOR DOBLE", texto[i:i+2], row, col))
            i += 2
            col += 2

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
    
    tokens.append(("EOF", c, row, col))
    return tokens

#try:
#     print(lexer.tokenizar("(a+b)*2;"))
#     print(lexer.tokenizar("system.out"))
#     print(lexer.tokenizar("x >= 3.14;"))
#     print(lexer.tokenizar("SI_DON_ARMANDO_GRITA (coleccion_actual == MOSCORROFIO) AHORA_SI {FREDDY_ANUNCIA('¡Hugo se quedó sin conceptos!');"))
#     print(lexer.tokenizar("CARTA_DE_ ARMANDO hola SALUDOS_CORDIALES"))



    
# except SyntaxError as e:
#     print(e)
