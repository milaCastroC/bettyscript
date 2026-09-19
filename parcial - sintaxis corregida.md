# BettyScript

## Gramática BNF

- **01** · [Declaración](#declaracion)
- **02** · [Asignación](#asignacion)
- **03** · [Tipos de datos](#tipos-de-datos)
- **04** · [Literales](#literales)
- **05** · [Condicionales](#condicionales)
- **06** · [Impresión](#impresion)
- **07** · [Sintaxis completa](#sintaxis-completa)

---

<a id="declaracion"></a>

## 01 · Declaración

```bnf
<declaracion> ::= <tipo_dato> <identificador> = <expresion> ;
```

### Reglas derivadas

```bnf
<tipo_dato> ::= SEIS_SEMESTRES | DEUDA_DE_PATRICIA | CHISME

<identificador> ::= <letra> | <letra> <resto_identificador>

<letra> ::= a | b | ... | z | A | B | ... | Z

<resto_identificador> ::= <caracter_identificador> | <caracter_identificador> <resto_identificador>

<caracter_identificador> ::= <letra> | <digito> | “_”

<digito> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

<expresion> ::= <expresion_aritmetica> | <expresion_cadena> | <expresion_booleana>

<expresion_aritmetica> ::= <operacion> | <valor_numerico> | (<operacion>)

<operacion> ::= <expresion_aritmetica> <operador> <expresion_aritmetica>

<operador> ::= + | - | * | / | %

<valor_numerico> ::= <literal_numerico> | <identificador>

<literal_numerico> ::= <numero_entero> | <numero_decimal>

<numero_entero> ::= <digito> | <digito> <numero_entero>

<numero_decimal> ::= <numero_entero> . <numero_entero>

<expresion_booleana> ::=  <valor_booleano> | (<comparacion>)

<valor_booleano> ::= <booleano> | <identificador>

<booleano> ::= TAN_DIVINO | PELITEÑIDA

<comparacion> ::= <expresion_aritmetica> <operador_relacional> <expresion_aritmetica> | 
<expresion_booleana> <operador_igualdad> <expresion_booleana> | 
<cadena> <operador_igualdad> <cadena>

<operador_relacional> ::= <operador_igualdad> | > | < | >= | <=

<operador_igualdad> ::= ==  | !=

<cadena> ::= <alfanumerico> | <alfanumerico> <cadena>

<alfanumerico> := <letra> | <digito> | <caracter_especial>

<caracter_especial> := ! | @ | # | $ | % | ^ | & | * | ( | ) | - | _ | + | = | [ | ] | { | } | < | > | / | \ | : | ;  | , | . | ? | ~ | ` | ¡ | ¿ |
```

---

<a id="asignacion"></a>

## 02 · Asignación

```bnf
<asignacion> ::= <identificador> = <expresion> ;
```

### Reglas derivadas

```bnf
<identificador> ::= <letra> | <letra> <resto_identificador>

<letra> ::= a | b | ... | z | A | B | ... | Z

<resto_identificador> ::= <caracter_identificador> | <caracter_identificador> <resto_identificador>

<caracter_identificador> ::= <letra> | <digito> | “_”

<digito> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

<expresion> ::= <expresion_aritmetica> | <expresion_cadena> | <expresion_booleana>

<expresion_aritmetica> ::= <operacion> | <valor_numerico> | (<operacion>)

<operacion> ::= <expresion_aritmetica> <operador> <expresion_aritmetica>

<operador> ::= + | - | * | / | %

<valor_numerico> ::= <literal_numerico> | <identificador>

<literal_numerico> ::= <numero_entero> | <numero_decimal>

<numero_entero> ::= <digito> | <digito> <numero_entero>

<numero_decimal> ::= <numero_entero> . <numero_entero>

<expresion_booleana> ::=  <valor_booleano> | (<comparacion>)

<valor_booleano> ::= <booleano> | <identificador>

<booleano> ::= TAN_DIVINO | PELITEÑIDA

<comparacion> ::= <expresion_aritmetica> <operador_relacional> <expresion_aritmetica> | 
<expresion_booleana> <operador_igualdad> <expresion_booleana> | 
<cadena> <operador_igualdad> <cadena>

<operador_relacional> ::= <operador_igualdad> | > | < | >= | <=

<operador_igualdad> ::= ==  | !=

<cadena> ::= <alfanumerico> | <alfanumerico> <cadena>

<alfanumerico> := <letra> | <digito> | <caracter_especial>

<caracter_especial> := ! | @ | # | $ | % | ^ | & | * | ( | ) | - | _ | + | = | [ | ] | { | } | < | > | / | \ | : | ;  | , | . | ? | ~ | ` | ¡ | ¿ |
```

---

<a id="tipos-de-datos"></a>

## 03 · Tipos de datos

```bnf
<tipo_dato> ::= SEIS_SEMESTRES | DEUDA_DE_PATRICIA | CHISME
```

<a id="literales"></a>
## 04 . Literal

```bnf
<literal> ::= <literal_numerico> | <valor_booleano> | <valor_cadena> | <nulo>
```

### Reglas derivadas

```bnf
<literal_numerico> ::= <numero_entero> | <numero_decimal>

<numero_entero> ::= <digito> | <digito> <numero_entero>

<digito> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

<numero_decimal> ::= <numero_entero> . <numero_entero>

<valor_booleano> ::= <booleano> | <identificador>

<booleano> ::= TAN_DIVINO | PELITEÑIDA

<identificador> ::= <letra> | <letra> <resto_identificador>

<letra> ::= a | b | ... | z | A | B | ... | Z

<resto_identificador> ::= <caracter_identificador> | <caracter_identificador> <resto_identificador>

<caracter_identificador> ::= <letra> | <digito> | “_”

<valor_cadena> ::= <cadena> | <identificador>

<cadena> ::= <alfanumerico> | <alfanumerico> <cadena>

<alfanumerico> := <letra> | <digito> | <caracter_especial>

<caracter_especial> := ! | @ | # | $ | % | ^ | & | * | ( | ) | - | _ | + | = | [ | ] | { | } | < | > | / | \ | : | ;  | , | . | ? | ~ | ` | ¡ | ¿ |

<nulo> ::= MOSCORROFIO
```

---

<a id="condicionales"></a>

## 05 · Condicionales

```bnf
<condicional> ::= "SI_DON_ARMANDO_GRITA ( <condicion> ) AHORA_SI <bloque>
   | SI_DON_ARMANDO_GRITA ( <condicion> ) AHORA_SI <bloque> PERDONEME_PERO_DISCULPEME <bloque>
```

### Reglas relacionadas

```bnf
<condicion> ::= <expresion_logica> | NI_POR_EL_CHIRAS <condicion_simple> | ( <expresion_logica> )

<expresion_logica> ::= <condicion_simple> | <expresion_logica> <operador_logico> <condicion_simple>
                  	| <expresion_logica> <operador_logico> ( <expresion_logica> )

<condicion_simple> ::= <comparacion> | <expresion_booleana>

<comparacion> ::= <expresion_aritmetica> <operador_relacional> <expresion_aritmetica> | 
                <expresion_booleana> <operador_igualdad> <expresion_booleana> | 
                <cadena> <operador_igualdad> <cadena>

<expresion_aritmetica> ::= <operacion> | <valor_numerico> | (<operacion>)

<operacion> ::= <expresion_aritmetica> <operador> <expresion_aritmetica>

<operador> ::= + | - | * | / | %

<valor_numerico> ::= <literal_numerico> | <identificador>

<literal_numerico> ::= <numero_entero> | <numero_decimal>

<numero_entero> ::= <digito> | <digito> <numero_entero>

<digito> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

<numero_decimal> ::= <numero_entero> . <numero_entero>

<identificador> ::= <letra> | <letra> <resto_identificador>

<letra> ::= a | b | ... | z | A | B | ... | Z

<resto_identificador> ::= <caracter_identificador> | <caracter_identificador> <resto_identificador>

<caracter_identificador> ::= <letra> | <digito> | “_”

<operador_relacional> ::= <operador_igualdad> | > | < | >= | <=

<operador_igualdad> ::= ==  | !=

<expresion_booleana> ::=  <valor_booleano> | (<comparacion>)

<valor_booleano> ::= <booleano> | <identificador>

<booleano> ::= TAN_DIVINO | PELITEÑIDA

<cadena> ::= <alfanumerico> | <alfanumerico> <cadena>

<alfanumerico> := <letra> | <digito> | <caracter_especial>

<caracter_especial> := ! | @ | # | $ | % | ^ | & | * | ( | ) | - | _ | + | = | [ | ] | { | } | < | > | / | \ | : | ;  | , | . | ? | ~ | ` | ¡ | ¿ |

<operador_logico> ::= Y_ADEMAS_FLUIDEZ_MAMI | SI_NO_ES_ESTO_ES_AQUELLO

<bloque> ::= { <instrucciones> }

<instrucciones> ::= <sentencia> | <sentencia> <instrucciones>

<sentencia> ::= <declaracion> | <asignacion> | <condicional> | <impresion> | <manejo_error> | <lanzar_error>

<declaracion> ::= <tipo_dato> <identificador> = <expresion> ;

<tipo_dato> ::= SEIS_SEMESTRES | DEUDA_DE_PATRICIA | CHISME

<expresion> ::= <expresion_aritmetica> | <expresion_cadena> | <expresion_booleana>

<asignacion> ::= <identificador> = <expresion> ;

<impresion> ::= FREDDY_ANUNCIA ( <expresion> );

<manejo_error> ::= MAQUILLAR_BALANCE <bloque> EL_DIABLO_ES_PUERCO ( <identificador> ) <bloque>

<lanzar_error> ::= AY_MARCE <identificador> ( <cadena> ) ;
```

---

<a id="impresion"></a>

## 06 · Impresión

```bnf
<impresion> ::= FREDDY_ANUNCIA ( <expresion> );
```

### Reglas derivadas

```bnf
<expresion> ::= <expresion_aritmetica> | <expresion_cadena> | <expresion_booleana>

<expresion_aritmetica> ::= <operacion> | <valor_numerico> | (<operacion>)

<operacion> ::= <expresion_aritmetica> <operador> <expresion_aritmetica>

<operador> ::= + | - | * | / | %

<valor_numerico> ::= <literal_numerico> | <identificador>

<literal_numerico> ::= <numero_entero> | <numero_decimal>

<numero_entero> ::= <digito> | <digito> <numero_entero>

<digito> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

<numero_decimal> ::= <numero_entero> . <numero_entero>

<identificador> ::= <letra> | <letra> <resto_identificador>

<letra> ::= a | b | ... | z | A | B | ... | Z

<resto_identificador> ::= <caracter_identificador> | <caracter_identificador> <resto_identificador>

<caracter_identificador> ::= <letra> | <digito> | “_”

<expresion_booleana> ::=  <valor_booleano> | (<comparacion>)

<valor_booleano> ::= <booleano> | <identificador>

<booleano> ::= TAN_DIVINO | PELITEÑIDA

<comparacion> ::= <expresion_aritmetica> <operador_relacional> <expresion_aritmetica> | 
<expresion_booleana> <operador_igualdad> <expresion_booleana> | 
<cadena> <operador_igualdad> <cadena>

<operador_relacional> ::= <operador_igualdad> | > | < | >= | <=

<operador_igualdad> ::= ==  | !=

<cadena> ::= <alfanumerico> | <alfanumerico> <cadena>

<alfanumerico> := <letra> | <digito> | <caracter_especial>

<caracter_especial> := ! | @ | # | $ | % | ^ | & | * | ( | ) | - | _ | + | = | [ | ] | { | } | < | > | / | \ | : | ;  | , | . | ? | ~ | ` | ¡ | ¿ |
```

---

<a id="sintaxis-completa"></a>

## 07 · Sintaxis completa

# Sintaxis BettyScript Completa

### Bloques

**\<instrucciones>** ::= \<sentencia> | \<sentencia> \<instrucciones>

**\<sentencia>** ::= \<declaracion> | \<asignacion> | \<condicional> | \<impresion> | \<manejo\_error> | \<lanzar\_error>

**\<bloque>** ::= { \<instrucciones> }

### Declaración y asignación

**\<declaracion>** ::= \<tipo\_dato> \<identificador> **=** \<expresion> ;
**\<asignacion>** ::= \<identificador> = \<expresion> ;

### Tipos, literales y valores

**\<tipo\_dato>** ::= SEIS\_SEMESTRES | DEUDA\_DE\_PATRICIA | CHISME

**\<valor>** ::= \<identificador> | \<literal>

**\<literal>** ::= \<literal\_numerico> | \<valor\_booleano> | \<valor\_cadena> | \<nulo>

**\<literal\_numerico> ::=** \<numero\_entero> | \<numero\_decimal>

**\<valor\_numerico> ::=** \<literal\_numerico> | \<identificador>

**\<valor\_booleano> ::=** \<booleano> | \<identificador>

**\<valor\_cadena> ::=** \<cadena> | \<identificador>

**\<booleano>** ::= TAN\_DIVINO | PELITEÑIDA

**\<nulo>** ::= MOSCORROFIO

**\<identificador>** ::= \<letra> | \<letra> \<resto\_identificador>

**\<resto\_identificador>** ::= \<caracter\_identificador> | \<caracter\_identificador> \<resto\_identificador>

**\<caracter\_identificador>** ::= \<letra> | \<digito> | “\_”

**\<letra>** ::= a | b | ... | z | A | B | ... | Z

**\<digito>** ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

**\<alfanumerico>** := \<letra> | \<digito> | \<caracter\_especial>

**\<caracter\_especial>** := ! | @ | # | $ | % | ^ | & | \* | ( | ) | - | \_ | + | = | [ | ] | { | } | < | > | / | \ | : | ;  | , | . | ? | \~ | \` | ¡ | ¿ | 

**\<numero\_entero>** ::= \<digito> | \<digito> \<numero\_entero>

**\<numero\_decimal>** ::= \<numero\_entero> **.** \<numero\_entero>

**\<cadena>** ::= \<alfanumerico> | \<alfanumerico> \<cadena>

### Expresiones

**\<expresion>** ::= \<expresion\_aritmetica> | \<expresion\_cadena> | \<expresion\_booleana>

**\<expresion\_aritmetica>** ::= \<operacion> | \<valor\_numerico> | (\<operacion>)

**\<expresion\_booleana>** ::=  \<valor\_booleano> | (\<comparacion>)

### Operaciones aritméticas

### \<operacion> ::= \<expresion\_aritmetica> \<operador> \<expresion\_aritmetica>

### \<operador> ::= + | - | \* | / | %

### Expresiones lógicas

**\<condicion>** ::= \<expresion\_logica> | NI\_POR\_EL\_CHIRAS \<condicion\_simple> | ( \<expresion\_logica> )

**\<expresion\_logica>** ::= \<condicion\_simple> | \<expresion\_logica> \<operador\_logico> \<condicion\_simple>
                  	| \<expresion\_logica> \<operador\_logico> ( \<expresion\_logica> )

**\<condicion\_simple>** ::= \<comparacion> | \<expresion\_booleana>

**\<comparacion>** ::= \<expresion\_aritmetica> \<operador\_relacional> \<expresion\_aritmetica> | 
\<expresion\_booleana> \<operador\_igualdad> \<expresion\_booleana> | 
\<cadena> \<operador\_igualdad> \<cadena>

**\<operador\_relacional>** ::= \<operador\_igualdad> | > | < | >= | <=

**\<operador\_igualdad>** ::= ==  | !=

**\<operador\_logico>** ::= Y\_ADEMAS\_FLUIDEZ\_MAMI | SI\_NO\_ES\_ESTO\_ES\_AQUELLO

### Condicionales

**\<condicional>** ::= "SI\_DON\_ARMANDO\_GRITA ( \<condicion> ) AHORA\_SI \<bloque>
 | SI\_DON\_ARMANDO\_GRITA ( \<condicion> ) AHORA\_SI \<bloque> PERDONEME\_PERO\_DISCULPEME \<bloque>

### Impresion

**\<impresion>** ::= FREDDY\_ANUNCIA ( \<expresion> );

### Lanzamiento y manejo de errores

**\<lanzar\_error>** ::= AY\_MARCE \<identificador> ( \<cadena> ) ;

**\<manejo\_error>** ::= MAQUILLAR\_BALANCE \<bloque> EL\_DIABLO\_ES\_PUERCO ( \<identificador> ) \<bloque>
