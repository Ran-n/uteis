#! /usr/bin/python3
# -*- coding: utf-8 -*-
# --------------------------------------------
#+ Autor:	Ran#
#+ Creado:	05/07/2021 17:36:35
#+ Editado:	05/07/2021 20:50:34
# --------------------------------------------
import os
import json
# --------------------------------------------
# carga os contidos dun ficheiro
def cargarFich(fich_nome, encoding='utf-8-sig'):
    # se o ficheiro a cargar non existe sacar erro
    if not os.path.isfile(fich_nome):
        raise Exception('O ficheiro {} non existe'.format(nome))

    # faise neste bloque en lugar de directamente para poder pechar a conexión
    # de non pechala pódese corromper
    try:
        conn = open(fich_nome, 'r', encoding=encoding)
        fich_contido = conn.read()
    except:
        # saca o erro producido
        raise
    finally:
        conn.close()
        return fich_contido

# garda nun ficheiro os contidos dun diccionario de python no formato json
def jgardarFich(fich_nome, contido, indent=1, sort_keys=False, ensure_ascii=False):
    # faise neste bloque en lugar de directamente para poder pechar a conexión
    # de non pechala pódese corromper
    try:
        conn = open(ficheiro, 'w')
        conn.write(json.dumps(contido, indent=indent, sort_keys=sort_keys, ensure_ascii=ensure_ascii))
    except:
        # saca o erro producido
        raise
        return False
    finally:
        conn.close()
        return True

# --------------------------------------------
if __name__ == '__main__':
    print('*> Probas <*')
    print('> cargar')
    print('sen facer')
# --------------------------------------------
