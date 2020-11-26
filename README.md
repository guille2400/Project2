# Project 2 - Twitter Search - DataBase2

In this project we will build a secondary memory index for tweets, and build a search engine for term search, for similar tweets retrieval.


## Procesamiento de los tweets y TFIDF Score

Primero se procesa cada Tweet independientemente para lograr convertir a token las stop words y eliminarlas. También debemos deshacernos de tildes y emojis para que sea posible generar el documento de frecuencias.


Para el TFIDF, el IDF(frecuencia de documento inverso) para documentos junto con su TF(Term Frequency). Esto se hace a lo largo de la división de trozos y se concatenan con cada uno de ellos. Luego, con los datos maestros, podemos realizar consultas. Cuando se pasa una consulta, se interpreta como un documento y se calcula el TF-IDF correspondiente para cada palabra. Luego encontramos los documentos para los cuales estas palabras no son 0. Eso significa que habrá una comparación mayor que 0, y calculamos el TF_IDF de los vectores de datos. Finalmente calculamos la similitud de coseno para el vector en la consulta y el vector en cada uno de los documentos a evaluar y los ordenamos.

## Front end

Usamos Django Web Framework para construir una aplicación web para usarlo como motor de búsqueda.


## Manejo de memoria Secundaria

Se nos da un directorio lleno de archivos .json donde cada archivo corresponde a una cantidad de tweets con sus respectivos datos. Para facilitar la implementación, fusionamos todos esos archivos en un solo "tweets.csv" con la función jsonToCsv () donde estaremos leyendo toda la información de ahora en adelante.

Como no podemos leer todos los tweets a la vez debido a restricciones de memoria, estaremos leyendo en fragmentos de tamaño 1000 y ejecutando la función generateTffd() para cada fragmento y escribiendo el marco de datos resultante (ordenado por palabra) en el disco.

Ahora que tenemos todas las tablas escritas en el disco, necesitamos fusionar dichas tablas en una sola para que tengamos toda la información en un solo archivo. Surge el mismo problema que antes, no podemos leer todos los fragmentos en la memoria para fusionarlos y convertirlos en uno, así que lo que hacemos aquí es leer las primeras n entradas de cada fragmento en el disco, fusionarlas y escribirlas en el " merged.csv "archivo. Cuando ejecute esa función hasta que hayamos leído todas las líneas en los fragmentos escritos. El resultado es un archivo ordenado donde se han fusionado todas las tablas.

