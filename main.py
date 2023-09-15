import time

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

for type_apple, price in apples.items():
    print(f"Сорт яблока: {type_apple}, Цена: {price}")

print("Ваш комп взломали: ")
print("Процент загруженных данных")
for i in range(1, 101):
    time.sleep(0.25)
    print(f"{i}%")