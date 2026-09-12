# Sintaxis BettyScript Actualizada

---

## 1. Bloques

### `<instrucciones>`

```text
<instrucciones> ::= <sentencia> | <sentencia> <instrucciones>
```

### `<sentencia>`

```text
<sentencia> ::= <declaracion> | <asignacion> | <condicional> | <impresion> | <manejo_error> | <lanzar_error>
```

### `<bloque>`

```text
<bloque> ::= { <instrucciones> }
```

---

## 2. Declaración y asignación

### `<declaracion>`

```text
<declaracion> ::= <tipo_dato> <identificador> = <expresion> ;
```

### `<asignacion>`

```text
<asignacion> ::= <identificador> = <expresion> ;
```

---

## 3. Tipos, literales y valores

### `<tipo_dato>`

```text
<tipo_dato> ::= SEIS_SEMESTRES | DEUDA_DE_PATRICIA | CHISME
```

### `<valor>`

```text
<valor> ::= <identificador> | <literal>
```

### `<literal>`

```text
<literal> ::= <literal_numerico> | <cadena> | <booleano> | <nulo>
```

### `<literal_numerico>`

```text
<literal_numerico> ::= <numero_entero> | <numero_decimal>
```

### `<valor_numerico>`

```text
<valor_numerico> ::= <identificador> | <literal_numerico>
```

### `<booleano>`

```text
<booleano> ::= TAN_DIVINO | PELITEÑIDA
```

### `<nulo>`

```text
<nulo> ::= MOSCORROFIO
```

### `<identificador>`

```text
<identificador> ::= <letra> | <letra> <resto_identificador>
```

### `<resto_identificador>`

```text
<resto_identificador> ::= <caracter_identificador> | <caracter_identificador> <resto_identificador>
```

### `<caracter_identificador>`

```text
<caracter_identificador> ::= <letra> | <digito> | “_”
```

### `<letra>`

```text
<letra> ::= a | b | ... | z | A | B | ... | Z
```

### `<digito>`

```text
<digito> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
```

### `<alfanumerico>`

```text
<alfanumerico> := <letra> | <digito> | <caracter_especial>
```

### `<caracter_especial>`

```text
<caracter_especial> := ! | @ | # | $ | % | ^ | & | * | ( | ) | - | _ | + | = | [ | ] | { | } | < | > | / | \\ | : | ; | , | . | ? | ~ | ` | ¡ | ¿
```

### `<numero_entero>`

```text
<numero_entero> ::= <digito> | <digito> <numero_entero>
```

### `<numero_decimal>`

```text
<numero_decimal> ::= <numero_entero> . <numero_entero>
```

### `<cadena>`

```text
<cadena> ::= <alfanumerico> | <alfanumerico> <cadena>
```

---

## 4. Expresiones aritméticas

### `<expresion_aritmetica>`

```text
<expresion_aritmetica> ::= <operacion> | <valor_numerico> | (<operacion>)
```

### `<operacion>`

```text
<operacion> ::= <expresion_aritmetica> <operador> <expresion_aritmetica>
```

### `<operador>`

```text
<operador> ::= + | - | * | / | %
```

---

## 5. Expresiones lógicas

### `<expresion>`

```text
<expresion> ::= <expresion_aritmetica> | <valor>
```

### `<condicion>`

```text
<condicion> ::= <expresion_logica> | NI_POR_EL_CHIRAS <condicion_simple> | ( <expresion_logica> )
```

### `<expresion_logica>`

```text
<expresion_logica> ::= <condicion_simple> | <expresion_logica> <operador_logico> <condicion_simple>
                    | <expresion_logica> <operador_logico> ( <expresion_logica> )
```

### `<condicion_simple>`

```text
<condicion_simple> ::= <comparacion> | <identificador>
```

### `<comparacion>`

```text
<comparacion> ::= <expresion> <operador_relacional> <expresion>
```

### `<operador_relacional>`

```text
<operador_relacional> ::= == | > | < | >= | <=
```

### `<operador_logico>`

```text
<operador_logico> ::= Y_ADEMAS_FLUIDEZ_MAMI | SI_NO_ES_ESTO_ES_AQUELLO
```

---

## 6. Condicionales

### `<condicional>`

```text
<condicional> ::= "SI_DON_ARMANDO_GRITA ( <condicion> ) AHORA_SI <bloque>
               | SI_DON_ARMANDO_GRITA ( <condicion> ) AHORA_SI <bloque> PERDONEME_PERO_DISCULPEME <bloque>
```

---

## 7. Impresion

### `<impresion>`

```text
<impresion> ::= FREDDY_ANUNCIA ( <expresion> ) ;
```

---

## 8. Lanzamiento y manejo de errores

### `<lanzar_error>`

```text
<lanzar_error> ::= AY_MARCE <identificador> ( <cadena> ) ;
```

### `<manejo_error>`

```text
<manejo_error> ::= MAQUILLAR_BALANCE <bloque> EL_DIABLO_ES_PUERCO ( <identificador> ) <bloque>
```
