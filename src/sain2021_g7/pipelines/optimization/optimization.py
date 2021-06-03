from flask.globals import g
import pandas as pd
import numpy as np 
import random


import pandas as pd
import numpy as np 
import random
#import mlrose
vendas2 = pd.read_csv('prodsales.csv', sep=";", header=0, decimal=".") 

#print(vendas2.at[186,'pporto'])


#s1 = [2500, 5, 4, 3, 2, 1, 0]
#s2 = [2500, 5, 3, 4, 2, 1, 0]
#s3 = [2500, 5, 2, 0, 1, 4, 3]

#5 - Guima --> 135
#4 - Braga --> 2031
#3 - Fama  --> 3923
#2 - Barce --> 62
#1 - Povoa --> 274
#0 - Porto --> 2241

distancias = [
        [0, 37, 59, 36, 60, 61], #0, Porto
        [37, 0, 24, 30, 49, 55], #1, Póvoa de Varzim
        [59, 24, 0, 23, 25, 48], #2, Barcelos
        [36, 30, 23, 0, 24, 25], #3, Vila Nova de Famalicão
        [60, 49, 25, 24, 0, 25], #4, Braga
        [61, 55, 48, 25, 25, 0]  #5, Guimarães
    ]

r = range(len(distancias))

caminho = {(i,j):distancias[i][j] for i in r for j in r}
#print(caminho)
#print(distancias[5])


def model(s1):
    K1 = s1[0]
    vendas = 0
    desperdicio = 0
    lucro = 0
    dist = 0
    stock_inicial = 0
    lista = []
    dst = 0
    #stock_final = 0
    for i in s1:
        if i == 5 and K1 > 0:
            #K1 = K1 - 135
            #print(K1)
            s = vendas2.at[186,'sguima']
            p = vendas2.at[186, 'pguima']
            stock_inicial = p - K1
            #print(stock_inicial)
            stock_final = stock_inicial - s
            v = stock_inicial - stock_final
            desperdicio = stock_final * 0.5
            
            vendas = s *2.5
            
            
            lucro = lucro + (vendas - desperdicio)
            print('')
            print('Guimarães --> ' 'Stock Inicial:', stock_inicial,'unidades.', 'Vendas: ', v,'unidades.', 'Stock Final: ', stock_final,'unidades.')
            lista.append(5)

        elif i == 4 and K1 > 0:
            s = vendas2.at[186,'sbraga']
            if K1 >= s:
                stock_inicial = s
                stock_final = stock_inicial - s
                K1 = K1 - s
                vendasb = s *2.5
            else: 
                stock_inicial = K1
                stock_final = 0
                vendasb = K1 *2.5
                K1 = 0
                
            desperdiciob = stock_final * 0.5
            #print(desperdiciob)
            #vendasb = 2031 *2.5
            #print(vendasb)
            v = stock_inicial - stock_final
            lucro = lucro + (vendasb - desperdiciob)
            print('Braga --> ' 'Stock Inicial:', stock_inicial,'unidades.', 'Vendas: ', v,'unidades.', 'Stock Final: ', stock_final,'unidades.')
            lista.append(4)
        
        elif i == 3 and K1 > 0:
            s = vendas2.at[186,'sfama']
            if K1 >= s:
                stock_inicial = s
                stock_final = stock_inicial - s
                K1 = K1 - s
                vendasf = s *2.5
            else: 
                stock_inicial = K1
                stock_final = 0
                vendasf = K1 * 2.5
                K1 = 0
            
            desperdiciof = stock_final * 0.5
            #print(desperdiciob)
            #vendasf = 469 *2.5
            #print(vendasb)
            v = stock_inicial - stock_final
            lucro = lucro + (vendasf - desperdiciof)
            print('Famalicão --> ' 'Stock Inicial:', stock_inicial,'unidades.', 'Vendas: ', v,'unidades.', 'Stock Final: ', stock_final,'unidades.')
            lista.append(3)
            
        elif i == 2 and K1 > 0:
            s = vendas2.at[186,'sbarce']
            if K1 >= s:
                stock_inicial = s
                stock_final = stock_inicial - s
                K1 = K1 - s
                vendasbar = s *2.5
            else: 
                stock_inicial = K1
                stock_final = 0
                vendasbar = K1 *2.5
                K1 = 0
            
            desperdiciobar = stock_final * 0.5
            #print(desperdiciob)
            #vendasbar = 62 *2.5
            #print(vendasb)
            v = stock_inicial - stock_final
            lucro = lucro + (vendasbar - desperdiciobar)
            print('Barcelos --> ' 'Stock Inicial:', stock_inicial,'unidades.', 'Vendas: ', v,'unidades.', 'Stock Final: ', stock_final,'unidades.')
            lista.append(2)
            
        elif i == 1 and K1 > 0:
            s = vendas2.at[186,'spovoa']
            if K1 >= s:
                stock_inicial = s
                stock_final = stock_inicial - s
                K1 = K1 - s
                vendaspov = s *2.5
            else: 
                stock_inicial = K1
                stock_final = 0
                vendaspov = K1 *2.5
                K1 = stock_final
            
            desperdiciopov = stock_final * 0.5
            #print(desperdiciob)
            #vendaspov = 274 *2.5
            #print(vendasb)
            v = stock_inicial - stock_final
            lucro = lucro + (vendaspov - desperdiciopov)
            print('Póvoa --> ' 'Stock Inicial:', stock_inicial,'unidades.', 'Vendas: ', v,'unidades.', 'Stock Final: ', stock_final,'unidades.')
            lista.append(1)
           
        elif i == 0 and K1 > 0:
            s = vendas2.at[186,'sporto']
            if K1 >= s:
                stock_inicial = s
                stock_final = stock_inicial - s
                K1 = K1 - s
                vendasp = s *2.5
            else: 
                stock_inicial = K1
                stock_final = 0
                vendasp = K1 *2.5
                K1 = 0
            
            desperdiciop = stock_final * 0.5
            #print(desperdiciob)
            #vendasp = 2241 *2.5
            #print(vendasb)
            v = stock_inicial - stock_final
            lucro = lucro + (vendasp - desperdiciop)
            print('Porto --> ' 'Stock Inicial:', stock_inicial,'unidades.', 'Vendas: ', v,'unidades.', 'Stock Final: ', stock_final,'unidades.')
            lista.append(0)
    print('')
    print('Lucro Total:', lucro, '€')

    if len(lista) == 1:
        list = [(lista[0], lista[0])]
    elif len(lista) == 2:
        list = [(lista[0], lista[1])]
    elif len(lista) == 3:
        list = [(lista[0], lista[1]), (lista[1], lista[2])]
    elif len(lista) == 4:
        list = [(lista[0], lista[1]), (lista[1], lista[2]), (lista[2], lista[3])]
    elif len(lista) == 5:
        list = [(lista[0], lista[1]), (lista[1], lista[2]), (lista[2], lista[3]), (lista[3], lista[4])]
        
    for a in list:
        if a in caminho:
            r = range(len(distancias))
            i = a[0]
            j = a[1]
            caminho2 = distancias[i][j]
            #print(caminho2)
            dst = dst + caminho2
            #print (dst)
    print('Distância Total:', dst, 'Km')
    print('')
    print('')
    return dst


def randomSolution(distancias):
    cities = list(range(len(distancias)))
    solution = [5]
    cities.remove(5)
    #print(cities)
    for i in range(len(cities)):
        randomCity = cities[random.randint(0, len(cities) - 1)]
        solution.append(randomCity)
        cities.remove(randomCity)
    
    K1 = random.randint(2500,3000)
    print('Produção:', K1, 'unidades.')
    #print(K1)
    solution.insert(0, K1)
    #print(solution)
    return solution
def getNeighbours(solution):
    neighbours = []
    solutionew = solution [2:]
    #print(solution)
    #print(solutionew)
    for i in range(len(solutionew)):
        for j in range(i + 1, len(solutionew)):
            neighbour = solutionew.copy()
            neighbour[i] = solutionew[j]
            neighbour[j] = solutionew[i]
            neighbour.insert(0, solution[0])
            neighbour.insert(1, 5)
            neighbours.append(neighbour)
    #print(neighbours)
    return neighbours



def getBestNeighbour(neighbours):
    bestRouteLength = model(neighbours[0])
    
    bestNeighbour = neighbours[0]
    print(bestNeighbour)
    for neighbour in neighbours:
        currentRouteLength = model(neighbour)
      
        if currentRouteLength < bestRouteLength:
            bestRouteLength = currentRouteLength
            bestNeighbour = neighbour
  
    
   
    return bestNeighbour, bestRouteLength

import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose

dist_list=[(1, 0, 37), (2, 0, 59), (2, 1, 24), (3, 0, 36), (3, 1, 30), (3, 2, 23), (4, 0, 60), (4, 1, 49), (4, 2, 25), (4, 3, 24), (5, 0, 61), (5, 1, 55), (5, 2, 48), (5, 3, 25), (5, 4, 25)]
fitness_dists = mlrose.TravellingSales(distances = dist_list)

def genetic_alg(distancias):
    problem_fit = mlrose.TSPOpt(length = 5, fitness_fn = fitness_dists,
                            maximize=False)
    currentSolution = randomSolution(distancias)
    currentRouteLength = model(currentSolution)
    neighbours = getNeighbours(currentSolution)
    bestNeighbour, bestNeighbourRouteLength = mlrose.genetic_alg(problem_fit, mutation_prob = 0.2, 
					      max_attempts = 1000, random_state = 2)


    #print('The best state found is: ', bestNeighbour)

    #print('The fitness at the best state is: ', bestNeighbourRouteLength)
#solution = [2683, 5, 4, 3, 2, 1, 0]
#neighbour = [[5, 3, 4, 2, 1, 0], [5, 2, 3, 4, 1, 0], [5, 1, 3, 2, 4, 0], [5, 0, 3, 2, 1, 4], [5, 4, 2, 3, 1, 0], [5, 4, 1, 2, 3, 0], [5, 4, 0, 2, 1, 3], [5, 4, 3, 1, 2, 0], [5, 4, 3, 0, 1, 2], [5, 4, 3, 2, 0, 1]]
#model(randomSolution(distancias), 1)
#hillClimbing(distancias)
#randomSolution(distancias)
#getNeighbours(solution)
#getBestNeighbour(neighbour)
#model(neighbours[0])
genetic_alg(distancias)


import pandas as pd
import numpy as np 
import random

vendas2 = pd.read_csv('prodsales.csv', sep=";", header=0, decimal=".") 
#print(vendas2.at[186,'pporto'])


#s1 = [2500, 5, 4, 3, 2, 1, 0]
#s2 = [2500, 5, 3, 4, 2, 1, 0]
#s3 = [2500, 5, 2, 0, 1, 4, 3]

#5 - Guima --> 135
#4 - Braga --> 2031
#3 - Fama  --> 3923
#2 - Barce --> 62
#1 - Povoa --> 274
#0 - Porto --> 2241

distancias = [
        [0, 37, 59, 36, 60, 61], #0, Porto
        [37, 0, 24, 30, 49, 55], #1, Póvoa de Varzim
        [59, 24, 0, 23, 25, 48], #2, Barcelos
        [36, 30, 23, 0, 24, 25], #3, Vila Nova de Famalicão
        [60, 49, 25, 24, 0, 25], #4, Braga
        [61, 55, 48, 25, 25, 0]  #5, Guimarães
    ]

r = range(len(distancias))

caminho = {(i,j):distancias[i][j] for i in r for j in r}
#print(caminho)
#print(distancias[5])

#lucro = 0
#dst = 0
def model(s1):
    K1 = s1[0]
    vendas = 0
    desperdicio = 0
    lucro = 0
    dist = 0
    stock_inicial = 0
    lista = []
    dst = 0
    #stock_final = 0
    for i in s1:
        if i == 5 and K1 > 0:
            #K1 = K1 - 135
            #print(K1)
            s = vendas2.at[186,'sguima']
            p = vendas2.at[186, 'pguima']
            stock_inicial = p - K1
            #print(stock_inicial)
            stock_final = stock_inicial - s
            v = stock_inicial - stock_final
            desperdicio = stock_final * 0.5
            
            vendas = s *2.5
            
            
            lucro = lucro + (vendas - desperdicio)
            #print('--Guimarães--')
            #print('Stock Inicial:', stock_inicial)
            #print('Vendas:', v)
            #print('Stock Final:', stock_final)
            #print('Carga do camião: ', K1)
            lista.append(5)

        elif i == 4 and K1 > 0:
            s = vendas2.at[186,'sbraga']
            if K1 >= s:
                stock_inicial = s
                stock_final = stock_inicial - s
                K1 = K1 - s
                vendasb = s *2.5
            else: 
                stock_inicial = K1
                stock_final = 0
                vendasb = K1 *2.5
                K1 = 0
                
            desperdiciob = stock_final * 0.5
            #print(desperdiciob)
            #vendasb = 2031 *2.5
            #print(vendasb)
            v = stock_inicial - stock_final
            lucro = lucro + (vendasb - desperdiciob)
            #print('')
            #print('--Braga--')
            #print('Stock Inicial:', stock_inicial)
            #print('Vendas:', v)
            #print('Stock Final:', stock_final)
            lista.append(4)
        
        elif i == 3 and K1 > 0:
            s = vendas2.at[186,'sfama']
            if K1 >= s:
                stock_inicial = s
                stock_final = stock_inicial - s
                K1 = K1 - s
                vendasf = s *2.5
            else: 
                stock_inicial = K1
                stock_final = 0
                vendasf = K1 * 2.5
                K1 = 0
            
            desperdiciof = stock_final * 0.5
            #print(desperdiciob)
            #vendasf = 469 *2.5
            #print(vendasb)
            v = stock_inicial - stock_final
            lucro = lucro + (vendasf - desperdiciof)
            #print('')
            #print('--Famalicão--')
            #print('Stock Inicial:', stock_inicial)
            #print('Vendas:', v)
            #print('Stock Final:', stock_final)
            lista.append(3)
            
        elif i == 2 and K1 > 0:
            s = vendas2.at[186,'sbarce']
            if K1 >= s:
                stock_inicial = s
                stock_final = stock_inicial - s
                K1 = K1 - s
                vendasbar = s *2.5
            else: 
                stock_inicial = K1
                stock_final = 0
                vendasbar = K1 *2.5
                K1 = 0
            
            desperdiciobar = stock_final * 0.5
            #print(desperdiciob)
            #vendasbar = 62 *2.5
            #print(vendasb)
            v = stock_inicial - stock_final
            lucro = lucro + (vendasbar - desperdiciobar)
            p#rint('')
            #print('--Barcelos--')
            #print('Stock Inicial:', stock_inicial)
            #print('Vendas:', v)
            #print('Stock Final:', stock_final)
            lista.append(2)
            
        elif i == 1 and K1 > 0:
            s = vendas2.at[186,'spovoa']
            if K1 >= s:
                stock_inicial = s
                stock_final = stock_inicial - s
                K1 = K1 - s
                vendaspov = s *2.5
            else: 
                stock_inicial = K1
                stock_final = 0
                vendaspov = K1 *2.5
                K1 = stock_final
            
            desperdiciopov = stock_final * 0.5
            #print(desperdiciob)
            #vendaspov = 274 *2.5
            #print(vendasb)
            v = stock_inicial - stock_final
            lucro = lucro + (vendaspov - desperdiciopov)
            #print('')
            #print('--Póvoa de Varzim--')
            #print('Stock Inicial:', stock_inicial)
            #print('Vendas:', v)
            #print('Stock Final:', stock_final)
            lista.append(1)
           
        elif i == 0 and K1 > 0:
            s = vendas2.at[186,'sporto']
            if K1 >= s:
                stock_inicial = s
                stock_final = stock_inicial - s
                K1 = K1 - s
                vendasp = s *2.5
            else: 
                stock_inicial = K1
                stock_final = 0
                vendasp = K1 *2.5
                K1 = 0
            
            desperdiciop = stock_final * 0.5
            #print(desperdiciob)
            #vendasp = 2241 *2.5
            #print(vendasb)
            v = stock_inicial - stock_final
            lucro = lucro + (vendasp - desperdiciop)
            #print('')
            #print('--Porto--')
            #print('Stock Inicial:', stock_inicial)
            #print('Vendas:', v)
            #print('Stock Final:', stock_final)
            lista.append(0)
    
    #print('')
    #print('Lucro Total:', lucro, '€')

    if len(lista) == 1:
        list = [(lista[0], lista[0])]
    elif len(lista) == 2:
        list = [(lista[0], lista[1])]
    elif len(lista) == 3:
        list = [(lista[0], lista[1]), (lista[1], lista[2])]
    elif len(lista) == 4:
        list = [(lista[0], lista[1]), (lista[1], lista[2]), (lista[2], lista[3])]
    elif len(lista) == 5:
        list = [(lista[0], lista[1]), (lista[1], lista[2]), (lista[2], lista[3]), (lista[3], lista[4])]
        
    for a in list:
        if a in caminho:
            r = range(len(distancias))
            i = a[0]
            j = a[1]
            caminho2 = distancias[i][j]
            #print(caminho2)
            dst = dst + caminho2
            #print (dst)
    #print('Distância Total:', dst, 'Km')
    #print('')
    #print('')
    return dst, lucro, lista



def randomSolution(distancias):
    cities = list(range(len(distancias)))
    solution = [5]
    cities.remove(5)
    #print(cities)
    for i in range(len(cities)):
        randomCity = cities[random.randint(0, len(cities) - 1)]
        solution.append(randomCity)
        cities.remove(randomCity)
    
    K1 = random.randint(2500,3000)
    #print('produção')
    #print(K1)
    solution.insert(0, K1)
    #print(solution)
    return solution
def getNeighbours(solution):
    neighbours = []
    solutionew = solution [2:]
    #print(solution)
    #print(solutionew)
    for i in range(len(solutionew)):
        for j in range(i + 1, len(solutionew)):
            neighbour = solutionew.copy()
            neighbour[i] = solutionew[j]
            neighbour[j] = solutionew[i]
            neighbour.insert(0, solution[0])
            neighbour.insert(1, 5)
            neighbours.append(neighbour)
    #print(neighbours)
    return neighbours



def getBestNeighbour(neighbours):
    bestRouteLength = model(neighbours[0])
    
    bestNeighbour = neighbours[0]
    #print(bestNeighbour)
    for neighbour in neighbours:
        currentRouteLength = model(neighbour)
      
        if currentRouteLength < bestRouteLength:
            bestRouteLength = currentRouteLength
            bestNeighbour = neighbour
  
    
   
    return bestNeighbour, bestRouteLength

def hillClimbing(distancias):
    currentSolution = randomSolution(distancias)
    currentRouteLength = model(currentSolution)
    neighbours = getNeighbours(currentSolution)
    bestNeighbour, bestNeighbourRouteLength = getBestNeighbour( neighbours)

    while bestNeighbourRouteLength < currentRouteLength:
        currentSolution = bestNeighbour
        currentRouteLength = bestNeighbourRouteLength
        neighbours = getNeighbours(currentSolution)
        bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(neighbours)
    print('')
    print('Distância:', currentRouteLength[0], 'km')
    #print(currentSolution)
    print('')
    print('Lucro:', currentRouteLength[1], '€')
    #print(currentRouteLength[2][0])
    lista2 = []
    for i in currentRouteLength[2]:
        lista2.append(str(i))
    #print(lista2)
    for i in lista2:
        if i == '5': lista2 = np.char.replace(lista2, '5', 'Guimarães')
        elif i == '4': lista2 = np.char.replace(lista2, '4', 'Braga')
        elif i == '3': lista2 = np.char.replace(lista2, '3', 'Famalicão')
        elif i == '2': lista2 = np.char.replace(lista2, '2', 'Barcelos')
        elif i == '1': lista2 = np.char.replace(lista2, '1', 'Póvoa')
        else: i = lista2 = np.char.replace(lista2, '0', 'Porto')
    print('')
    print('Percurso:', lista2)
              

    #print(currentRouteLength[2])
    #print('')
    #print('Lucro Total:', lucro, '€')
    #print('Distância Total:', dst, 'Km')
    return currentSolution, currentRouteLength
#solution = [2683, 5, 4, 3, 2, 1, 0]
#neighbour = [[5, 3, 4, 2, 1, 0], [5, 2, 3, 4, 1, 0], [5, 1, 3, 2, 4, 0], [5, 0, 3, 2, 1, 4], [5, 4, 2, 3, 1, 0], [5, 4, 1, 2, 3, 0], [5, 4, 0, 2, 1, 3], [5, 4, 3, 1, 2, 0], [5, 4, 3, 0, 1, 2], [5, 4, 3, 2, 0, 1]]
#model(randomSolution(distancias), 1)
#hillClimbing(distancias)
#randomSolution(distancias)
#getNeighbours(solution)
#getBestNeighbour(neighbour)
#model(neighbours[0])
hillClimbing(distancias)



import random
import pandas as pd

def optimizeFunc(x):
    return 2.5 * (x[1] +  x[2] + x[3] + x[4] + x[5] + x[6]) - 0.5 * (x[0] - x[1] - x[7])

def evaluate(x):
    score = optimizeFunc(x)
    return score
cities=["Porto", "Póvoa", "Barcelos", "Famalicão", "Braga", "Guimarães"]
distDF = pd.read_csv('dist.csv', sep=";", decimal=".", names=cities) 
distDF.set_index(pd.Index(cities))

distanceArray = distDF.to_numpy()

def calculateDistance(distIndexes):
    dist = 0
    for i in range(0, len(distIndexes)):
        if i + 1 < len(distIndexes):
            dist += distanceArray[distIndexes[i]][distIndexes[i + 1]]
        else:  
            return dist

def pathToString(indexes):
    path = []
    for i in range(0, len(indexes)):
        path.append(cities[indexes[i]])
    return path

def mutate(boundaries):
    indexes = [0]
    mutatedSolution = [4290,135,0,0,0,0,0,0]
    truckLoad = random.randint(10, 3000)
    mutatedSolution[7] = truckLoad
    for i in range(2, len(mutatedSolution) - 1):
        currentIndex = random.randint(2, len(mutatedSolution) - 1)
        if currentIndex not in indexes:
            indexes.append(currentIndex)
        else: 
            while currentIndex in indexes:
                currentIndex = random.randint(2, len(mutatedSolution) - 1)
                if currentIndex not in indexes:
                    indexes.append(currentIndex)
                    break
        
        unload = boundaries[currentIndex]
        if truckLoad > unload:
            truckLoad -= unload
            mutatedSolution[currentIndex] = unload
        else:
            mutatedSolution[currentIndex] = truckLoad
            distIndexes = [x - 2  for x in indexes]
            distIndexes[0] = 5
            distance = calculateDistance(distIndexes)
            return mutatedSolution, distIndexes, distance

x = [4290, 135, 10, 0,0,0, 469, 2500]
boundaries = [4290,135,2241,274,62,3923,2031,2500] # pguima, sGuima, sPorto, sPovoa, sBarcelos, sFama, sBraga, truckload
best_score = evaluate(x)
best_distance = 10000
for i in range(0, 1000000):
    new_x, distIndexes,distance = mutate(boundaries)
    path = pathToString(distIndexes)
    score = evaluate(new_x)

    if  score >= best_score and distance <= best_distance and x != new_x:
        x = new_x
        best_score = score
        best_distance = distance
        print("Solution:", x, "Profit:", best_score, "€", "Path:", path, "Distance:", distance, "Km.") 
    
x = [4290, 135, 10, 0,0,0, 469, 2500]
boundaries = [4290,135,2241,274,62,3923,2031,2500] # pguima, sGuima, sPorto, sPovoa, sBarcelos, sFama, sBraga, truckload
best_score = evaluate(x)
best_distance = 10000
for i in range(0, 1000000):
    new_x, distIndexes,distance = mutate(boundaries)
    path = pathToString(distIndexes)
    score = evaluate(new_x)

    if  score > best_score:
        x = new_x
        best_score = score
        print("Solution:", x, "Profit:", best_score, "€", "Path:", path, "Distance:", distance, "Km.") 


import pandas as pd
import numpy as np 
import random
vendas2 = pd.read_csv('prodsales.csv', sep=";", header=0, decimal=".") 

#print(vendas2.at[186,'pporto'])


s1 = [2500, 5, 4, 3, 2, 1, 0]
#s2 = [2500, 5, 3, 4, 2, 1, 0]
#s3 = [2500, 5, 2, 0, 1, 4, 3]

#5 - Guima --> 135
#4 - Braga --> 2031
#3 - Fama  --> 3923
#2 - Barce --> 62
#1 - Povoa --> 274
#0 - Porto --> 2241

distancias = [
        [0, 37, 59, 36, 60, 61], #0, Porto
        [37, 0, 24, 30, 49, 55], #1, Póvoa de Varzim
        [59, 24, 0, 23, 25, 48], #2, Barcelos
        [36, 30, 23, 0, 24, 25], #3, Vila Nova de Famalicão
        [60, 49, 25, 24, 0, 25], #4, Braga
        [61, 55, 48, 25, 25, 0]  #5, Guimarães
    ]

r = range(len(distancias))

caminho = {(i,j):distancias[i][j] for i in r for j in r}
#print(caminho)
#print(distancias[5])


def model(s1):
    K1 = s1[0]
    vendas = 0
    desperdicio = 0
    lucro = 0
    dist = 0
    stock_inicial = 0
    lista = []
    dst = 0
    #stock_final = 0
    for i in s1:
        if i == 5 and K1 > 0:
            #K1 = K1 - 135
            #print(K1)
            s = vendas2.at[186,'sguima']
            p = vendas2.at[186, 'pguima']
            stock_inicial = p - K1
            #print(stock_inicial)
            stock_final = stock_inicial - s
            v = stock_inicial - stock_final
            desperdicio = stock_final * 0.5
            
            vendas = s *2.5
            
            
            lucro = lucro + (vendas - desperdicio)
            print('Produção: ',K1)
            print('Guimarães --> ' 'Stock Inicial:', stock_inicial,'unidades.', 'Vendas: ', v,'unidades.', 'Stock Final: ', stock_final,'unidades.')
            lista.append(5)

        elif i == 4 and K1 > 0:
            s = vendas2.at[186,'sbraga']
            if K1 >= s:
                stock_inicial = s
                stock_final = stock_inicial - s
                K1 = K1 - s
                vendasb = s *2.5
            else: 
                stock_inicial = K1
                stock_final = 0
                vendasb = K1 *2.5
                K1 = 0
                
            desperdiciob = stock_final * 0.5
            #print(desperdiciob)
            #vendasb = 2031 *2.5
            #print(vendasb)
            v = stock_inicial - stock_final
            lucro = lucro + (vendasb - desperdiciob)
            print('Braga --> ' 'Stock Inicial:', stock_inicial,'unidades.', 'Vendas: ', v,'unidades.', 'Stock Final: ', stock_final,'unidades.')
            lista.append(4)
        
        elif i == 3 and K1 > 0:
            s = vendas2.at[186,'sfama']
            if K1 >= s:
                stock_inicial = s
                stock_final = stock_inicial - s
                K1 = K1 - s
                vendasf = s *2.5
            else: 
                stock_inicial = K1
                stock_final = 0
                vendasf = K1 * 2.5
                K1 = 0
            
            desperdiciof = stock_final * 0.5
            #print(desperdiciob)
            #vendasf = 469 *2.5
            #print(vendasb)
            v = stock_inicial - stock_final
            lucro = lucro + (vendasf - desperdiciof)
            print('Famalicao --> ' 'Stock Inicial:', stock_inicial,'unidades.', 'Vendas: ', v,'unidades.', 'Stock Final: ', stock_final,'unidades.')
            lista.append(3)
            
        elif i == 2 and K1 > 0:
            s = vendas2.at[186,'sbarce']
            if K1 >= s:
                stock_inicial = s
                stock_final = stock_inicial - s
                K1 = K1 - s
                vendasbar = s *2.5
            else: 
                stock_inicial = K1
                stock_final = 0
                vendasbar = K1 *2.5
                K1 = 0
            
            desperdiciobar = stock_final * 0.5
            #print(desperdiciob)
            #vendasbar = 62 *2.5
            #print(vendasb)
            v = stock_inicial - stock_final
            lucro = lucro + (vendasbar - desperdiciobar)
            print('Barcelos --> ' 'Stock Inicial:', stock_inicial,'unidades.', 'Vendas: ', v,'unidades.', 'Stock Final: ', stock_final,'unidades.')
            lista.append(2)
            
        elif i == 1 and K1 > 0:
            s = vendas2.at[186,'spovoa']
            if K1 >= s:
                stock_inicial = s
                stock_final = stock_inicial - s
                K1 = K1 - s
                vendaspov = s *2.5
            else: 
                stock_inicial = K1
                stock_final = 0
                vendaspov = K1 *2.5
                K1 = stock_final
            
            desperdiciopov = stock_final * 0.5
            #print(desperdiciob)
            #vendaspov = 274 *2.5
            #print(vendasb)
            v = stock_inicial - stock_final
            lucro = lucro + (vendaspov - desperdiciopov)
            print('Povoa --> ' 'Stock Inicial:', stock_inicial,'unidades.', 'Vendas: ', v,'unidades.', 'Stock Final: ', stock_final,'unidades.')
            lista.append(1)
           
        elif i == 0 and K1 > 0:
            s = vendas2.at[186,'sporto']
            if K1 >= s:
                stock_inicial = s
                stock_final = stock_inicial - s
                K1 = K1 - s
                vendasp = s *2.5
            else: 
                stock_inicial = K1
                stock_final = 0
                vendasp = K1 *2.5
                K1 = 0
            
            desperdiciop = stock_final * 0.5
            #print(desperdiciob)
            #vendasp = 2241 *2.5
            #print(vendasb)
            v = stock_inicial - stock_final
            lucro = lucro + (vendasp - desperdiciop)
            print('Porto --> ' 'Stock Inicial:', stock_inicial,'unidades.', 'Vendas: ', v,'unidades.', 'Stock Final: ', stock_final,'unidades.')
            lista.append(0)
    print('')
    print('Lucro Total:', lucro, '€')

    if len(lista) == 1:
        list = [(lista[0], lista[0])]
    elif len(lista) == 2:
        list = [(lista[0], lista[1])]
    elif len(lista) == 3:
        list = [(lista[0], lista[1]), (lista[1], lista[2])]
    elif len(lista) == 4:
        list = [(lista[0], lista[1]), (lista[1], lista[2]), (lista[2], lista[3])]
    elif len(lista) == 5:
        list = [(lista[0], lista[1]), (lista[1], lista[2]), (lista[2], lista[3]), (lista[3], lista[4])]
        
    for a in list:
        if a in caminho:
            r = range(len(distancias))
            i = a[0]
            j = a[1]
            caminho2 = distancias[i][j]
            #print(caminho2)
            dst = dst + caminho2
            #print (dst)
    print('Distância Total:', dst, 'Km')
    print('')
    print('')
    return lucro


def randomSolution(distancias):
    cities = list(range(len(distancias)))
    solution = [5]
    cities.remove(5)
    print(cities)
    for i in range(len(cities)):
        randomCity = cities[random.randint(0, len(cities) - 1)]
        solution.append(randomCity)
        cities.remove(randomCity)
    
    K1 = random.randint(2500,3000)
    #K1 = 2500
    print('produção')
    print(K1)
    solution.insert(0, K1)
    print(solution)
    return solution
def getNeighbours(solution):
    neighbours = []
    solutionew = solution [2:]
    print(solution)
    print(solutionew)
    for i in range(len(solutionew)):
        for j in range(i + 1, len(solutionew)):
            neighbour = solutionew.copy()
            neighbour[i] = solutionew[j]
            neighbour[j] = solutionew[i]
            neighbour.insert(0, solution[0])
            neighbour.insert(1, 5)
            neighbours.append(neighbour)
    print(neighbours)
    return neighbours



def getBestNeighbour(neighbours):
    bestRouteLength = model(neighbours[0])
    
    bestNeighbour = neighbours[0]
    print(bestNeighbour)
    for neighbour in neighbours:
        currentRouteLength = model(neighbour)
      
        if currentRouteLength < bestRouteLength:
            bestRouteLength = currentRouteLength
            bestNeighbour = neighbour
  
    
   
    return bestNeighbour, bestRouteLength

import random
import math

def simulated_annealing(initial_state):
    """Peforms simulated annealing to find a solution"""
    initial_temp = 50
    final_temp = 1
    alpha = 1
    
    current_temp = initial_temp

    # Start by initializing the current state with the initial state
    current_state = initial_state
    solution = current_state
    teste = randomSolution(distancias)
    while current_temp > final_temp:
        neighbour = teste
        print('Aqui----------------------')
        print(neighbour)
        # Check if neighbor is best so far
        cost_diff = model(current_state) - model(neighbour)

        # if the new solution is better, accept it
        if cost_diff > 0:
            solution = neighbour
        # if the new solution is not better, accept it with a probability of e^(-cost/temp)
        else:
            if random.uniform(0, 1) < math.exp(-cost_diff / current_temp):
                solution = neighbour
        # decrement the temperature
        current_temp -= alpha

    return solution


simulated_annealing(s1)

def optimization(
    concat_results_sarimax: pd.DataFrame,
    contat_result_prophet: pd.DataFrame
) -> pd.DataFrame:

    hill_climbing = pd.DataFrame()   
    simulated_annealing = pd.DataFrame()   
    genetic_algorithm = pd.DataFrame()   
    monte_carlo = pd.DataFrame()  

    return hill_climbing, simulated_annealing, genetic_algorithm, monte_carlo 

    
