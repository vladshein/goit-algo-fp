#Final project task6
'''
Необхідно написати програму на Python, яка використовує два підходи — жадібний алгоритм
та алгоритм динамічного програмування для розв’язання задачі вибору їжі з найбільшою
сумарною калорійністю в межах обмеженого бюджету.

Кожен вид їжі має вказану вартість і калорійність. Дані про їжу представлені у вигляді
словника, де ключ — назва страви, а значення — це словник з вартістю та калорійністю.
'''

def greedy_algorithm(items, budget):
    # Сортуємо страви за співвідношенням калорій до вартості в порядку спадання
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    selected_items = []
    total_cost = 0
    total_calories = 0

    for item, details in sorted_items:
        if total_cost + details['cost'] <= budget:
            selected_items.append(item)
            total_cost += details['cost']
            total_calories += details['calories']
    
    return selected_items, total_cost, total_calories

def dynamic_programming(items, budget):
    # Ініціалізуємо таблицю DP
    dp = [[0 for _ in range(budget + 1)] for _ in range(len(items) + 1)]
    item_list = list(items.items())
    
    for i in range(1, len(item_list) + 1):
        item_name, details = item_list[i - 1]
        cost = details['cost']
        calories = details['calories']
        
        for w in range(1, budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Відновлюємо вибрані страви
    w = budget
    n = len(item_list)
    selected_items = []
    
    while w > 0 and n > 0:
        if dp[n][w] != dp[n - 1][w]:
            item_name, details = item_list[n - 1]
            selected_items.append(item_name)
            w -= details['cost']
        n -= 1
    
    total_calories = dp[len(item_list)][budget]
    total_cost = sum(items[item]['cost'] for item in selected_items)
    
    return selected_items, total_cost, total_calories

# Приклад використання
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
budget = 100

print("Greedy algorithm")
print(greedy_algorithm(items, budget))

print("Dynamic programming")
print(dynamic_programming(items, budget))