import math

total_students = int(input("Количество студентов: "))
bus_capacity = int(input("Мест в автобусе: "))

full_buses = total_students // bus_capacity
remainder = total_students % bus_capacity

if total_students == 0:
    total_buses = 0
else:
    total_buses = (total_students + bus_capacity - 1) // bus_capacity

radius = float(input("Введите радиус для дополнительных расчетов: "))
circle_length = 2 * math.pi * radius
circle_area = math.pi * (radius ** 2)

print()
print(f"Полностью заполненных автобусов: {full_buses}")
print(f"Остаток студентов: {remainder}")
print(f"Минимальное число автобусов: {total_buses}")
print(f"Длина окружности: {circle_length:.2f}")
print(f"Площадь круга: {circle_area:.2f}")
