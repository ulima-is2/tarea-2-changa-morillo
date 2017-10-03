# Tarea 2

### Integrantes
| Nombres                          | Código   | Usuario         |
| -------------------------------- | -------- | --------------- |
| Christian Manuel Changa Castillo | 20143344 | christianempire |
| Bruna Morillo Palacios           | 20142059 | BrunaMP         |

### Respuestas

#### Pregunta 1
Uno de los principios que no se utilizó es el de Open/Closed, pues el código no es del todo abierto como para que pueda haber herencia. La existencia de dos clases muy similares entre si (CinePlaneta y CineStark) en lugar de una padre que pueda instanciarse y/o heredarse hace que este principio no se cumpla.

Otro de los principios que no se utilizó es el de Liskov substitution. Ya que existen dos clases similares: CinePlaneta y CineStark. Que poseen métodos similares, cuando podrían tener una misma clase base que posea esos métodos para que no halla la necesidad de reimplementarlos.

Finalmente el último método cuya implementación falló es el de Interface segregation. Ya que los métodos que se repiten en ambas clases (CinePlaneta y CineStark) podrían incluirse en una interfaz y utilizar dicha interfaz en las clases en lugar de definir los métodos en cada una de ellas.

#### Pregunta 2
La resolución de la pregunta 2 se encuentra en el archivo patrones-resuelto.py. La sustentación de la aplicación de cada uno de los tres patrones se encuentra en los comentarios.

#### Pregunta 3
La resolución de la pregunta 3 se encuentra en el archivo patrones-sql.py.