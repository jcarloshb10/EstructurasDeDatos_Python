def preorden(arbol_bin):
    __preorden(arbol_bin.raiz)

def __preorden(sub_arbol):
    if sub_arbol:
        #print(sub_arbol.clave)
        __preorden(sub_arbol.izq)
        __preorden(sub_arbol.der)

def cad_preorden(arbol_bin, sep="^"):
    """Retorna una cadena en preorden, utilizando
    un separador "^"
    "clave1^clave2^...^claveN"
    Para personas sería: "123:Juan:20 años*089:Hugo:50 años*...*789:Pedro:6 años"
    """    
    
    return sep.join(__cad_preorden(arbol_bin.raiz))

def __cad_preorden(sub_arbol):
    cadena = ""
    if sub_arbol is not None:
        cadena = str(sub_arbol.clave)
        cadena += __cad_preorden(sub_arbol.izq)
        cadena += __cad_preorden(sub_arbol.der)
    return cadena

def inorden(arbol_bin):
    __inorden(arbol_bin.raiz)

def __inorden(sub_arbol):
    if sub_arbol is not None:
        #print(sub_arbol.clave)
        __inorden(sub_arbol.izq)
        __inorden(sub_arbol.der)

def cad_inorden(arbol_bin, sep="-"):
    return sep.join(__cad_inorden(arbol_bin.raiz))

def __cad_inorden(sub_arbol):
    cadena = ""
    if sub_arbol is not None:
        cadena = __cad_inorden(sub_arbol.izq)
        cadena += str(sub_arbol.clave)
        cadena += __cad_inorden(sub_arbol.der)
    return cadena

def postorden(arbol_bin):
    __postorden(arbol_bin.raiz)

def __postorden(sub_arbol):
    if sub_arbol is not None:
        #print(sub_arbol.clave)
        if sub_arbol.izq is not None:
            __postorden(sub_arbol.izq)
        if sub_arbol.der is not None:
            __postorden(sub_arbol.der)

def cad_postorden(arbol_bin, sep="-"):
    return sep.join(__cad_postorden(arbol_bin.raiz))

def __cad_postorden(sub_arbol):
    cadena = ""
    if sub_arbol is not None:
        if sub_arbol.izq is not None:
            cadena += __cad_postorden(sub_arbol.izq)
        if sub_arbol.der is not None:
            cadena += __cad_postorden(sub_arbol.der)
        cadena += str(sub_arbol.clave)
    return cadena

