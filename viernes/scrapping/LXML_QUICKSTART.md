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

Para "aplanar" el texto contenido en un elemento puede utilizaer el método `itertext()`.

Para eliminar nodos del arbol debe pedirle al elemento padre que remueva al nodo hijo.

    node_to_delete.getparent().remove(node_to_delete)