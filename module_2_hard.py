num = int(input("Введите число от 3 до 20: "))
for i in range(1, 21):
    for j in range(1, 21):
        if num % (i + j) == 0 and i < j and i != j:
            print(f"Password: {i} и {j}")
print("Бежим дальше!")
