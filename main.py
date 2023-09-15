print("Введите количество яблок.")
a = int(input())
apples = [0]*a
print(f"У вас {len(apples)} яблок.")
print("Укажите, какого сорта яблоко по очереди:")
for i in range(0,len(apples)):
    apples[i] = str(input())    

print(apples)