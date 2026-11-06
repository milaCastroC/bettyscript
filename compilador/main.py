import sys
from lexer import tokenizar

if __name__ == "__main__":
    with open("ejemplo.txt", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    tokens = tokenizar(contenido)

    print(f"{'LINEA':<6}{'COL':<5}{'TIPO':<20}TEXTO")
    for token in tokens:
        print(f"{token.linea:<6}{token.columna:<5}{token.tipo:<20}{token.texto}")

    print("-------------------------------------")
    for token in tokens:
        print(token)
