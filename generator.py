import random
from itertools import *
import time

# импорт собственных файлов
from genetic import *
from tables import  *

A_MAX = 2**20
LENGTH = 24
random.seed(100)

#генератор рюкзачного вектора
def vector_gen():
    vector = []
    for _ in range(0, LENGTH):
        vector.append(random.randint(1, A_MAX))
    vector.sort()
    return(vector)

# генератор n рюкзаков
def backpacks_gen(n):
    backpacks = []
    for _ in range (0, n):
        backpacks.append(vector_gen())
    return backpacks

# генератор целевых весов рюкзака
def backpack_task(vector):
    part = random.randint(3, 12)
    weight = sum(random.sample(vector, k=part))
    return(weight, part)

# осуществление полного перебора c таймированием
def full_enumeration(vector, weight):
    count = 0
    beg = time.perf_counter() 
    for l in range(0,24):
        for tmp in combinations(vector, l):
            if sum(tmp) == weight:
                count += 1
                if count == 1:
                    clock1 = time.perf_counter() - beg
                    clock_all = clock1
                else:
                    clock_all = time.perf_counter() - beg
    return(clock1, clock_all, count)

if __name__ == "__main__":
    # генерация векторов
    vectors = []
    for _ in range(50):
        vectors.append(vector_gen())
    vectors_table_gen(vectors)

    # генерация задач о рюкзаке
    backpacks = []
    for i in range(50):
        vector = vectors[i]
        for _ in range(10):
            backpacks.append(backpack_task(vector))
    tasks_table_gen(backpacks)

    '''
    # генерация решений полным перебором
    full_en_sol = []
    for i in range (50):
        vector = vectors[i]
        for j in range(10):
            weight = backpacks[10*i + j][0]
            full_en_sol.append(full_enumeration(vector, weight))
    full_en_table_sol(full_en_sol)
    '''

    # генерация решений ген-алгоритмом
    genetic_sol = []
    for i in range (50):
        vector = vectors[i]
        for j in range(10):
            weight = backpacks[10*i + j][0]
            genetic_sol.append(genetic(vector, weight))
    gen_table_sol(genetic_sol)
