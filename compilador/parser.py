from tokens import ErrorSintactico
from arbol import *

# GRAMATICA EBNF - BETTYSCRIPT
#
# programa    ::= instruccion* EOF
# instruccion ::= declaracion | asignacion | salida | condicional | ciclo
# declaracion ::= TIPO IDENTIFICADOR '=' expresion ';'
# asignacion  ::= IDENTIFICADOR '=' expresion ';'
#
# expresion   ::= termino (('+' | '-') termino)*
# termino     ::= factor (('*' | '/') factor)*
#
# factor      ::= NUMERO
#               | CADENA
#               | IDENTIFICADOR
#               | '(' expresion ')'
# instruccion ::= declaracion | asignacion | salida
#
# salida ::= 'FREDDY_ANUNCIA' '(' expresion ')' ';'
#
# bloque ::= '{' instruccion* '}'

# condicional ::= 'SI_DON_ARMANDO_GRITA'
#                 '(' condicion ')'
#                 'AHORA_SI' bloque
#                 ('PERDONEME_PERO_DISCULPEME' bloque)?
#
# ciclo ::= 'INICIO_DEL_CHISME'
#           '(' condicion ')'
#           'AHORA_SI' bloque



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
        if t.tipo == "PALABRA_RESERVADA" and t.texto == "FREDDY_ANUNCIA":
            return self.salida()
        if t.tipo == "PALABRA_RESERVADA" and t.texto == "SI_DON_ARMANDO_GRITA":
            return self.condicional()
        if (t.tipo == "PALABRA_RESERVADA"and t.texto == "INICIO_DEL_CHISME"):
            return self.ciclo()
        raise ErrorSintactico(
            f"se esperaba el inicio de una instrucción y llegó '{t.texto}'",
            t.linea,
            t.columna
        )


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

    def salida(self):
            palabra = self.esperar("PALABRA_RESERVADA", "FREDDY_ANUNCIA")
            self.esperar("SIMBOLO", "(")
            valor = self.expresion()
            self.esperar("SIMBOLO", ")")
            self.esperar("SIMBOLO", ";")
            
            return Mostrar(palabra, valor)

    def condicion(self):
        izq = self.expresion()
        operador = self.esperar("COMPARADOR")
        der = self.expresion()
        return Comparacion(izq, operador, der)

    def bloque(self):
        llave = self.esperar("SIMBOLO", "{")
        instrucciones = []
        while not (self.actual().tipo == "SIMBOLO" and self.actual().texto == "}"):
            if self.actual().tipo == "EOF":
                t = self.actual()
                raise ErrorSintactico(f"falta '}}' para cerrar el bloque abierto en la línea {llave.linea}",t.linea, t.columna)
            instrucciones.append(self.instruccion())
        self.avanzar()
        return instrucciones

    def condicional(self):
        palabra = self.esperar("PALABRA_RESERVADA", "SI_DON_ARMANDO_GRITA")

        self.esperar("SIMBOLO", "(")
        condicion = self.condicion()
        self.esperar("SIMBOLO", ")")

        self.esperar("PALABRA_RESERVADA", "AHORA_SI")
        entonces = self.bloque()

        sino = None

        if(self.actual().tipo == "PALABRA_RESERVADA"  and self.actual().texto == "PERDONEME_PERO_DISCULPEME"):
            self.avanzar()
            sino = self.bloque()

        return Condicional(palabra, condicion, entonces, sino)

    def ciclo(self):
        palabra = self.esperar("PALABRA_RESERVADA","INICIO_DEL_CHISME")

        self.esperar("SIMBOLO", "(")
        condicion = self.condicion()
        self.esperar("SIMBOLO", ")")

        self.esperar("PALABRA_RESERVADA", "AHORA_SI")

        cuerpo = self.bloque()

        return Mientras(palabra, condicion, cuerpo)
