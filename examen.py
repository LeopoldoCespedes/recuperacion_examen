def mediana(diccionario):
    ascendente = {}
    lista = []
    i= 0
    mediana = 0
    for valor in diccionario:
        lista.append(diccionario["valor"+str(i)])
        i = i+1
    ascendente = sorted(lista)
    print(ascendente)
    if len(ascendente) % 2 == 1:
        mediana =  ascendente[len(ascendente) // 2]
    else:
        mediana=  (ascendente[len(ascendente)//2 - 1] + ascendente[len(ascendente) // 2]) / 2

    return mediana
valores = {'valor0':5,'valor1':3,'valor2':8,'valor3': 1,'valor4':6}
#1 3 5 6 8
print(mediana(valores))      


def procesar(fichero,numero):
    lista_alumnos = []
    with open(fichero, 'r') as file:
        for linea in file:
            palabras = linea.split()
            if numero in palabras:
                lista_alumnos.append(linea)
    return lista_alumnos
procesar()
                    