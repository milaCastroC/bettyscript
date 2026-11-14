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

    try:
        tokens = tokenizar(codigo)
        programa = Parser(tokens).programa()
        Interprete().ejecutar_programa(programa)

    except ErrorDeLenguaje as e:
        print(e)
        print(f"linea = {e.linea}, columna = {e.columna}")


if __name__ == "__main__":
    main()