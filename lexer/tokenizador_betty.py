#Implementación BettyScript
def tokeniza_betty(texto):

    tokens = []
    i = 0

    while i < len(texto):
        c = texto[i]

        if c == " ":
            i += 1
        elif c.isdigit():
            inicio = i
            while i < len(texto) and texto[i].isdigit():
                i += 1
            tokens.append(("SEIS_SEMESTRES", texto[inicio:i]))
        elif c.isalpha():
                inicio = i
                while i < len(texto) and texto[i].isalpha():
                    i += 1
                tokens.append(("CHISME", texto[inicio:i]))
        elif c == ";":
            tokens.append(("FIN", c))
            i += 1
        else:
            raise SyntaxError(f"Carácter inesperado '{c}'")
    
    return tokens

try:
    print(tokeniza_betty("7888a1parangaricutirimicuaro1234holi"))
except SyntaxError as e:
    print(e)