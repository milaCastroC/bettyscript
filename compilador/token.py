from dataclasses import dataclass
@dataclass
class Token:
    tipo: str
    texto: str
    linea: int
    columna: int
t = Token("NUMERO", "5", 1, 9) # se crea un objeto
print(t.tipo) # NUMERO
print(t.columna) # 9    