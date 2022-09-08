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
tras aplicar cada patch ejecute los testeos de unidad para verificar que el patch fue aplicado correctamente.
*No aplique el patch de Víctor todavía*.

       patch laura/kyu7.py [nombre].patch
       python3 laura/tests.py

4) Por último aplique el patch de Víctor y vuelva a correr las validaciones. 
¿Se aplica exitosamente? ¿Cómo interpreta la salida? ¿Qué significan los errores?
¿La Validación fue exitosa?

5) Revierta el patch de Víctor y vuelva a correr las validaciones para verificar que
se revirtió correctamente.

       patch -R laura/kyu7.py victor.patch

6) Aplique el patch de Víctor nuevamente esta vez con el flag de mergeo.

       patch --merge=merge laura/kyu7.py victor.patch

7) Vuelva a ejecutar la validación. ¿Por qué falla? Puede ayudarse a
interpretar la salida leyendo la documentación del flag `--merge` en el manual de
patch `man patch`

8) Edite el archivo `kyu7.py` de Laura para resolver los conflictos en favor
de los cambios de Víctor. Asegúrese que todas las validaciones sean exitosas.
