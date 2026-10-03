# MiniEjercicio 1
print("\n---Miniejercicio 1---")

nombre = 'Camiluztian'
edad = 21
print (f"Mi nombre es: {nombre} y tengo {edad}")
edad += 1
print(f"Ahora tengo: {edad}")

#Miniejercicio 2
print("\n---Miniejercicio 2---")

texto = 'a1b22c'
i = 0
while i < len(texto):
    if(texto[i].isdigit()):
        print(texto[i])
    i += 1

#Miniejercicio 3
print("\n---Miniejercicio3---")

texto = 'a1b22c'
i = 0
tokens = []

while i < len(texto):
    if(texto[i].isdigit()):
        tokens.append(("DIGITO", texto[i]))
    i += 1

print(tokens)

#Miniejercicio 4
print("\n---Miniejercicio 4---")

texto = 'a1b22c'

def digitos(texto):
    i = 0
    tokens = []
    while i < len(texto):
        if(texto[i].isdigit()):
            tokens.append(("DIGITO", texto[i]))
        i += 1
    return tokens

print(digitos('a1b22c'))
print(digitos('3H'))
print(digitos('CamiluztianHerrera1234'))

#Miniejercicio 5
print("\n---Miniejercicio 5---")

def digitos_exception(texto):
    i = 0
    tokens = []
    while i < len(texto):
        if(texto[i].isdigit()):
            tokens.append(("DIGITO", texto[i]))
        elif(texto[i].isalpha()):
             tokens.append(("LETRA", texto[i]))
        else:
            raise SyntaxError(f"El caracter {texto[i]} no es dígito ni letra")
        i += 1
    return tokens

print("\n---Miniejercicio 5 sin error---")
try:
    print(digitos_exception("a1b"))
except SyntaxError as e:
    print(e)
print("\n---Miniejercicio 5 con error---")
try:
    print(digitos_exception("a1@"))
except SyntaxError as e:
    print(e)