import math

# Завдання 1: Площі прямокутників
def rectangle_area(length, width):
    return length * width

# Введення сторін прямокутників
length1 = float(input("Введіть довжину першого прямокутника: "))
width1 = float(input("Введіть ширину першого прямокутника: "))
length2 = float(input("Введіть довжину другого прямокутника: "))
width2 = float(input("Введіть ширину другого прямокутника: "))
length3 = float(input("Введіть довжину третього прямокутника: "))
width3 = float(input("Введіть ширину третього прямокутника: "))

# Обчислення площ
area1 = rectangle_area(length1, width1)
area2 = rectangle_area(length2, width2)
area3 = rectangle_area(length3, width3)

print("Площа першого прямокутника:", area1)
print("Площа другого прямокутника:", area2)
print("Площа третього прямокутника:", area3)

# Завдання 2: Гіпотенузи прямокутних трикутників
def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

# Введення катетів трикутників
a1 = float(input("Введіть перший катет першого трикутника: "))
b1 = float(input("Введіть другий катет першого трикутника: "))
a2 = float(input("Введіть перший катет другого трикутника: "))
b2 = float(input("Введіть другий катет другого трикутника: "))

# Обчислення гіпотенуз
hyp1 = hypotenuse(a1, b1)
hyp2 = hypotenuse(a2, b2)

print("Гіпотенуза першого трикутника:", hyp1)
print("Гіпотенуза другого трикутника:", hyp2)

if hyp1 > hyp2:
    print("Гіпотенуза першого трикутника більше.")
elif hyp1 < hyp2:
    print("Гіпотенуза другого трикутника більше.")
else:
    print("Гіпотенузи обох трикутників рівні.")

# Завдання 3: Перевірка точок на належність до кола
def is_inside_circle(x, y, a, b, R):
    return (x - a)**2 + (y - b)**2 < R**2

# Введення параметрів кола
a = float(input("Введіть координату a центра кола: "))
b = float(input("Введіть координату b центра кола: "))
R = float(input("Введіть радіус кола: "))

# Введення координат точок
p1 = float(input("Введіть координату x точки P: "))
p2 = float(input("Введіть координату y точки P: "))
f1 = float(input("Введіть координату x точки F: "))
f2 = float(input("Введіть координату y точки F: "))
l1 = float(input("Введіть координату x точки L: "))
l2 = float(input("Введіть координату y точки L: "))

# Перевірка точок
points_inside = 0
points_inside += is_inside_circle(p1, p2, a, b, R)
points_inside += is_inside_circle(f1, f2, a, b, R)
points_inside += is_inside_circle(l1, l2, a, b, R)

print("Кількість точок всередині кола:", points_inside)

# Завдання 4: Площа чотирикутника
def quadrilateral_area(X, Y, Z, T):
    # Площа двох трикутників, на які розбивається чотирикутник прямим кутом
    area1 = 0.5 * X * Y
    area2 = 0.5 * Z * T
    return area1 + area2

# Введення сторін чотирикутника
X = float(input("Введіть довжину сторони X: "))
Y = float(input("Введіть довжину сторони Y: "))
Z = float(input("Введіть довжину сторони Z: "))
T = float(input("Введіть довжину сторони T: "))

# Обчислення площі
area = quadrilateral_area(X, Y, Z, T)
print("Площа чотирикутника:", area)

# Завдання 5: Пошук чисел, що діляться на кожне із заданих
def find_divisible_numbers(n, numbers):
    result = []
    for i in range(1, n+1):
        if all(i % num == 0 for num in numbers):
            result.append(i)
    return result

# Введення числа n та чисел для перевірки
n = int(input("Введіть верхню межу n: "))
numbers = list(map(int, input("Введіть числа для перевірки, розділені пробілами: ").split()))

# Пошук та виведення чисел
divisible_numbers = find_divisible_numbers(n, numbers)
print("Числа, які діляться на кожне із заданих чисел:", divisible_numbers)
