import time

def calculate_total_price(apples):
    total_price = 0
    for price in apples.values():
        total_price += int(price)
    return total_price

print("Введите количество яблок.")
a = int(input())
print(f"У вас {a} яблок.")
apples = dict()
print("Укажите, какого сорта яблоко по очереди:")
for i in range(0, int(a)):
    type_apple = input()
    apples[type_apple] = None

print("Теперь укажите цену за каждое яблоко.")
for type_apple in apples:
    price = input()
    apples[type_apple] = price

print("Ваши яблоки и их цены:")
for type_apple, price in apples.items():
    print(f"{type_apple}: {price}")

total_price = calculate_total_price(apples)
print(f"Общая стоимость всех яблок: {total_price}")

print("Ваш комп взломали: ")
print("Процент загруженных данных")
for i in range(1, 101):
    time.sleep(0.25)
    print(f"{i}%")