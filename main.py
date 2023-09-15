import time

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Пожалуйста, введите целое число.")

def main():
    print("Введите количество яблок.")
    a = get_int_input()
    print(f"У вас {a} яблок.")

    apples = {}

    print("Укажите, какого сорта яблоко по очереди:")
    for _ in range(a):
        type_apple = input()
        while True:
            try:
                price = float(input("Теперь укажите цену за каждое яблоко:"))
                break
            except ValueError:
                print("Пожалуйста, введите число для цены.")

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
