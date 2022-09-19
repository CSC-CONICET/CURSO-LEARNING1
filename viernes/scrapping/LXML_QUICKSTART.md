# Guia rápida de lxml

## Instalación

    pip install lxml

## Descarga de un documento utilizando urllib

Se modifica el user-agent, "disfrazándonos" de Mozilla para evitar bloqueo a bots.

    from lxml.html import parse
    import urllib.request
    
    #cambio de user agent
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)

    #descarga y parseo de la pagina.
    response = urllib.request.urlopen('http://example.com')
    doc = parse(response)

Para ejecutar queries de xpath sobre el documento o cualquier nodo, se utiliza el método `xpath()`.
Este método devolverá una lista de elementos que coincidan con la query. 

Puede acceder al texto de un elemento mediante la propiedad `text`.

Para "aplanar" el texto contenido en un subárbol que cuelga de un elemento puede utilizar el método `itertext()`.

Para eliminar nodos del arbol debe pedirle al elemento padre que remueva al nodo hijo.

    node_to_delete.getparent().remove(node_to_delete)

Puede acceder a los atributos de un elemento mediante el diccionario `attrib`.

    anchor_element.attrib['href']

Para acceder a los nodos hijos de un elemento se puede utilizar el método `getchildren()`

Para inspeccionar el contenido de un elemento puede usar la función tostring

    from lxml.etree import tostring
    tostring(elemento)