price = int(input("Введите цену тетради: "))
count = int(input("Введите количество тетрадей: "))
paid = int(input("Введите внесенную сумму: "))

cost = price * count
change = paid - cost

print(f"Стоимость: {cost}")
print(f"Сдача: {change}")
