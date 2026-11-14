from tokens import ErrorSintactico
from arbol import *

class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def actual(self):
        return self.tokens[self.pos]

    def avanzar(self):
        t = self.tokens[self.pos]
        self.pos += 1
        return t

    def esperar(self, tipo, texto=None):
        t = self.actual()
        if t.tipo != tipo or (texto is not None and t.texto != texto):
            esperado = f"'{texto}'" if texto else f"un {tipo}"
            actual = "el fin del archivo" if t.tipo == "EOF" else f"'{t.texto}'"
            raise ErrorSintactico(f"se esperaba {esperado} y llegó {actual}", t.linea, t.columna)
        return self.avanzar()

    def programa(self):
        instrucciones = []
        while self.actual().tipo != "EOF":
            instrucciones.append(self.instruccion())
        return Programa(instrucciones)
    
    def instruccion(self):
        t = self.actual()
        if t.tipo == "TIPO":
            return self.declaracion()
        if t.tipo == "IDENTIFICADOR":
            return self.asignacion()
        raise ErrorSintactico(f"se esperaba el inicio de una instrucción y llegó '{t.texto}'",t.linea, t.columna)

    def declaracion(self):
        tipo = self.esperar("TIPO")
        nombre = self.esperar("IDENTIFICADOR") 
        self.esperar("SIMBOLO", "=")
        valor = self.expresion() 
        self.esperar("SIMBOLO", ";") 
        return Declaracion(tipo, nombre, valor)

    def asignacion(self):
        nombre = self.esperar("IDENTIFICADOR")
        self.esperar("SIMBOLO", "=")
        valor = self.expresion()
        self.esperar("SIMBOLO", ";")
        return Asignacion(nombre, valor)

    def expresion(self):
        izq = self.termino() # termino
        while self.actual().tipo == "OPERADOR" and self.actual().texto in ("+", "-"):
            operador = self.avanzar() # '+' o '-'
            der = self.termino() # termino
            izq = OperacionBinaria(izq, operador, der)
        return izq

    def termino(self):
        izq = self.factor() # factor
        while self.actual().tipo == "OPERADOR" and self.actual().texto in ("*", "/"):
            operador = self.avanzar() # '*' o '/'
            der = self.factor() # factor
            izq = OperacionBinaria(izq, operador, der)
        return izq
    
    def factor(self):
        t = self.actual()
        if t.tipo == "NUMERO":
            return Numero(self.avanzar())
        if t.tipo == "CADENA":
            return Cadena(self.avanzar())
        if t.tipo == "IDENTIFICADOR":
            return Variable(self.avanzar())
        if t.tipo == "SIMBOLO" and t.texto == "(":
            self.avanzar() # '('
            dentro = self.expresion() # expresion
            self.esperar("SIMBOLO", ")") # ')'
            return dentro
        raise ErrorSintactico(f"se esperaba un número, una variable o '(' y llegó '{t.texto}'",t.linea, t.columna)

    