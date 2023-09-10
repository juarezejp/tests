#Contar los cuadrados elegantes en un jardin
def contar_cuadros_elegantes(N, M, jardin):
    count = 0
    #iterar a traves de las filas y columnas del jardin
    for i in range(N):
        for j in range(M):
            #Comparar el color de la celda actual con las celdas en las esquinas de los cuadrados
            for x in range(i+1, N):
                for y in range(j+1, M):
                    if jardin[i][j] == jardin[i][y] == jardin[x][j] == jardin[x][y]:
                        count += 1
    return count

#lectura de la entrada desde un archivo de texto
with open("input.txt", "r") as entrada:
    T = int(entrada.readline().strip())
    for _ in range(T):
        N, M = map(int, entrada.readline().strip().split())
        jardin = []
        for _ in range(N):
            linea = entrada.readline().strip()
            jardin.append(linea)
        
        #Llamar a la funcion e imprimir el resultado
        res = contar_cuadros_elegantes(N, M, jardin)
        print(res)
