import lexer

class Parser: # 1. se define la plantilla

    def __init__(self, tokens): # 2. se ejecuta solo al crear un Parser
        self.tokens = tokens # 3. guarda la lista dentro del objeto
        self.pos = 0 # 4. el dedo: empieza en el token 0

    def actual(self): # 5. acción: dice en qué token va el dedo
        return self.tokens[self.pos]

    def avanzar(self): # 6. acción: mueve el dedo una posición
        self.pos += 1   

class ErrorLexico(Exception):
    def __init__(self, mensaje, linea, columna):
        super().__init__(
            f"Error léxico en línea {linea}, columna {columna}: {mensaje}"
        )
        self.linea = linea
        self.columna = columna
