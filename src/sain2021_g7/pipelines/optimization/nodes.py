# Copyright 2021 QuantumBlack Visual Analytics Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND
# NONINFRINGEMENT. IN NO EVENT WILL THE LICENSOR OR OTHER CONTRIBUTORS
# BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# The QuantumBlack Visual Analytics Limited ("QuantumBlack") name and logo
# (either separately or in combination, "QuantumBlack Trademarks") are
# trademarks of QuantumBlack. The License does not grant you any right or
# license to the QuantumBlack Trademarks. You may not use the QuantumBlack
# Trademarks or any confusingly similar mark as a trademark for your product,
# or use the QuantumBlack Trademarks in any other manner that might cause
# confusion in the marketplace, including but not limited to in advertising,
# on websites, or on software.
#
# See the License for the specific language governing permissions and
# limitations under the License.
"""
This is a boilerplate pipeline 'optimization'
generated using Kedro 0.17.3
"""

import pandas as pd
import numpy as np 
import random


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
            print('--Guimarães--')
            print('Stock Inicial:', stock_inicial)
            print('Vendas:', v)
            print('Stock Final:', stock_final)
            print('Carga do camião: ', K1)
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
            print('')
            print('--Braga--')
            print('Stock Inicial:', stock_inicial)
            print('Vendas:', v)
            print('Stock Final:', stock_final)
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
            print('')
            print('--Famalicão--')
            print('Stock Inicial:', stock_inicial)
            print('Vendas:', v)
            print('Stock Final:', stock_final)
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
            print('')
            print('--Barcelos--')
            print('Stock Inicial:', stock_inicial)
            print('Vendas:', v)
            print('Stock Final:', stock_final)
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
            print('')
            print('--Póvoa de Varzim--')
            print('Stock Inicial:', stock_inicial)
            print('Vendas:', v)
            print('Stock Final:', stock_final)
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
            print('')
            print('--Porto--')
            print('Stock Inicial:', stock_inicial)
            print('Vendas:', v)
            print('Stock Final:', stock_final)
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
    print(cities)
    for i in range(len(cities)):
        randomCity = cities[random.randint(0, len(cities) - 1)]
        solution.append(randomCity)
        cities.remove(randomCity)
    
    K1 = random.randint(2500,3000)
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
    #print(currentRouteLength)
    #print(currentSolution)
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