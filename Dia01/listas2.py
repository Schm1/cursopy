lista = [0] * 10
lista[0] = 10
lista[1] = 20
lista[2] = 30
copia = lista[:]
naoecopia = lista
naoecopia[0] = 200
copia[0] = 100
print("Lista", lista)
print("Copia",copia)
print("naoecopia",naoecopia)
