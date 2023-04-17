import random
import time

chrome_len = 24      # длина хромосомы
population = 100      # размер популяции
cross_prob = 0.5     # вероятность кроссинговера
mut_prob = 0.1       # вероятность мутации

# генерация одной рандомной хромосомы
def rand_generation(chrome_len):
    chromosome = ''
    for _ in range (chrome_len+1):
        chromosome += str(random.randint(0,1))
    return(chromosome)  

#генерация популяции в виде словаря с фитнесс-функцией
def pop_generation(population, vector, weight):
    dict_pop = {}
    for _ in range (population):
        chromosome = rand_generation(chrome_len)
        dict_pop[chromosome] = fitness(chromosome, vector, weight)    
    return(dict_pop)

#подсчет фитнесс функции 
def fitness(chromosome, vector, weight):
    s = 0
    for i in range(len(vector)):
        s += int(chromosome[i])*vector[i]
    fitness = abs(weight - s)
    return(fitness)

# кроссинговер (chromosome : str)
def crossingover(chromosome, chromosome1):
    k = random.randint(0, chrome_len)
    new = chromosome[0:k] + chromosome1[k:]
    new1 = chromosome1[0:k] + chromosome[k:]
    return(new, new1)

# мутация (chromosome : str)
def mutation(chromosome):
    k = random.randint(0, 13) 
    new = list(chromosome)
    new[k] = str(abs(int(new[k])-1))
    return(''.join(new))

# репродукция на основе метода ранжирования
def reproduction(dict_pop):
    #сортируем словарь
    sorted_dict = {}
    sorted_keys = sorted(dict_pop.keys())
    for w in sorted_keys:
        sorted_dict[w] = dict_pop[w]
    l = len(sorted_dict)
    prob = [round((i+1)*200/(l*(l+1)), 2) for i in range(l)]
    chromosome = random.choices(list(sorted_dict), weights=prob)[0]
    chromosome1 = random.choices(list(sorted_dict), weights=prob)[0]
    while chromosome1 == chromosome:
        chromosome1 = random.choices(list(sorted_dict), weights=prob)[0]
    return(crossingover(chromosome, chromosome1))

# функция остановки алгоритма
def check_out(count, min_fitness, gen_time):
    flag = 0
    if (count == 100) or (min_fitness == 0) or (gen_time > 10):
        flag = 1
    return (flag)

# функция вероятностного кроссинговера
def prob_cross(child_pop, chromosome, vector, weight):
    if random.random() < cross_prob:
        child_pop[chromosome] = fitness(chromosome, vector, weight)

# функция поиска решения с помощью ген-алгоритма
def genetic(vector, weight):
    dict_pop = pop_generation(population, vector, weight)        # основная популяция
    child_pop = {}                                               # популяция детей
    num_generation = 0                                           # подсчет числа популяция
    count, min_fitness = 0, 0                                                    # подсчет итераций, где не улучшается фитнесс-функция
    beg = time.perf_counter() 
    while True:
        num_generation += 1
        if min_fitness == (min(dict_pop.values())):
            count +=1
        else:
            count = 0
        min_fitness = (min(dict_pop.values()))
        for _ in range (0, population):
            x, y = reproduction(dict_pop)[0], reproduction(dict_pop)[1] # получение 2ух дочерних хромосом
            prob_cross(child_pop, x, vector, weight)
            prob_cross(child_pop, y, vector, weight)
        for chromosome in child_pop:
            if random.random() < mut_prob:
                new = mutation(chromosome)
                dict_pop[new] = fitness(new, vector, weight)
        dict_pop = dict((sorted((dict_pop | child_pop).items(), key=lambda item: item[1]))[0:population])
        child_pop.clear()
        gen_time = time.perf_counter() - beg
        if check_out(count, min_fitness, gen_time):
            break
    return(gen_time, min_fitness, num_generation)