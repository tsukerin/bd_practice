import time

def calculate_total_cost(apples):
    total_cost = 0
    for price in apples.values():
        total_cost += int(price)
    return total_cost

print("Введите количество яблок.")
a = int(input())
print(f"У вас {a} яблок.")

apples = dict()

print("Укажите, какого сорта яблоко по очереди:")
for i in range(0, a):
    type_apple = input()
    print("Теперь укажите цену за каждое яблоко.")
    price = input()
    apples[type_apple] = price

print("Информация о ваших яблоках:")
for type_apple, price in apples.items():
    print(f"Сорт: {type_apple}, Цена: {price}")

total_cost = calculate_total_cost(apples)
print(f"Общая стоимость яблок: {total_cost}")

print("Ваш комп взломали: ")
print("Процент загруженных данных")
for i in range(1, 101):
    time.sleep(0.25)
    print(f"{i}%")
