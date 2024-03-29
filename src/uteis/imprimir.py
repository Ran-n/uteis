#! /usr/bin/python3
# -*- coding: utf-8 -*-
# --------------------------------------------
#+ Autor:	Ran#
#+ Creado:	05/07/2021 17:47:50
#+ Editado:	2022/01/26 19:52:15.129610
# --------------------------------------------
import json
# --------------------------------------------
# forma bonita de imprimir diccionarios de python
def jprint(diccionario, indent=4, sort=False):
    """
    Dado un diccionario en python, mostrao de forma bonita por pantalla.

    @entrada:
        diccionario -   Requerido   -   Diccionario
        └ Elemento a imprimir.
        indent      -   Opcional    -   Int
        └ Indentación a mostrar.
        sort        -   Opcional    -   Booleano
        └ Se ordea o diccionario.

    @saida:
        Impresión por pantalla.
    """

    print(json.dumps(diccionario, indent=indent, sort_keys=sort, ensure_ascii=False).encode('utf8').decode())

# --------------------------------------------

if __name__ == '__main__':
    print('*> Probas <*')
    print('> jprint')
    print('Imprimindo {"a": 1, "b": 2}:')
    jprint({'a': 1, 'b': 2})

# --------------------------------------------
