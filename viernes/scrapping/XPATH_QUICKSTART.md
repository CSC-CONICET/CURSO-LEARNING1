# Guía rápida de xpath

Se tomará como pagina de ejemplo [craigs-list](https://buenosaires.craigslist.org/).

Abra la consola de desarrollador de su navegador (F12)

Puede utilizar el modo inspector para localizar un nodo objetivo.
Por ejemplo el título en la equina superior izquierda de la página es un nodo `<h1>`

Para ejecutar consultas de xpath, puede utilizar la función de jQuery `$x()` en la consola de
desarrollador.

Tomemos por objetivo el título de la página en la esquina superior izquierda:
    
    <html>
        <head><...></head>
        <body>
            <...>
                <h1 id="logo">
                    <a href="https://www.craigslist.org/about/sites?lang=es&amp;cc=es">craigslist</a>
                    <sup><a href="//geo.craigslist.org/iso/ar">ar</a></sup>
                </h1>
            <...>
        </body>
    </html>

Para seleccionar el título de la página:

    $x("/html/body/div[1]/section/div[2]/h1")

La doble barra `//` en un path, machea todos los nodos que tengan como ancestro el tag anterior a la doble barra
Por ejemplo, las siguientes dos queries producirán el mismo resultado a la query anterior.

    $x("/html/body//h1")

    $x("//h1")

Como wildcard puede utilizar el asterisco `*` que matchea cualquier tag. Por ejemplo, para seleccionar todos los
hijos de h1
    
    $x("//h1/*")

Para matchear un atributo se puede colocar un `@` antes del nombre del atributo. Por ejemplo,
para recuperar la url a la que apunta un anchor

    $x("//h1/a/@href")

Los nodos de texto son nodos especiales a los que se accede mediante la función `text()`. Para
recuperar la palabra *craigslist* dentro del título:

    $x("//h1/a/text()")

A los elementos se les puede aplicar filtros mediante el operador `[]`. El caso típico es filtrar
por los atributos `class` o `id`. Por ejemplo para recuperar el atributo con el id *logo*.

    $x("//*[@id = 'logo']")

Notar que es necesario anidar 2 tipos de comillas, una para demarcar el string que es el argumento de
la función `$x()` y otro para delimitar el string `logo` que será procesado por el parser de xpath.
