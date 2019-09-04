""" Algoritmo de Ford Fulkerson """

# importa numpy al proyecto
import numpy as np

# Especifica el número de vértices de tu gráfica
N = 8
# el arreglo que guardará la trayectoria entre la fuente y el pozo
trayectoria = np.array([], dtype='int32')

INFINITE = 9999999999

# se define el algoritmo de búsqueda, que regresa True si el pozo fue visitado
def BFS(grafoResidual, inicio, pozo, trayectoria):

    queue = np.array([], dtype='int32')
    visitado = np.array([], dtype='int32')

    for x in range(0, N):
        visitado = np.append(visitado, 0)

    queue = np.append(queue, inicio)
    visitado[inicio] = True
    trayectoria[inicio] = -1


    while not len(queue) == 0:

        u, queue = queue[0], queue[1:len(queue)]

        for v in range(0,N):
            if visitado[v] == False and grafoResidual[u][v] > 0:

                queue = np.append(queue, v)
                visitado[v] = True
                trayectoria[v] = u

    if visitado[pozo]:

        return True

    else:

        return False

# Ford Fulkerson te pide un grafo y especificar fuente y pozo
def AlgoritmoFordFulkerson(grafo, inicio, pozo):

    u,v = 0,0
    grafoResidual = grafo.copy()
    maxFlow = 0

    while BFS(grafoResidual, inicio, pozo, trayectoria):

        pathFlow = INFINITE
        v = pozo

        while not v == inicio:

            u = trayectoria[v]
            pathFlow = min(pathFlow, grafoResidual[u][v])
            v = trayectoria[v]

        v = pozo

        while not v == inicio:

            u = trayectoria[v]
            grafoResidual[u][v] -= pathFlow
            grafoResidual[v][u] += pathFlow
            v = trayectoria[v]

        maxFlow += pathFlow

    return maxFlow

def main():
# especifica tu gráfica
    grafo = np.array([[0, 9, 7, 9, 0, 0, 0, 0],
                      [0, 0, 0, 0, 5, 4, 0, 0],
                      [0, 0, 0, 0, 0, 0, 8, 0],
                      [0, 0, 0, 0, 0, 0, 11, 0],
                      [0, 0, 0, 2, 0, 0, 0, 3],
                      [0, 0, 1, 0, 0, 0, 0, 3],
                      [0, 0, 0, 0, 0, 0, 0, 19],
                      [0, 0, 0, 0, 0, 0, 0, 0]]);

    for x in range(0, N):
         global trayectoria
         trayectoria = np.append(trayectoria, 0)


    print("El flujo máximo de la gráfica es {}".format(AlgoritmoFordFulkerson(grafo, 0, N-1)))

if __name__ == '__main__':
    main()
