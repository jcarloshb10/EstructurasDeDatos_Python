#!/usr/bin/env python
from ed.secuenciales.listaSE import ListaSE
from ed.secuenciales.listaCSE import ListaCSE
from loteria import Premio, Loteria, Concursante

#MI TEST Parcial 2
if __name__ == "__main__":
    
    
    premi=Premio("camioneta",52)
    premi2=Premio("camion",49)
    premi3=Premio("camioncito",18)
    print(premi==premi2)
    print(premi)
    print(premi2)
    print("#################concursantes##################")
    concu=Concursante("Andres")
    concu1=Concursante("andres")
    concu2=Concursante("Andres")
    concu3=Concursante("Jiame")
    print(concu==concu2)
    print(concu)
    print(concu1)
    print(concu2)
    print("###################### loteria ###############################")
    loter=Loteria(400)
    print(loter.agregar_premio(premi))
    print(loter.__str__())
    print(loter.agregar_premio(premi2))
    print(loter.agregar_premio(premi3))
    print("###################### Agregar cocursante a la loteria ###############################")
    print(loter.agregar_concursante(concu))
    print(loter.agregar_concursante(concu1))
    print(loter.agregar_concursante(Concursante("sebitas")))
    #print(loter.agregar_concursante(Concursante("Jiame")))


    print("$$$$$$$$$$$$$$$$$$$$presentacion############################")
    print(loter.__str__())
    print("______________________")
    print("El total de premios acumulado es : ",loter.pozo())

    print(loter.sortear(23,12))
    print("______________________")
    print(loter.__str__())
    print("______________________")
    print(loter.sortear(23,12))
    print("______________________")
    print(loter.__str__())
    print("______________________")
    print(loter.sortear(23,12))
    print("______________________")
    print(loter.__str__())
    print(loter.agregar_concursante(Concursante("robertp")))
    print(loter.agregar_concursante(Concursante("roberto")))
    print(loter.agregar_concursante(Concursante("jdzan")))
    print("______________________")
    print(loter.sortear(23,12))
    print("______________________")
    print(loter.__str__())
    print("______________________")
    print(loter.sortear(23,12))
    print("______________________")
    print(loter.__str__())
    print("______________________")
    print(type(loter.sortear(23,12)))
    print("______________________")
    print(loter.__str__())
    print("______________________")
