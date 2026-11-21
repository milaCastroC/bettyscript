from tokens import ErrorSemantico
import re
from arbol import (
    Numero,
    Variable,
    Cadena,
    OperacionBinaria,
    OperacionUnaria,
    Declaracion,
    Asignacion,
    Mostrar,
    Comparacion,
    Lectura,
    Condicional,
    Mientras,
    OperacionLogica,
    NegacionLogica,
    Booleano
)

ACEPTA = {
    "SEIS_SEMESTRES": (int,),
    "DEUDA_DE_PATRICIA": (int, float),
    "CHISME": (str,),
    "CHISME_CONFIRMADO": (bool,)
}

class Entorno:
    def __init__(self, padre=None):
        self.variables = {}
        self.padre = padre

    def buscar(self, nombre):
        if nombre in self.variables:
            return self
        if self.padre is not None:
            return self.padre.buscar(nombre)
        return None
    
class Interprete:
    def __init__(self):
        self.entorno=Entorno()


    def leer_entrada(self, nodo, tipo=None):
        etiqueta = tipo if tipo is not None else "CHISME"

        try:
            texto = input(f"AY_MARCE ({etiqueta})> ")
        except EOFError:
            raise ErrorSemantico(
                "no se recibió ningún valor de entrada",
                nodo.palabra.linea,
                nodo.palabra.columna
            )

        if tipo is None or tipo == "CHISME":
            return texto

        valor = texto.strip()

        if tipo == "SEIS_SEMESTRES":
            if re.fullmatch(r"[+-]?\d+", valor):
                try:
                    return int(valor)
                except ValueError:
                    pass
        
        
        elif tipo == "DEUDA_DE_PATRICIA":
            if re.fullmatch(r"[+-]?\d+", valor):
                return int(valor)

            if re.fullmatch(r"[+-]?\d+\.\d+", valor):
                return float(valor)


        elif tipo == "CHISME_CONFIRMADO":
            if valor == "TAN_DIVINO":
                return True

            if valor == "PELITEÑIDA":
                return False

        raise ErrorSemantico(
            f"no se puede convertir '{texto}' al tipo {tipo}",
            nodo.palabra.linea,
            nodo.palabra.columna
        )

    def evaluar_asignable(self, nodo, tipo):
        if isinstance(nodo, Lectura):
            return self.leer_entrada(nodo, tipo)

        return self.evaluar(nodo)

    def evaluar (self, nodo):
        if isinstance (nodo, Numero):
            texto= nodo.token.texto
            return float (texto) if "." in texto else int(texto)

        if isinstance (nodo, OperacionUnaria):
            valor = self.evaluar(nodo.valor)
            if type(valor) not in (int, float):
                raise ErrorSemantico(
                    f"no se puede usar '{nodo.operador.texto}' con valores no numéricos",
                    nodo.operador.linea,
                    nodo.operador.columna
                )
            return -valor
            
        if isinstance (nodo, Cadena):
            return nodo.token.texto[1:-1]

        
        if isinstance(nodo, Lectura):
            return self.leer_entrada(nodo)

        
        if isinstance (nodo, Variable):
            nombre= nodo.token.texto
            entorno = self.entorno.buscar(nombre)
            if entorno is None:
                raise ErrorSemantico(
                    f"variable '{nombre}' no ha sido declarada",
                    nodo.token.linea,
                    nodo.token.columna
                )
            return entorno.variables[nombre]["valor"]

        if isinstance (nodo, OperacionBinaria): 
            izq= self.evaluar(nodo.izq)
            der= self.evaluar(nodo.der)
            return self.operar (izq, nodo.operador, der)

        if isinstance (nodo, OperacionLogica):
            izq = self.evaluar(nodo.izq)
            op = nodo.operador.texto
            
            if type(izq) != bool:
                raise ErrorSemantico(
                    f"no se puede usar '{op}' con valores no booleanos",
                    nodo.operador.linea,
                    nodo.operador.columna
                )
            
            if op == "Y_ADEMAS_FLUIDEZ_MAMI":
                if not izq:
                    return False
                der = self.evaluar(nodo.der)

                if type(der) != bool:
                    raise ErrorSemantico(
                        f"no se puede usar '{op}' con valores no booleanos",
                        nodo.operador.linea,
                        nodo.operador.columna
                    )
                return der

            if op == "SI_NO_ES_ESTO_ES_AQUELLO":
                if izq:
                    return True
                der = self.evaluar(nodo.der)

                if type(der) != bool:
                    raise ErrorSemantico(
                        f"no se puede usar '{op}' con valores no booleanos",
                        nodo.operador.linea,
                        nodo.operador.columna
                    )
                return der
            
            raise ErrorSemantico(
                f"operador lógico '{op}' no reconocido",
                nodo.operador.linea,
                nodo.operador.columna
            )


        if isinstance(nodo, NegacionLogica):
            valor = self.evaluar(nodo.valor)

            if type(valor) != bool:
                raise ErrorSemantico(
                    f"no se puede usar '{nodo.operador.texto}' con valores no booleanos",
                    nodo.operador.linea,
                    nodo.operador.columna
                )

            return not valor


        if isinstance (nodo, Comparacion): 
            izq= self.evaluar(nodo.izq)
            der= self.evaluar(nodo.der)
            op = nodo.operador.texto

            # Igualdad entre booleanos
            if type(izq) is bool and type(der) is bool:
                if op == "==":
                    return izq == der

                if op == "!=":
                    return izq != der

                raise ErrorSemantico(
                    f"el operador '{op}' no admite booleanos",
                    nodo.operador.linea,
                    nodo.operador.columna
                )


            if type(izq) not in (int, float) or type(der) not in (int, float):
                raise ErrorSemantico(
                    f"no se puede usar '{op}' con valores no numéricos",
                    nodo.operador.linea,
                    nodo.operador.columna
                ) 

            if op == "==":
                return izq == der

            if op == "!=":
                return izq != der

            if op == "<":
                return izq < der

            if op == ">":
                return izq > der

            if op == "<=":
                return izq <= der

            if op == ">=":
                return izq >= der

        if isinstance(nodo, Booleano):
            if nodo.token.texto == "TAN_DIVINO":
                return True

            if nodo.token.texto == "PELITEÑIDA":
                return False


    def operar (self, izq, operador, der):
        op=operador.texto
        if type(izq) not in (int, float) or type(der) not in (int, float):
            raise ErrorSemantico(
                f"no se puede usar '{op}' con valores no numéricos",
                operador.linea,
                operador.columna
            )
        if op== "+":
            return izq + der
        if op== "-":
            return izq - der
        if op== "*":
            return izq * der
        if op== "/":
            if der==0:
                raise ErrorSemantico(
                    "Error: División por cero",
                    operador.linea,
                    operador.columna
                )
            if type(izq)==int and type(der)==int:
                return izq // der
                
                
            return izq / der

        raise ErrorSemantico(
            f"operador '{op}' no reconocido",
            operador.linea,
            operador.columna
        )

        
    
    def ejecutar(self, nodo):
        
        if isinstance (nodo, Declaracion):
            nombre = nodo.nombre.texto
            tipo = nodo.tipo.texto

            if nombre in self.entorno.variables:
                linea_original = self.entorno.variables[nombre]["linea"]
                raise ErrorSemantico(
                    f"la variable '{nombre}' ya ha sido declarada en la linea {linea_original}",
                    nodo.nombre.linea,
                    nodo.nombre.columna
                )
            valor = self.evaluar_asignable(nodo.valor, tipo)
            
            if type(valor) not in ACEPTA[tipo]:
                raise ErrorSemantico(
                    f"no se puede guardar un {type(valor).__name__} en la variable '{nombre}' de tipo {tipo}",
                    nodo.nombre.linea,
                    nodo.nombre.columna
                )
            
            self.entorno.variables[nombre]={
                "tipo": nodo.tipo.texto, 
                "valor": valor,
                "linea": nodo.nombre.linea
            }

        elif isinstance(nodo, Asignacion):
            nombre = nodo.nombre.texto
            entorno = self.entorno.buscar(nombre)

            if entorno is None:
                raise ErrorSemantico(
                    f"la variable '{nombre}' no ha sido declarada",
                    nodo.nombre.linea,
                    nodo.nombre.columna
                )
            tipo = entorno.variables[nombre]["tipo"]
            valor = self.evaluar_asignable(nodo.valor, tipo)


            if type(valor) not in ACEPTA[tipo]:
                raise ErrorSemantico(
                    f"no se puede guardar un {type(valor).__name__} en la variable '{nombre}' de tipo {tipo}",
                    nodo.nombre.linea,
                    nodo.nombre.columna
                )

            entorno.variables[nombre]["valor"] = valor
            
        elif isinstance(nodo, Mostrar):
            valor=self.evaluar(nodo.valor)
            print(valor)

        elif isinstance(nodo, Condicional):
            resultado = self.evaluar(nodo.condicion)

            if type(resultado) is not bool:
                raise ErrorSemantico(
                    "la condición debe ser de tipo CHISME_CONFIRMADO",
                    nodo.palabra.linea,
                    nodo.palabra.columna
                )

            if resultado:
                self.ejecutar_bloque(nodo.entonces)

            elif nodo.sino is not None:
                self.ejecutar_bloque(nodo.sino)

        
        elif isinstance(nodo, Mientras):
            vueltas = 0
            
            while True:
                resultado = self.evaluar(nodo.condicion)

                if type(resultado) is not bool:
                    raise ErrorSemantico(
                        "la condición debe ser de tipo CHISME_CONFIRMADO",
                        nodo.palabra.linea,
                        nodo.palabra.columna
                    )

                if not resultado:
                    break
                
                if vueltas >= 100000:
                    raise ErrorSemantico(
                        "el ciclo superó 100000 vueltas; "
                        "¿falta actualizar la variable de la condición?",
                        nodo.palabra.linea,
                        nodo.palabra.columna
                    )
                self.ejecutar_bloque(nodo.cuerpo)
                vueltas += 1

    def ejecutar_bloque(self, instrucciones):
        entorno_anterior = self.entorno
        self.entorno = Entorno(entorno_anterior)
        try:
            for instruccion in instrucciones:
                self.ejecutar(instruccion)
        finally:
            self.entorno = entorno_anterior

    def ejecutar_programa(self, programa):
        for instruccion in programa.instrucciones:
            self.ejecutar(instruccion)

