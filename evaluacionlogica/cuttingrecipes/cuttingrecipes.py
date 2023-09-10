#Calcular MCD de dos números
def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

#Funcion para reducir la receta
def reducir_receta(ingredientes):
    #Encontrar el mcd de todos los ingredientes
    mcd_comun = ingredientes[0]
    for i in range(1, len(ingredientes)):
        mcd_comun = mcd(mcd_comun, ingredientes[i])
    
    #Reducir la receta dividiendo todos los ingredientes por el mcd comun
    receta_reducida = []
    for ingrediente in ingredientes:
        resultado = ingrediente // mcd_comun
        receta_reducida.append(str(resultado))
    return receta_reducida

#Leer archivo deentrada desde el archivo "recetas.txt"
with open("recetas.txt", "r") as infile:
    T = int(infile.readline().strip())
    for _ in range(T):
        datos = infile.readline().strip().split()
        N = int(datos[0])
        ingredientes = []
        for i in range(1, N+1):
            ingrediente = int(datos[i])
            ingredientes.append(ingrediente)        
        #llamar a la funcion para reducir la receta y mostrar el resultado
        res = reducir_receta(ingredientes)
        print(" ".join(res))
