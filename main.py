import time

print("Введите количество яблок.")
a = int(input())
print(f"У вас {a} яблок.")

apples = {}

print("Укажите, какого сорта яблоко по очереди:")
for _ in range(a):
    type_apple = input()
    print("Теперь укажите цену за каждое яблоко.")
    price = input()
    apples[type_apple] = price

print("Информация о ваших яблоках:")
for type_apple, price in apples.items():
    print(f"Сорт: {type_apple}, Цена: {price}")

print("Выполняется обработка данных")
print("Процент завершенности обработки")
for i in range(1, 101):
    time.sleep(0.25)
    print(f"{i}%")
