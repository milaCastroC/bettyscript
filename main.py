import sys

from lexer import tokenizar
from tokens import ErrorDeLenguaje
from parser import Parser
from arbol import mostrar_arbol
from interprete import Interprete


def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py programa.txt")
        return

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        codigo = f.read()
        lineas = codigo.splitlines()
    try:
        tokens = tokenizar(codigo)
        programa = Parser(tokens).programa()
        Interprete().ejecutar_programa(programa)

        # Mostrar arbol
        # mostrar_arbol(programa)

    except ErrorDeLenguaje as e:
        print(e)
        if 1 <= e.linea <= len(lineas):
            linea_codigo = lineas[e.linea - 1]
            print(linea_codigo)
            print(" " * (e.columna - 1) + "^")

        elif (e.linea == len(lineas) + 1 and codigo.endswith(("\n", "\r"))and lineas):
            ultima_linea = lineas[-1]
            print(ultima_linea)
            print(" " * len(ultima_linea) + "^")


if __name__ == "__main__":
    main()