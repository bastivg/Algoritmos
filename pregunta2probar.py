#lcs
#**Busca la cadena de similitud mas grande
#**usando programacion dinamica guarda los valores en una matriz de dimension 2.
def lcs(X, Y , L):
    m = len(X)
    n = len(Y)
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    return L

#fpc
#**funcion que recorre la matriz buscando la cadena de similitud mas larga
#**dependiendo de X rellena la lista con - en las partes que no hay similitud
#**Se uso como referencia https://www.youtube.com/watch?v=er7_2ATj-vk&t=1045s&ab_channel=jorgerodriguezc
def fpc(X , Y , L):
    m = len(X)
    n = len(Y)
    palabra = ""
    while(n > 0 and m > 0):
        if(X[m-1] == Y[n-1]):
            palabra += X[m-1]
            n= n-1
            m= m-1
        else:
            if(L[m-1][n] >= L[m][n-1]):
                m= m-1
                palabra+="-"
            else:
                n= n-1
    return palabra

#creacion matriz
##crea la matriz en la que se guardaran los valores.
def creacion_matriz(X,Y):
    m = len(X)
    n = len(Y)
    L = []
    for i in range(m+1):
        L.append([])
        for j in range(n+1):
            L[i].append(None)
    ##llenado de la matriz.
    for i in range(m + 1):
        L[i][0] = 0
    for j in range(n + 1):
        L[0][j] = 0
    L = lcs(X,Y,L)
    return L

def borrar_numero(palabra):
    con = 0
    while con < len(palabra):
        if(palabra[con] == " "):
            con += 1
            palabra = palabra[con:]
            return(palabra)
        con += 1
    return(-1)

contador_casos = 0; contador_output = 0; definitivo = ""; tempt = ""
num_casos = int(input())
definitivo += str(num_casos) + "\n"
while contador_casos < num_casos:
    palabra1 = input()
    X = borrar_numero(palabra1)
    palabra2 = input()
    Y = borrar_numero(palabra2)
    m = len(X)
    n = len(Y)
    L = []

    L1 = creacion_matriz(X,Y)
    h1 = fpc(X,Y,L1)
    h1 = h1[::-1]
    L2 = creacion_matriz(Y,h1)
    h2 = fpc(Y,h1,L2)
    h2 = list(reversed(h2))
    c1,c2 = 0,0
    aux1 = ""
    aux2 = ""
    if(h1[0] != X[c1]):
        while(c1 <len(h1) and h1[0] != X[c1]):
            aux1 += X[c1]
            c1 += 1
        contador_output += 1
        tempt +=  aux1 + "\n"
        X = X[c1:]
        aux1 = ""
    if(h2[0] != Y[c2]):
        while(c2 <len(h2) and h2[0] != Y[c2]):
            aux2 += Y[c2]
            c2 += 1
        contador_output += 1
        tempt += "  " + aux2 + "\n"
        Y = Y[c2:]
        aux2 = ""
    c1,c2 = 0,0
    while c1 < len(h1) and c2 < len(h2):
        if(h1[c1] == "-" and h2[c2] == "-"):
            while(c1 <len(h1) and h1[c1] == "-"):
                aux1 += X[c1]
                c1 += 1
            while (c2 < len(h2) and h2[c2] == "-"):
                aux2 += Y[c2]
                c2 += 1
            contador_output += 1
            tempt += aux1 + " " + aux2 + "\n"
            aux1,aux2 = "",""
        elif(h2[c2] == "-"):
            while (c2 < len(h2) and h2[c2] == "-"):
                aux2 += Y[c2]
                c2 += 1
            contador_output += 1
            tempt += "  " + aux2 + "\n"
            aux2 = ""
        elif(h1[c1] == "-"):
            while(c1 <len(h1) and h1[c1] == "-"):
                aux1 += X[c1]
                c1 += 1
            contador_output += 1
            tempt += aux1 + "\n"
            aux1 = ""
        c1+=1
        c2+=1
    while c1 < len(h1):
        if(h1[c1] == "-"):
            while(c1 <len(h1) and h1[c1] == "-"):
                aux1 += X[c1]
                c1 += 1
            contador_output += 1
            tempt += aux1 + "\n"
            aux1 = ""
        c1+=1
    while c2 < len(h2):
        if(h2[c2] == "-"):
            while (c2 < len(h2) and h2[c2] == "-"):
                aux2 += Y[c2]
                c2 += 1
            contador_output += 1
            tempt += "  " + aux2 + "\n"
            aux2 = ""
        c2+=1
    definitivo += str(contador_output) + "\n"
    definitivo += tempt
    contador_output = 0;contador_casos += 1; tempt = ""
print(definitivo)
