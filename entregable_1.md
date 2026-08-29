# Entregable 1 — BettyScript

## Nombre del lenguaje

**BettyScript**

## Integrantes

- Botero
- Calderon
- Castro

---

## 1. Dominio del sistema

El dominio de este proyecto se centra en el diseño, especificación y construcción de un lenguaje formal llamado **BettyScript**. La principal característica de este lenguaje es que su sintaxis, palabras reservadas, tipos de datos y estructuras de control están construidas íntegramente a partir del léxico, las frases icónicas y las referencias culturales de la telenovela colombiana *Yo soy Betty, la fea*.

---

# 2. Reglas en lenguaje natural

## 2.1. Reglas con una sola condición

### Regla 1: Verificación de chisme real

Si `rumor_confirmado` es verdadero, se imprime **“¡Atención Ecomoda, último minuto!”**.

```bettyscript
SI_DON_ARMANDO_GRITA (rumor_confirmado == TAN_DIVINO) AHORA_SI {
    FREDDY_ANUNCIA("¡Atención Ecomoda, último minuto!");
}
```

### Regla 2: Prevención de nulos en diseños

Si `coleccion_actual` tiene un valor nulo, se muestra **“¡Hugo se quedó sin conceptos!”**.

```bettyscript
SI_DON_ARMANDO_GRITA (coleccion_actual == MOSCORROFIO) AHORA_SI {
    FREDDY_ANUNCIA("¡Hugo se quedó sin conceptos!");
}
```

### Regla 3: Control de acceso privado en gerencia

Declara un dato privado de tipo texto llamado `secreto_presidencial` con el valor `"Terramoda"`. Si `secretaria_ocupada` es verdadero, se muestra **“No se puede pasar a la oficina principal.”**.

```bettyscript
BAJE_LA_VOZ_BEATRIZ CHISME secreto_presidencial = "Terramoda";

SI_DON_ARMANDO_GRITA (secretaria_ocupada == TAN_DIVINO) AHORA_SI {
    FREDDY_ANUNCIA("No se puede pasar a la oficina principal.");
}
```

---

## 2.2. Reglas con condiciones compuestas usando Y / O

### Regla 4: Filtro de contratación con Y lógico

Si `estudio_finanzas` y `recomendacion_valida` son verdaderos, se muestra **“Bienvenida al corporativo.”**.

```bettyscript
SI_DON_ARMANDO_GRITA (
    estudio_finanzas == TAN_DIVINO
    Y_ADEMAS_FLUIDEZ_MAMI
    recomendacion_valida == TAN_DIVINO
) AHORA_SI {
    FREDDY_ANUNCIA("Bienvenida al corporativo.");
}
```

### Regla 5: Emergencia de Patricia con O lógico

Si `sin_gasolina` o `tarjeta_bloqueada` son verdaderos, se muestra **“¡Alguien auxilie a la peliteñida!”**.

```bettyscript
SI_DON_ARMANDO_GRITA (
    sin_gasolina == TAN_DIVINO
    SI_NO_ES_ESTO_ES_AQUELLO
    tarjeta_bloqueada == TAN_DIVINO
) AHORA_SI {
    FREDDY_ANUNCIA("¡Alguien auxilie a la peliteñida!");
}
```

### Regla 6: Condición compuesta mixta (Y / O) para almuerzos

Si `es_del_cuartel` es verdadero y además `es_hora_almuerzo` o `inesita_termino` son verdaderos, se muestra **“¡Vámonos a almorzar, muchachas!”**.

```bettyscript
SI_DON_ARMANDO_GRITA (
    es_del_cuartel == TAN_DIVINO
    Y_ADEMAS_FLUIDEZ_MAMI
    (
        es_hora_almuerzo == TAN_DIVINO
        SI_NO_ES_ESTO_ES_AQUELLO
        inesita_termino == TAN_DIVINO
    )
) AHORA_SI {
    FREDDY_ANUNCIA("¡Vámonos a almorzar, muchachas!");
}
```

---

## 2.3. Reglas que combinan tipos de datos distintos (Numérico + Booleano)

### Regla 7: Alerta de deuda y cuentas congeladas

Si `deuda_dolares` es mayor a `1.000.000` y `cuentas_congeladas` es verdadero, se lanza una excepción financiera con el mensaje **“¡Nos van a quitar Ecomoda!”**.

```bettyscript
DEUDA_DE_PATRICIA deuda_dolares = 2000000;

SI_DON_ARMANDO_GRITA (
    deuda_dolares > 1000000
    Y_ADEMAS_FLUIDEZ_MAMI
    cuentas_congeladas == TAN_DIVINO
) AHORA_SI {
    AY_MARCE ExcepcionFinanciera("¡Nos van a quitar Ecomoda!");
}
```

### Regla 8: Restricción de presupuesto para diseñadores

Si `presupuesto_diseno` es menor a `5.000` y `usar_telas_nacionales` es verdadero, se muestra **“Hugo Lombardi ha renunciado furioso.”**.

```bettyscript
SEIS_SEMESTRES presupuesto_diseno = 3500;

SI_DON_ARMANDO_GRITA (
    presupuesto_diseno < 5000
    Y_ADEMAS_FLUIDEZ_MAMI
    usar_telas_nacionales == TAN_DIVINO
) AHORA_SI {
    FREDDY_ANUNCIA("Hugo Lombardi ha renunciado furioso.");
}
```

---

## 2.4. Reglas adicionales del lenguaje

### Regla 9: Alternativa diplomática con Else

Si `armando_presente` es verdadero, se muestra **“Paso la llamada a presidencia.”**; de lo contrario, se muestra **“El doctor se encuentra en una reunión muy importante.”**.

```bettyscript
SI_DON_ARMANDO_GRITA (armando_presente == TAN_DIVINO) AHORA_SI {
    FREDDY_ANUNCIA("Paso la llamada a presidencia.");
} PERDONEME_PERO_DISCULPEME {
    FREDDY_ANUNCIA("El doctor se encuentra en una reunión muy importante.");
}
```

### Regla 10: Negación estricta con NOT (!)

Si `es_miembro_junta` no es verdadero, se muestra **“Usted no tiene acceso a esta sección.”**.

```bettyscript
SI_DON_ARMANDO_GRITA (NI_POR_EL_CHIRAS es_miembro_junta) AHORA_SI {
    FREDDY_ANUNCIA("Usted no tiene acceso a esta sección.");
}
```

### Regla 11: Bloque Try protegido

Se intenta mostrar **“Presentando informe a la junta...”** y, si ocurre un error, se muestra **“¡Nos descubrieron los auditores!”**.

```bettyscript
MAQUILLAR_BALANCE {
    FREDDY_ANUNCIA("Presentando informe a la junta...");
} EL_DIABLO_ES_PUERCO (error) {
    FREDDY_ANUNCIA("¡Nos descubrieron los auditores!");
}
```

### Regla 12: Retorno final de datos

Devuelve verdadero.

```bettyscript
ENTREGUE_EL_BALANCE TAN_DIVINO;
```

### Regla 13: Definición pública global

Declara una variable pública de tipo texto llamada `estado_actual` con el valor `"En crisis"`.

```bettyscript
QUE_SE_ENTERE_TODA_ECOMODA CHISME estado_actual = "En crisis";
```

### Regla 14: Validación de saldos vacíos

Si `saldo_celular` es igual a `0`, se muestra **“Por favor, ¿me presta para una llamadita?”**.

```bettyscript
SI_DON_ARMANDO_GRITA (saldo_celular == 0) AHORA_SI {
    FREDDY_ANUNCIA("Por favor, ¿me presta para una llamadita?");
}
```

### Regla 15: Lanzamiento directo de error

Si `mercedes_rayado` es verdadero, se lanza una excepción de tragedia con el mensaje **“¡Me arruinaron el carro!”**.

```bettyscript
SI_DON_ARMANDO_GRITA (mercedes_rayado == TAN_DIVINO) AHORA_SI {
    AY_MARCE ExcepcionTragedia("¡Me arruinaron el carro!");
}
```

---

# 3. Palabras reservadas

| **Tipo de dato / elemento en Java** | **Palabra reservada BettyScript** | **Significado** | **Categoría** |
|---|---|---|---|
| **Tipos de datos** |  |  |  |
| `int` | `SEIS_SEMESTRES` | Tipo numérico entero | Palabra clave (Tipo de dato) |
| `double` | `DEUDA_DE_PATRICIA` | Tipo numérico decimal | Palabra clave (Tipo de dato) |
| `String` | `CHISME` | Cadena de caracteres (texto) | Palabra clave (Tipo de dato) |
| `null` | `MOSCORROFIO` | Valor nulo o sin asignar | Literal (Nulo) |
| **Operadores y literales** |  |  |  |
| `true` | `TAN_DIVINO` | Valor lógico verdadero | Literal (Booleano) |
| `false` | `PELITEÑIDA` | Valor lógico falso | Literal (Booleano) |
| `==`, `!=`, `>`, `<`, `>=`, `<=` | `==`, `!=`, `>`, `<`, `>=`, `<=` | Comparación de valores | Operador relacional |
| `+`, `-`, `*`, `/`, `%` | `+`, `-`, `*`, `/`, `%` | Operaciones matemáticas | Operador aritmético |
| **Condicionales** |  |  |  |
| `if` | `SI_DON_ARMANDO_GRITA` | Inicia un bloque condicional | Palabra clave (Control de flujo) |
| `then` / entonces | `AHORA_SI` | Delimita qué hacer si la condición es verdadera | Palabra clave (Control de flujo) |
| `else` | `PERDONEME_PERO_DISCULPEME` | Alternativa si la condición es falsa | Palabra clave (Control de flujo) |
| `&&` (AND) | `Y_ADEMAS_FLUIDEZ_MAMI` | Conjunción lógica (Y) | Operador lógico |
| `||` (OR) | `SI_NO_ES_ESTO_ES_AQUELLO` | Disyunción lógica (O) | Operador lógico |
| `!` (NOT) / negación | `NI_POR_EL_CHIRAS` | Negación lógica (NO) | Operador lógico |
| **Ciclos y control de flujo** |  |  |  |
| `return` | `ENTREGUE_EL_BALANCE` | Devuelve un valor al final | Palabra clave (Control de flujo) |
| inicio `while` | `INICIO_DEL_CHISME` | Inicia un ciclo iterativo | Palabra clave (Control de flujo) |
| `break` | `SE_ACABO_EL_CHISME` | Rompe y sale del ciclo actual | Palabra clave (Control de flujo) |
| `continue` | `SIGAMOS_CON_EL_CHISME` | Salta a la siguiente iteración | Palabra clave (Control de flujo) |
| **Manejo de errores** |  |  |  |
| `throw` (Error) | `AY_MARCE` | Lanza una excepción o error | Palabra clave (Manejo de errores) |
| `try` | `MAQUILLAR_BALANCE` | Inicia un bloque protegido | Palabra clave (Manejo de errores) |
| `catch` | `EL_DIABLO_ES_PUERCO` | Captura y maneja un error | Palabra clave (Manejo de errores) |
| `print()` | `FREDDY_ANUNCIA` | Imprime un mensaje en pantalla | Palabra clave (Salida) |
| **Modificadores de acceso** |  |  |  |
| `private` | `BAJE_LA_VOZ_BEATRIZ` | Restringe el acceso (Privado) | Palabra clave (Modificador de acceso) |
| `public` | `QUE_SE_ENTERE_TODA_ECOMODA` | Permite el acceso global (Público) | Palabra clave (Modificador de acceso) |

---

# 4. Tabla de clasificación de variables

| **Variable** | **Tipo en Java** | **Ejemplo** |
|---|---|---|
| `rumor_confirmado` | `boolean` | `true` |
| `coleccion_actual` | `String` | `"verano"` |
| `secreto_presidencial` | `String` | `"Terramoda"` |
| `secretaria_ocupada` | `boolean` | `false` |
| `estudio_finanzas` | `boolean` | `true` |
| `recomendacion_valida` | `boolean` | `false` |
| `sin_gasolina` | `boolean` | `true` |
| `tarjeta_bloqueada` | `boolean` | `false` |
| `es_del_cuartel` | `boolean` | `true` |
| `es_hora_almuerzo` | `boolean` | `false` |
| `inesita_termino` | `boolean` | `true` |
| `deuda_dolares` | `double` | `1000000` |
| `cuentas_congeladas` | `boolean` | `false` |
| `presupuesto_diseno` | `int` | `3500` |
| `usar_telas_nacionales` | `boolean` | `false` |
| `armando_presente` | `boolean` | `true` |
| `es_miembro_junta` | `boolean` | `false` |
| `estado_actual` | `String` | `"En crisis"` |
| `saldo_celular` | `int` | `0` |
| `mercedes_rayado` | `boolean` | `true` |

---

# 5. Sintaxis general de las reglas

## 5.1. Declaraciones

### `<declaracion>`

```text
[<modificador>] <tipo_dato> <variable> = <valor> ;
```

### `<modificador>`

```text
BAJE_LA_VOZ_BEATRIZ
|
QUE_SE_ENTERE_TODA_ECOMODA
```

### `<tipo_dato>`

```text
SEIS_SEMESTRES
|
DEUDA_DE_PATRICIA
|
CHISME
```

### `<variable>`

```text
identificador_en_minusculas
```

### `<valor>`

```text
numero
|
numero_decimal
|
"texto"
|
TAN_DIVINO
|
PELITEÑIDA
|
MOSCORROFIO
```

---

## 5.2. Condiciones

### `<condicional>`

```text
SI_DON_ARMANDO_GRITA (<condicion>) AHORA_SI {
    <accion>
}
[PERDONEME_PERO_DISCULPEME {
    <accion>
}]
```

### `<condicion>`

**Forma 1 — Condición relacional**

```text
(<variable> <operador_relacional> <valor>)
```

**Forma 2 — Condición con operadores lógicos**

```text
(<condicion> <operador_logico> <condicion>)
```

**Forma 3 — Condición con negación**

```text
(NI_POR_EL_CHIRAS <condicion>)
```

### `<operador_relacional>`

```text
== | != | > | < | >= | <=
```

### `<operador_logico>`

```text
Y_ADEMAS_FLUIDEZ_MAMI
|
SI_NO_ES_ESTO_ES_AQUELLO
```

### `<accion>`

```text
FREDDY_ANUNCIA("texto");
|
AY_MARCE Excepcion("texto");
|
ENTREGUE_EL_BALANCE <valor>;
```

---

# 6. Descripción de palabras reservadas principales

### `SI_DON_ARMANDO_GRITA`

Es la palabra reservada que define el inicio de una estructura de control condicional. Evalúa si la expresión que le sigue es verdadera.

### `AHORA_SI`

Es el delimitador que indica el inicio del bloque de código que se ejecutará exclusivamente si la condición evaluada resulta verdadera.

### `Y_ADEMAS_FLUIDEZ_MAMI`

Funciona como operador lógico de conjunción **AND**. Se utiliza para evaluar múltiples condiciones simultáneamente y exige que todas sean verdaderas para que se cumpla la sentencia.

### `SI_NO_ES_ESTO_ES_AQUELLO`

Funciona como operador lógico de disyunción **OR**. Se utiliza para evaluar múltiples condiciones y requiere que al menos una de ellas sea verdadera para que se cumpla la sentencia.

---

# 7. Convención de escritura uniforme

Para garantizar que el código escrito en BettyScript sea legible y pueda ser procesado correctamente por el analizador léxico y sintáctico, todo programa debe cumplir con las siguientes convenciones.

## 7.1. Palabras reservadas en mayúsculas

Todas las palabras clave del lenguaje —tipos de datos, condicionales, modificadores de acceso, literales booleanos, valores nulos y funciones integradas— deben escribirse estrictamente en letras mayúsculas sostenidas.

Las palabras compuestas se separan mediante guion bajo (`_`).

**Ejemplos:**

```text
SI_DON_ARMANDO_GRITA
SEIS_SEMESTRES
TAN_DIVINO
BAJE_LA_VOZ_BEATRIZ
```

## 7.2. Variables en minúsculas con guion bajo

Los identificadores creados para nombrar variables deben escribirse completamente en minúsculas siguiendo la convención `snake_case`.

**Ejemplos:**

```text
rumor_confirmado
coleccion_actual
deuda_dolares
```

## 7.3. Operadores de comparación

Las comparaciones relacionales utilizan símbolos matemáticos universales de programación para mantener la claridad lógica.

Operadores permitidos:

| Operador | Significado |
|---|---|
| `==` | Igualdad |
| `!=` | Diferencia |
| `>` | Mayor que |
| `<` | Menor que |
| `>=` | Mayor o igual |
| `<=` | Menor o igual |

## 7.4. Formato consistente de las reglas

Se debe mantener una estructura sintáctica uniforme para delimitar correctamente bloques y sentencias:

- **Paréntesis `()`**: son obligatorios para agrupar condiciones lógicas y relacionales y para aislar las negaciones con `NI_POR_EL_CHIRAS`.
- **Llaves `{}`**: son obligatorias para delimitar los bloques de instrucciones correspondientes a `AHORA_SI` y `PERDONEME_PERO_DISCULPEME`.
- **Punto y coma `;`**: toda declaración de variables y toda instrucción de acción debe terminar con punto y coma.

