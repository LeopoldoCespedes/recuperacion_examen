def mediana(diccionario):
    ascendente = {}
    lista = []
    i= 0
    for valor in diccionario:
        lista.append(diccionario["valor"+str(i)])
        i = i+1
    sorted(lista)
    #ahora la mediana  de la lista sorted
    if(len(lista)%2 == 0):
        mediana = lista[len(lista)/2] + lista[(len(lista)/2)+1]
        print(mediana)
    else:
        mediana = lista[int(len(lista)/2)]
        ascendente.update({"mediana":mediana})


    return ascendente
valores = {'valor0':5,'valor1':3,'valor2':8,'valor3': 1,'valor4':6}
print(mediana(valores))      