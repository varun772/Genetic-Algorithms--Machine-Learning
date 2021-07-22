import numpy as np
import client as server
import random
#import pandas as pd


id = 'RP4SS6ogrZVSo1lqdTqyV3FlSECOMePWowMwxafjoHIWO8T9q5'

def crossover(parents):
    offspring = np.empty((9,11))
    for k in range(4):
        randone = np.random.randint(1,30)
        u = random.random()
        parent1_idx = (k+randone)%parents.shape[0]
        n_c = 3
        parent2_idx = (k+3+randone)%parents.shape[0]
        beta = 0
        if (u < 0.5):
            beta = (2 * u)**((n_c + 1)**-1)
        else:
            beta = ((2*(1-u))**-1)**((n_c + 1)**-1)
        #print("parents for crossover")
        #print(parents[parent1_idx])
        #print(parents[parent2_idx])
        offspring[k] = 0.5*((1+beta) * parents[parent1_idx] +(1-beta) * parents[parent2_idx])
        offspring[8-k] = 0.5*((1-beta) * parents[parent1_idx] + (1+beta) *parents[parent2_idx])
        #print("crossover obtained")
        #print(offspring)
    return offspring

def mutation(population):
    offspring_mutation=np.empty((3,11))
    offspring_mutation=population
    for i in range(3):
        value1 = np.random.uniform(-0.3, 0.3, 1)
        random_idx=np.random.randint(0,11)
        x = offspring_mutation[i][random_idx] * value1
        #print("parent for mutaion")
        #print(population[i])
        offspring_mutation[i][random_idx]=population[i][random_idx]+ x
        #print("mutaion obtained")
        #print(offspring_mutation)
    return offspring_mutation

def main():
        #print("1")
        givenvector = np.array([1.9237022743158314e-155, -7.562875343278416e-13, -1.0014703304070917e-13, 1.4029357812677044e-11, -0.0005239018228393697, 5.454728690129104e-16, 3.763349229891341e-16, 1.8315187889680715e-05, -1.3182520516828682e-06, -7.45738643620891e-09, 4.77588774576599e-10])
        population = np.zeros((24,11))
        #print("2")
        trainfactor = 0.4
        for i in range(0,24):
            population[i] = givenvector
            value = np.random.uniform(-0.2,0.2,1)
            value1 = np.random.randint(0,11)
            if value1 > 0:
                value1 = value1 - 1
            x = population[i][value1] * value
            population[i][value1]=population[i][value1] + x

        #print("3")
        fitness = np.zeros(24)
        for j in range(0,2):
            print("Generation")
            print(j)
            for i in range(0,len(population)):
                err = server.get_errors('RP4SS6ogrZVSo1lqdTqyV3FlSECOMePWowMwxafjoHIWO8T9q5',list(population[i]))
                print(err)
                print("Population")
                print(list(population[i]))
                assert len(err) == 2
                fitness[i] = err[1]+ ( trainfactor * err[0])
            parents = np.empty((6,11))
            fitness1 = fitness.argsort()
        
            for i in range(0,6):  
                parents[i]=population[int(fitness1[i])]
            #print("parents")
            #print(parents)
            offspring_crossover =  crossover(parents)
            #print("first crossover")
            #print(offspring_crossover)
            offspring_crossover1 = crossover(offspring_crossover)
            #print("double crossover")
            #print(offspring_crossover1)
            offspring_mutation =  mutation(parents)
            #print("first mutation")
            #print(offspring_mutation)
            offspring_mutation1=mutation(offspring_mutation)
            #print("crossover of mutation")
            #print(offspring_mutation1)
            population[0:9,:]=offspring_crossover1[0:9,:]
            population[9:18,:]=offspring_crossover1[0:9,:]
            population[18:21,:]=offspring_mutation[0:3,:]
            population[21:24,:]=offspring_mutation1[0:3,:]
    
if __name__ == '__main__':
    main() 