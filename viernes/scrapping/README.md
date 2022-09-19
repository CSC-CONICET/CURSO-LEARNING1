# Scrapping

## Introducción

Uno de los desafíos en el mundo de la ciencia de datos es la obtención y el curado de los datos previo al procesamiento.
Muchas veces hay datos disponibles en Internet, pero presentados en un formato orientado al consumo humano. En estos
casos el Web-Scrapping es una técnica útil para tomar esos datos y convertirlos es un formato estructurado apto para
aplicar técnicas de learning.

Web scraping es la extracción de información de sitios web mediante programas de software conocidos como robots. 
Usualmente, estos programas simulan la navegación de un humano en la World Wide Web.

## Actividad

El objetivo será construir un dataset etiquetado de *[Web Novels](https://en.wikipedia.org/wiki/Web_fiction)*

El datataset a construir consistirá de los siguientes campos:

* Url de la novela
* Título
* Autor
* Géneros
* Sinopsis
* Texto de la novela.


Los datos serán scrappeandos de la página [readwn](https://www.readwn.com).

## Indicaciones para el armado del dataset 

1) La url de las novelas será obtenida desde el [índice por popularidad](https://www.readwn.com/list/all/all-onclick-0.html).
Deberá descargar al menos las 500 novelas más populares.

2) Desde la página principal de la novela podrá completar los campos título, autor, géneros, sinopsis
Además podrá acceder al índice de capítulos.

3) Por cada novela deberá descargar los primeros 10 capítulos.

4) El texto del capítulo deberá ser en forma de texto plano.

## Aplicación

Una vez armado el dataset, debera construir un clasificador multicategórico que permita predecir los géneros a
los que pertenece un texto.

## Consideraciones.

Sea amable con la página para que la ip no sea bloqueada por abuso. Deberá acceder a aproximadamente 5000 urls. Accediendo
de a 1 por segundo podrá completar el dataset en aproximadamente una hora y media.

Es probable que la conexión se interrumpa. Considere un esquema en que pueda soportar interrupciones, por ejemplo, descargando
el índice de urls para poder continuar desde la última novela que se estaba descargando antes de la interrupción.

## Detalles técnicos.

Si ya posee un método de scrapping de su preferencia puede utilizarlo. Para la actividad se sugiere el uso de 
[xpath](https://www.w3schools.com/xml/xpath_intro.asp) y el módulo [lxml](https://lxml.de/) de python.

Las siguientes guías rápidas tienen el contenido mínimo necesario para resolver el tp:

* [GUÍA RÁPIDA DE XPATH](XPATH_QUICKSTART.md)
* [GUÍA RÁPIDA DE LXML](LXML_QUICKSTART.md)