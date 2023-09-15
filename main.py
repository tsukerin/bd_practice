import time

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Пожалуйста, введите целое число.")

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Пожалуйста, введите число.")

def main():
    print("Введите количество яблок:")
    apple_count = get_int_input()
    print(f"У вас {apple_count} яблок.")

    apples = {}

    print("Укажите, какого сорта яблоко по очереди:")
    for _ in range(apple_count):
        type_apple = input()
        price = get_float_input("Теперь укажите цену за каждое яблоко:")
        apples[type_apple] = price

    print("Информация о ваших яблоках:")
    for type_apple, price in apples.items():
        print(f"Сорт: {type_apple}, Цена: {price}")

    print("Выполняется обработка данных")
    print("Процент завершенности обработки")
    for i in range(1, 101):
        time.sleep(0.25)
        print(f"{i}%", end='\r')  # Используем '\r', чтобы обновлять процент на одной строке.

if __name__ == "__main__":
    main()
