# Proceso de Construcción de BettyScript y su Fundamentación Teórica

El lenguaje formal que estamos construyendo recibe el nombre de **“BettyScript”**, cuya sintaxis, tipos de datos y estructuras corresponden a referencias y frases célebres a la telenovela colombiana *“Yo soy Betty, la fea”*. Con este lenguaje buscamos establecer un sistema de signos y reglas donde cada expresión tenga un significado único y verificable, creando un sistema simbólico unívoco y claro que evite los errores de razonamiento e interpretación (Pradilla, 2017, cap. II, "Formalización", pp. 48).
A partir de cada frase o situación icónica de la novela buscamos traducirlas a una construcción fija del lenguaje de modo que su significado deje de depender del lenguaje natural y pase a depender únicamente de las reglas del sistema.

---

# 1. Reglas de lenguajes formales

Inicialmente tomamos 15 reglas redactadas en lenguaje natural (por ejemplo, "Si `rumor_confirmado` es verdadero, se imprime 'Atención Ecomoda, último minuto'") y las escribimos directamente en su forma simbólica dentro de BettyScript (`SI_DON_ARMANDO_GRITA (...) AHORA_SI {...}`).

Cada una de estas reglas ya escritas en símbolos constituye, una **expresión bien formada (F)**. Es decir, una cadena de signos del vocabulario del lenguaje que sigue una gramática (Pradilla, 2017, cap. II, sec. 3.A, "Construcción de un sistema formal", pp. 43-44). Aunque en este paso todavía no hayamos formulado esa gramática de manera explícita y general . Este paso también se enmarca en el proceso general de formalización que describe el libro al sustituir enunciados de un discurso ambiguo e impreciso por un lenguaje simbólico donde cada configuración de signos tiene un significado unívoco.

---

# 2. Sintaxis de las reglas (Condiciones que se deben establecer)

Para la sintaxis de las reglas definimos la estructura general que debe cumplir toda declaración y todo condicional (`<declaracion>`, `<condicional>`, `<condicion>`), junto con una convención de escritura definida (mayúsculas para palabras reservadas, `snake_case` para variables, uso obligatorio de paréntesis, llaves y punto y coma).

En este paso formulamos las reglas de formación que definen en general qué es una **F** dentro de BettyScript. El libro exige tres condiciones para esto: cuáles son las expresiones iniciales que ya cuentan como válidas, cómo se combinan expresiones válidas para formar otras nuevas, y una condición de cierre que descarta todo lo que no provenga de las dos anteriores (Pradilla, 2017, cap. II, sec. 3.A, "Construcción de un sistema formal", pp. 43-44). En nuestra sintaxis, una variable o un valor solos son expresiones iniciales válidas, las condiciones se combinan mediante los operadores lógicos del lenguaje, y cualquier combinación fuera de esas reglas queda descartada como error de sintaxis.

---

# 3. Lexer

En el siguiente paso elaboramos una tabla de clasificación que agrupa cada signo del lenguaje por categoría (tipos de dato, operadores relacionales y lógicos, condicionales, modificadores de acceso, entre otros), estableciendo además su equivalencia con las construcciones correspondientes de **Java**, que es el lenguaje en el que implementaremos el lexer.

El libro nombra explícitamente el **"análisis lexical"** como la primera fase de la compilación: separar la cadena de entrada en subcadenas según categorías sintácticas ya definidas, sin interpretar aún su significado (Pradilla, 2017, cap. V, “Lenguajes de computación y lenguajes formales”, sec. 4, nota 14, pp. 142-143). Eso es justo lo que hace un lexer, y opera sobre el vocabulario o alfabeto (**Σ**) que el libro exige definir primero al construir un sistema formal. En nuestro caso, la tabla de palabras reservadas, literales y operadores de BettyScript.

---

# 4. Palabras reservadas

Finalmente, en las palabras reservadas fijamos una lista cerrada de palabras clave (`SI_DON_ARMANDO_GRITA`, `FREDDY_ANUNCIA`, `CHISME`, `TAN_DIVINO`, etc.), cada una asociada a un único significado técnico equivalente a una construcción de Java (`if`, `print()`, `String`, `true`).

Este paso corresponde a dos de las características que el libro exige a todo lenguaje formal, presentadas en la sección **"Características del lenguaje formal"** (Pradilla, 2017,Cap. II, “Características del lenguaje formal”, p. 58): que sea **unívoco** (a cada nombre le corresponde un solo objeto o significado) y que tenga **funcionalidad** (a cada signo le corresponde una función). También se apoya en la explicación sobre la designación de signos en el metalenguaje, donde se indica que a cada símbolo corresponde un nombre y a cada nombre un solo símbolo (Pradilla, 2017, cap. ll, “Características del lenguaje formal” pp. 60-61) . Esto es lo que nos garantiza que, por ejemplo, `TAN_DIVINO` siempre representa el valor booleano verdadero y nunca otra cosa.

---

**Fuente:** Pradilla Rueda, M. (2017). *Lenguajes formales y lenguajes computacionales*. Fondo de Publicaciones Corporación Universitaria Republicana. https://urepublicana.edu.co/images/libros_pdf/978-958-5447-09-7.pdf
