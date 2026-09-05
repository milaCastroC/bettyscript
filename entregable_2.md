# Lenguaje Formal

De acuerdo con la autora, un **lenguaje formal** es un lenguaje enteramente simbólico y artificial diseñado en oposición al lenguaje natural u ordinario. En rigor, se define como una cadena de signos construidos y vinculados de acuerdo con reglas estrictas, omitiendo cualquier tipo de interpretación o significado inicial que dichos signos pudieran recibir.

Su objetivo primordial es sustituir el discurso común, con frecuencia ambiguo y equívoco, por un sistema simbólico unívoco y claro que evite los errores de razonamiento e interpretación.

## Creación de un lenguaje formal

Antes de llegar a la construcción propiamente dicha, la autora señala dos condiciones que todo proceso de formalización presupone:

* **Constructividad:** los elementos que intervienen deben ser totalmente distinguibles entre sí y del resultado del proceso; se relaciona con lo enumerable (poder identificar cada signo y sustituirlo por otro según reglas), sin llegar a exigir totalizaciones infinitas.

* **Simbolización:** exige recurrir a símbolos distintos de los del lenguaje ordinario, con un nivel de abstracción suficiente para crear un simbolismo nuevo.

Citando a Martin (1968), el libro detalla los pasos para construir un sistema formal \(S\):

1. **Vocabulario o alfabeto (Σ):** definir un inventario completo de signos, organizados por categorías, donde cada signo pertenece a una sola categoría.

2. **Palabras (Γ):** combinar los signos del vocabulario en cadenas finitas (palabras), permitiendo la repetición de un mismo signo.

3. **Expresiones bien formadas (F):** una fórmula que está escrita correctamente según las reglas del sistema. No importa si tiene sentido o es cierta, solo que esté bien armada. Se define porque:

   * Hay piezas básicas que ya cuentan como válidas de entrada.
   * Hay reglas para combinar piezas válidas y formar otras más grandes.
   * Todo lo demás no cuenta.

4. **Tesis o teoremas (T):** una expresión bien formada que además se puede demostrar dentro del sistema. Se define porque:

   * Hay casos base que se aceptan como válidos sin necesidad de probarlos (**axiomas**).
   * Hay reglas para obtener nuevas tesis a partir de tesis ya probadas.
   * Todo lo demás no cuenta como demostrado.

## Cómo se compone (estructura interna)

Un sistema formal así construido queda compuesto por:

* Vocabulario.
* Expresiones bien formadas (**F**) iniciales.
* Reglas de formación.
* Axiomas.
* Teoremas.
* Reglas de deducción o transformación.

El libro ilustra esto con un sistema para la **lógica proposicional**, compuesto por variables, conectores como `⌐`, `V`, `⊃` y `∧`, signos de puntuación, reglas de sustitución y *modus ponens*.

Dentro del sistema pueden distinguirse dos ejes principales:

* **Eje sintáctico** —de naturaleza proposicional y analítica—: establece cómo se descompone el lenguaje en proposiciones elementales y compuestas.

* **Eje semántico** —de naturaleza representacional—: establece cómo esas proposiciones se relacionan con hechos extralingüísticos.

Además, a un sistema formal se le exigen cuatro características:

1. **Ser explícito:** sus reglas y componentes deben estar claramente establecidos.
2. **Ser unívoco:** a cada nombre debe corresponder un objeto.
3. **Tener funcionalidad:** a cada signo debe corresponder una función determinada.
4. **Mantener una distinción de niveles lógicos:** debe separar:

   * El **lenguaje-objeto**, con el que se construyen las expresiones.
   * El **metalenguaje**, es decir, el lenguaje —por ejemplo, el español— utilizado para hablar sobre esas expresiones y estudiar su sintaxis y su semántica.

## Fuente

Pradilla Rueda, M. (2017). *Lenguajes formales y lenguajes computacionales*. Fondo de Publicaciones Corporación Universitaria Republicana.

https://urepublicana.edu.co/images/libros_pdf/978-958-5447-09-7.pdf
