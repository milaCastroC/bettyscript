# BettyScript

## 1. Nombre del lenguaje e integrantes

**Nombre del lenguaje:** BettyScript

**Integrantes del equipo:**
- Mariluz Calderon Guevara
- Sebastian Botero Gonzalez
- Maria Camila Castro Cardona

## 2. Cómo ejecutar

**Requisito:** Python 3.10 o superior. No requiere dependencias externas.

Clonar el repositorio:

```bash
git clone https://github.com/milaCastroC/bettyscript.git
cd bettyscript
```

## 3. Ficha del lenguaje

### Nombre y origen

**BettyScript** es un lenguaje de programación educativo e interpretado, desarrollado en Python e inspirado en la telenovela colombiana *Yo soy Betty, la fea*.

Su nombre combina **Betty**, protagonista de la historia, con **Script**, término utilizado en programación. El lenguaje transforma expresiones y referencias de Ecomoda en palabras reservadas, permitiendo aplicar conceptos de análisis léxico, análisis sintáctico e interpretación de programas mediante una sintaxis original.

### Tabla de traducción de Java a BettyScript

| Concepto | Java | BettyScript |
|---|---|---|
| Tipo entero | `int` | `SEIS_SEMESTRES` |
| Tipo decimal | `double` | `DEUDA_DE_PATRICIA` |
| Tipo cadena | `String` | `CHISME` |
| Tipo booleano | `boolean` | `CHISME_CONFIRMADO` |
| Verdadero | `true` | `TAN_DIVINO` |
| Falso | `false` | `PELITEÑIDA` |
| Asignación | `=` | `=` |
| Fin de instrucción | `;` | `;` |
| Salida | `System.out.println()` | `FREDDY_ANUNCIA()` |
| Condicional | `if` | `SI_DON_ARMANDO_GRITA` |
| Inicio del bloque verdadero | `{` | `AHORA_SI {` |
| Alternativa | `else` | `PERDONEME_PERO_DISCULPEME` |
| Ciclo | `while` | `INICIO_DEL_CHISME` |
| Comentario de línea | `//` | `OJO_PUES` |
| Comentario de bloque | `/* ... */` | `CARTA_DE_ARMANDO ... SALUDOS_CORDIALES` |

### Decisión de diseño

La principal decisión de diseño fue **reemplazar las palabras reservadas tradicionales por expresiones inspiradas en la cultura popular colombiana**, conservando elementos de programación como los operadores matemáticos, la asignación mediante `=`, el fin de instrucción `;` y los bloques delimitados por `{ }`.

A diferencia de Java, BettyScript utiliza expresiones como `SI_DON_ARMANDO_GRITA` para las condiciones, `INICIO_DEL_CHISME` para los ciclos y `FREDDY_ANUNCIA` para mostrar información.

Esta decisión permite mantener una estructura de programación reconocible y, al mismo tiempo, construir un lenguaje con identidad propia.

## 4. Gramática final en EBNF

```ebnf
programa ::= instruccion* EOF

instruccion ::= declaracion
              | asignacion
              | salida
              | condicional
              | ciclo

declaracion ::= TIPO IDENTIFICADOR "=" valor ";"

asignacion ::= IDENTIFICADOR "=" valor ";"

salida ::= "FREDDY_ANUNCIA" "(" valor ")" ";"

bloque ::= "{" instruccion* "}"

condicional ::= "SI_DON_ARMANDO_GRITA"
                "(" condicion ")"
                "AHORA_SI" bloque
                ("PERDONEME_PERO_DISCULPEME" bloque)?

ciclo ::= "INICIO_DEL_CHISME"
          "(" condicion ")"
          "AHORA_SI" bloque

valor ::= condicion

condicion ::= condicion_o

condicion_o ::= condicion_y
                ("SI_NO_ES_ESTO_ES_AQUELLO" condicion_y)*

condicion_y ::= condicion_no
                ("Y_ADEMAS_FLUIDEZ_MAMI" condicion_no)*

condicion_no ::= "NI_POR_EL_CHIRAS" condicion_no
               | condicion_atomica

condicion_atomica ::= expresion (COMPARADOR expresion)?
                    | "(" condicion ")"

expresion ::= termino (("+" | "-") termino)*

termino ::= factor (("*" | "/") factor)*

factor ::= "-" factor
         | NUMERO
         | CADENA
         | BOOLEAN
         | IDENTIFICADOR
         | "(" expresion ")"
         | lectura

lectura ::= "AY_MARCE" "(" ")"

TIPO ::= "SEIS_SEMESTRES"
       | "DEUDA_DE_PATRICIA"
       | "CHISME"
       | "CHISME_CONFIRMADO"

BOOLEAN ::= "TAN_DIVINO"
          | "PELITEÑIDA"

COMPARADOR ::= "=="
             | "!="
             | "<"
             | ">"
             | "<="
             | ">="
```

**Elementos léxicos:**
- `IDENTIFICADOR`: nombre de variable que comienza con una letra y puede contener letras, números y guiones bajos.
- `NUMERO`: número entero o decimal, utilizando el punto como separador decimal.
- `CADENA`: texto delimitado por comillas simples.
- `EOF`: final del archivo.

Los comentarios son reconocidos y descartados por el analizador léxico.

**Precedencia de operadores**, de mayor a menor:

1. Agrupación mediante paréntesis.
2. Negativo unario (`-`).
3. Multiplicación y división (`*`, `/`).
4. Suma y resta (`+`, `-`).
5. Comparaciones (`==`, `!=`, `<`, `>`, `<=`, `>=`).
6. Negación lógica (`NI_POR_EL_CHIRAS`).
7. Conjunción lógica (`Y_ADEMAS_FLUIDEZ_MAMI`).
8. Disyunción lógica (`SI_NO_ES_ESTO_ES_AQUELLO`).

## 5. Reglas de operaciones entre tipos

BettyScript utiliza **tipado explícito**. Cada variable debe declararse indicando su tipo y los valores asignados deben ser compatibles.

### Tipos de datos

| Tipo BettyScript | Tipo interno en Python | Valores admitidos |
|---|---|---|
| `SEIS_SEMESTRES` | `int` | Enteros |
| `DEUDA_DE_PATRICIA` | `int`, `float` | Enteros y decimales |
| `CHISME` | `str` | Cadenas |
| `CHISME_CONFIRMADO` | `bool` | Verdadero y falso |

### Operaciones aritméticas

Los operadores `+`, `-`, `*` y `/` aceptan exclusivamente valores numéricos.

| Operandos | Resultado |
|---|---|
| Entero con entero | Entero en suma, resta y multiplicación |
| Entero con decimal | Decimal |
| Decimal con decimal | Decimal |
| Entero dividido entre entero | División entera |
| División con operandos decimales | División real |
| Negativo unario aplicado a número | Número con signo invertido |

La división entre enteros utiliza `//` de Python, que redondea hacia abajo. La división con decimales utiliza `/`.

No se permiten operaciones aritméticas entre cadenas, booleanos o valores numéricos y cadenas. La división entre cero genera un error semántico.

### Comparaciones y operaciones lógicas

- Los valores numéricos admiten `==`, `!=`, `<`, `>`, `<=` y `>=`.
- Los valores booleanos admiten `==` y `!=` entre sí.
- Las operaciones de orden entre booleanos no están permitidas.
- Los operadores `Y_ADEMAS_FLUIDEZ_MAMI`, `SI_NO_ES_ESTO_ES_AQUELLO` y `NI_POR_EL_CHIRAS` trabajan con valores booleanos.
- Las operaciones lógicas de conjunción y disyunción utilizan evaluación de cortocircuito.
- Las condiciones de `SI_DON_ARMANDO_GRITA` e `INICIO_DEL_CHISME` deben devolver un valor booleano.

### Alcance de variables

BettyScript utiliza entornos anidados. Una variable declarada dentro de un bloque deja de estar disponible al terminar ese bloque.

Los bloques pueden consultar y modificar variables de entornos exteriores. También se permite el sombreado de variables, donde una declaración local tiene prioridad sobre otra externa con el mismo nombre.

Cada iteración de un ciclo utiliza un entorno local independiente.

### Validación de tipos y errores

El intérprete genera errores semánticos ante asignaciones incompatibles, variables no declaradas, operaciones inválidas o divisiones entre cero.

Los errores incluyen línea y columna. El programa también muestra un indicador `^` para señalar la ubicación del error dentro del código fuente.

Los ciclos tienen un límite de 100.000 iteraciones para evitar ejecuciones potencialmente infinitas.

## 6. Requerimientos electivos implementados

### 6.1. Electivo 1: Tipo booleano

**Objetivo:** permitir declarar variables booleanas y utilizarlas en expresiones y condiciones.

Se implementó el tipo `CHISME_CONFIRMADO`, con los siguientes valores:

- `TAN_DIVINO`: verdadero (`True`).
- `PELITEÑIDA`: falso (`False`).

Las variables booleanas pueden almacenar resultados de comparaciones, participar en operaciones lógicas y utilizarse directamente en condicionales y ciclos.

**Ejemplo:**

```text
SEIS_SEMESTRES nota = 4;

CHISME_CONFIRMADO aprobado = nota >= 3;

SI_DON_ARMANDO_GRITA (aprobado) AHORA_SI {
    FREDDY_ANUNCIA('Materia aprobada');
}
```

**Salida esperada:**

```text
Materia aprobada
```

**Implementación:** el lexer identifica los literales booleanos, el parser construye nodos `Booleano` y el intérprete utiliza el tipo `bool` de Python para evaluar y validar los valores.

Las asignaciones incompatibles producen errores semánticos.

### 6.2. Electivo 2: Lectura de datos

**Objetivo:** permitir que el usuario introduzca datos desde la consola, convertirlos al tipo esperado y detectar entradas inválidas.

Se implementó la expresión `AY_MARCE()`.

Cuando se utiliza directamente en una declaración o asignación, el intérprete identifica el tipo de la variable receptora y convierte el dato introducido.

| Tipo | Entrada válida | Conversión |
|---|---|---|
| `SEIS_SEMESTRES` | `25` | Entero |
| `DEUDA_DE_PATRICIA` | `4.5` | Decimal |
| `CHISME` | `Betty` | Cadena |
| `CHISME_CONFIRMADO` | `TAN_DIVINO` | Verdadero |
| `CHISME_CONFIRMADO` | `PELITEÑIDA` | Falso |

**Ejemplo:**

```text
CHISME nombre = AY_MARCE();
SEIS_SEMESTRES edad = AY_MARCE();

FREDDY_ANUNCIA(nombre);
FREDDY_ANUNCIA(edad);
```

**Ejecución esperada:**

```text
AY_MARCE (CHISME)> Betty
AY_MARCE (SEIS_SEMESTRES)> 25
Betty
25
```

**Implementación:** el parser reconoce `AY_MARCE()` y construye un nodo `Lectura`. El intérprete utiliza `input()` para solicitar información y convierte el resultado según el tipo esperado.

Las entradas numéricas se validan mediante expresiones regulares y las booleanas únicamente admiten `TAN_DIVINO` o `PELITEÑIDA`.

Si la entrada no puede convertirse al tipo solicitado, se genera un error semántico con línea y columna.

La conversión según el tipo se aplica a lecturas directas en declaraciones y asignaciones. Sin una variable receptora, la lectura devuelve una cadena.