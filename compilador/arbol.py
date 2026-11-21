from dataclasses import dataclass
from tokens import Token

@dataclass
class Numero:
    token: Token

@dataclass
class Variable:
    token: Token

@dataclass
class Cadena:
    token: Token

@dataclass
class Declaracion: 
    tipo: Token
    nombre: Token
    valor: object

@dataclass
class Asignacion: 
    nombre: Token
    valor: object

@dataclass
class Mostrar:
    palabra: Token
    valor: object

@dataclass
class Programa:
    instrucciones: list

@dataclass
class OperacionBinaria:
    izq: object
    operador: Token
    der: object

@dataclass
class Comparacion:
    izq: object
    operador: Token
    der: object

@dataclass
class Condicional:
    palabra: Token
    condicion: object
    entonces: list
    sino: list | None

@dataclass
class OperacionLogica:
    izq: object
    operador: Token
    der: object

@dataclass
class NegacionLogica:
    operador: Token
    valor: object


@dataclass
class Mientras:
    palabra: Token
    condicion: object
    cuerpo: list


def mostrar_arbol(nodo, nivel=0):
    espacio = "  " * nivel

    if isinstance(nodo, Programa):
        print(f"{espacio}Programa")
        for instruccion in nodo.instrucciones:
            mostrar_arbol(instruccion, nivel + 1)

    elif isinstance(nodo, Declaracion):
        print(f"{espacio}Declaracion {nodo.tipo.texto} {nodo.nombre.texto}")
        mostrar_arbol(nodo.valor, nivel + 1)

    elif isinstance(nodo, Asignacion):
        print(f"{espacio}Asignacion {nodo.nombre.texto}")
        mostrar_arbol(nodo.valor, nivel + 1)

    elif isinstance(nodo, Mostrar):
        print(f"{espacio}Mostrar {nodo.palabra.texto}")
        mostrar_arbol(nodo.valor, nivel + 1)

    elif isinstance(nodo, OperacionBinaria):
        print(f"{espacio}OperacionBinaria {nodo.operador.texto}")
        mostrar_arbol(nodo.izq, nivel + 1)
        mostrar_arbol(nodo.der, nivel + 1)

    elif isinstance(nodo, Numero):
        print(f"{espacio}Numero {nodo.token.texto}")

    elif isinstance(nodo, Variable):
        print(f"{espacio}Variable {nodo.token.texto}")

    elif isinstance(nodo, Cadena):
        print(f"{espacio}Cadena {nodo.token.texto}")

    elif isinstance(nodo, Comparacion):
        print(f"{espacio}Comparacion {nodo.operador.texto}")
        mostrar_arbol(nodo.izq, nivel + 1)
        mostrar_arbol(nodo.der, nivel + 1)

    elif isinstance(nodo, OperacionLogica):
        print(f"{espacio}OperacionLogica {nodo.operador.texto}")
        mostrar_arbol(nodo.izq, nivel + 1)
        mostrar_arbol(nodo.der, nivel + 1)

    elif isinstance(nodo, NegacionLogica):
        print(f"{espacio}NegacionLogica {nodo.operador.texto}")
        mostrar_arbol(nodo.valor, nivel + 1)

    elif isinstance(nodo, Condicional):
        print(f"{espacio}Condicional")

        print(f"{espacio}  Condicion:")
        mostrar_arbol(nodo.condicion, nivel + 2)

        print(f"{espacio}  Entonces:")
        for instruccion in nodo.entonces:
            mostrar_arbol(instruccion, nivel + 2)

        if nodo.sino is not None:
            print(f"{espacio}  Sino:")
            for instruccion in nodo.sino:
                mostrar_arbol(instruccion, nivel + 2)
    
    elif isinstance(nodo, Mientras):
        print(f"{espacio}Mientras")

        print(f"{espacio}  Condicion:")
        mostrar_arbol(nodo.condicion, nivel + 2)

        print(f"{espacio}  Cuerpo:")
        for instruccion in nodo.cuerpo:
            mostrar_arbol(instruccion, nivel + 2)

