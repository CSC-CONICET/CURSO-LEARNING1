# Diff & Patch

En la clase de programación se asignan 4 desafíos a resolver en grupos de 5
Alicia, Berto, Carlos y Víctor se reparten cada uno de los 4 desafios en el archivo
`kyu7.py` y lo resuelven, cada quien en su propia carpeta.

Usted jugará el rol de Laura, la 5ta integrante que se encarga 
de juntar y coordinar y validar las soluciones de sus compañeros.

Laura valida las soluciones ejecutando el script `tests.py`

1) Utilizando el comando `diff` compare el archivo `kyu7.py` sin resolver en la carpeta Laura,
respecto a los de Alicia, Berto, Carlos y Víctor.

       diff laura/kyu7.py [nombre]/kyu7.py7
   
2) Genere un archivo de patch por cada una de las soluciones respecto el archivo sin resolver que tiene Laura.
Si quiere, inspeccione el contenido del archivo.

       diff -u laura/kyu7.py [nombre]/kyu7.py7 > [nombre].patch

3) Aplique los patches con las soluciones de Alicia, Berto, Carlos, 
tras aplicar cada patch ejecute los testeos de unidad para verificar que el patch fue aplicado correctamente:

       patch laura/kyu7.py [nombre].patch
       python3 laura/tests.py

4) Por ultimo aplique el patch de Víctor. Por qué falló?

