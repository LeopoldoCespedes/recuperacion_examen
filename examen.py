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
    cont = 0
    with open(fichero, 'r') as file:
        for linea in file:
            palabras = linea.split()
            for palabra in palabras:
             n = len(palabras[0])
             if palabras[0][n-1] == str(numero):
                cont = 1
                lista_alumnos.append(linea)
        if cont == 0:
            raise ValueError("No hay estudiantes de ese curso")
             
    return lista_alumnos
print(procesar("C:\\Users\\rokoh\\OneDrive\\Escritorio\\python examen\\recuperacion_examen\\recuperacion_examen\\fichero.csv",3))

def combinar(diccionario_nombres_edades,diccionario_nombres_profesiones,diccionario_nombres_sueldos):
    diccionario_final = {}
    for values in diccionario_nombres_edades:
         diccionario_final[values] = {
            'edad': diccionario_nombres_edades[values],
            'profesión': diccionario_nombres_profesiones[values],
            'sueldo': diccionario_nombres_sueldos[values]
        }
    return diccionario_final
diccionario_nombres_edades = {'Ana': 25, 'Juan': 30, 'Maria': 28}
diccionario_nombres_profesiones = {'Ana': 'Ingeniera', 'Juan': 'Doctor', 'Maria':'Abogada'}
diccionario_nombres_sueldos = {'Ana': 5000, 'Juan': 7000, 'Maria': 6000}
print(combinar(diccionario_nombres_edades,diccionario_nombres_profesiones,diccionario_nombres_sueldos))

from collections import defaultdict

def palabra_repetida(nombre_archivo):
    contador = defaultdict(int)
    palabra_max = ""
    with open(nombre_archivo, 'r') as file:
        for linea in file:
            palabras = linea.split()
            for palabra in palabras:
                contador[palabra] += 1
        maximo = max(contador.values())
        for palabra, repeticiones in contador.items():
            if repeticiones == maximo:
                palabra_max = palabra
        return palabra_max
print(palabra_repetida("C:\\Users\\rokoh\\OneDrive\\Escritorio\\python examen\\recuperacion_examen\\recuperacion_examen\\palabras.txt"))

    




