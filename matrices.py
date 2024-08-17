matriz = [[12,2,3],
          [4,545,6],
          [798,8,9]
         ]

matrizchar=[['A','B','C','D'],['E','F','G','H'],['I','J','K','L'],['M','N','O','P']]


def imprimirMatriz(matriz):
    tamax=1
    for fila in matriz:
        for elemento in fila:
            if len(str(elemento))>tamax:
                tamax=len(str(elemento))
    for fila in matriz:
        for elemento in fila:
            print(f'{elemento:{tamax}}', end=' ')
        print()

matrizPalabras=[['Basquétbol','Beisbol','Ajedrez'],['Natación','Voleibol','Fútbol'],['Damas', 'Tenis','Tiro con arco']]

def imprimirTabla(tabla, titulos):
    tabla.insert(0, titulos)
    tamax=[]
    i=0
    for fila in tabla:
        i+=1
        j=0
        for elemento in fila:
            if i==1:
                tamax.append(len(str(elemento)))
            elif tamax[j]<len(str(elemento)):
                tamax[j]=len(str(elemento))
            j+=1
    for fila in tabla:
        j=0
        for elemento in fila:
            print(f'{elemento:{tamax[j]}}', end=' ')
            j+=1
        print()

empleados=[['25363', 'Pedro Guillermo Rodríguez Pineda', '829-923-5678'],['24267', 'Carlos Pérez Parra', '809-819-6909']]
titulos=['Código','Nombre completo', 'Número']

matrizCalificaciones=[[90,95,100],
                      [97,89,93],
                      [85,94,100]]

def obtenerPromedioFila(matriz, nfila):
    sumatoria=0
    for valor in matriz[nfila]:
        sumatoria+=valor
    return sumatoria/len(matriz[nfila])

def obtenerPromedioColumna(matriz, ncol):
    sumatoria=0
    for fila in matriz:
        sumatoria+=fila[ncol]
    return sumatoria/len(matriz)

def obtenerTraza(matriz):
    traza=0
    j=0
    for fila in matriz:
        traza+=fila[j]
        j+=1
    return traza

def obtenerTrazaInversa(matriz):
    trazainversa=0
    j=len(matriz)-1
    for i in range(len(matriz)):
        trazainversa+=matriz[i][j]
        j-=1
    return trazainversa

print(obtenerTrazaInversa(matrizCalificaciones))
