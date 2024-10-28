#Final project task7
'''
Необхідно написати програму на Python, яка імітує велику кількість
кидків кубиків, обчислює суми чисел, які випадають на кубиках,
і визначає ймовірність кожної можливої суми.
'''

import random
# Функція для підрахунку імовірності кидання двох кубиків
def count_probability(num):
    # Створення і ініціалізація нулями словника для підрахунку результатів
    prod_dict = {}
    count = num
    for i in range(2, 13):
        prod_dict[i] = 0
    
    # Рандом для кидків двох кубиків, підрахунок їх суми та запис суми в результуючий словник
    while num > 0:
        temp1 = random.randint(1, 6)
        temp2 = random.randint(1, 6)
        sum = temp1 + temp2

        prod_dict[sum] += 1
        num -= 1
    
    # Підрахунок імовірності та вивід результатів
    for i in range(2,13):
        if prod_dict[i]:
            probability = prod_dict[i]/count
            print(f"Probability of {i} is {probability*100:.2f}%")

count_probability(10000)
