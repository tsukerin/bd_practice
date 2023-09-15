print("Введите количество яблок.")
a = int(input())
print(f"У вас {a} яблок.")
apples = dict()
print("Укажите, какого сорта яблоко по очереди:")
for i in range(0,int(a)):
    type_apple = input()    

print("Теперь укажите цену за каждое яблоко.")
for i in range(0,int(a)):
    price = input()

apples[type_apple] = price

for apples in type_apple, price:
    print(apples)