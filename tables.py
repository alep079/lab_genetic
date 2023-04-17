import pandas as pd

A_MAX = 2**20
LENGTH = 24

# генерация таблицы векторов
def vectors_table_gen(vectors):
    df = pd.DataFrame ({
    'Номер вектора' : [i+1 for i in range (50)],
    'Вектор' : vectors,
    'Amax' : [str(A_MAX) for _ in range (50)]
    })
    df.to_excel('Вектора.xlsx', index=False)

# генерация таблицы рюкзачных задач
def tasks_table_gen(backpacks):
    df = pd.DataFrame ({
    'Номер задачи' : [i+1 for i in range (500)],
    'Номер вектора' : [(i//10) + 1 for i in range (500)],
    'Целевой вес' : [backpacks[i][0] for i in range (500)],
    'Доля предметов' : [backpacks[i][1] for i in range (500)]
    })
    df.to_excel('Задачи.xlsx', index=False)

# генерация таблицы решений задач полным перебором
def full_en_table_sol(full_en_sol):
    df = pd.DataFrame ({
    'Номер задачи' : [i+1 for i in range (500)],
    'Время нахождения первого решения' : [full_en_sol[i][0] for i in range (500)],
    'Время нахождения всех решений' : [full_en_sol[i][1] for i in range (500)],
    'Число решений' : [full_en_sol[i][2] for i in range (500)]
    })
    for i in range (500):
        pass
    df.to_excel('Решения_перебор.xlsx', index=False)

# генерация таблицы решений задач генетическим алгоритмом
def gen_table_sol(genetic_sol):
    df = pd.DataFrame ({
    'Номер задачи' : [i+1 for i in range (500)],
    'Время работы алгоритма' : [genetic_sol[i][0] for i in range (500)],
    'Достигнутый минимум фитнесс-функции' : [genetic_sol[i][1] for i in range (500)],
    'Причина остановки алгоритма' : ['' for i in range (500)],
    'Номер последнего поколения' : [genetic_sol[i][2] for i in range (500)]
    })
    for i in range (500):
        if df['Достигнутый минимум фитнесс-функции'][i] == 0:
            df['Причина остановки алгоритма'][i] = 'Фитнесс функция'
        elif df['Время работы алгоритма'][i] > 10:
            df['Причина остановки алгоритма'][i] = 'Превышено время'
        else:
            df['Причина остановки алгоритма'][i] = 'Неизменяемость поколений'
    df.to_excel('Решения_ген_алг_02.xlsx', index=False)