a1 = float(input("Введіть довжину першої сторони першого прямокутника: "))
b1 = float(input("Введіть довжину другої сторони першого прямокутника: "))
a2 = float(input("Введіть довжину першої сторони другого прямокутника: "))
b2 = float(input("Введіть довжину другої сторони другого прямокутника: "))
a3 = float(input("Введіть довжину першої сторони третього прямокутника: "))
b3 = float(input("Введіть довжину другої сторони третього прямокутника: "))
area1 = a1 * b1
area2 = a2 * b2
area3 = a3 * b3
print("Площа першого прямокутника:", area1)
print("Площа другого прямокутника:", area2)
print("Площа третього прямокутника:", area3)
import math
def hypotenuse_length(a, b):
  return math.sqrt(a**2 + b**2)
a1 = float(input("Введіть довжину першого катета першого трикутника: "))
b1 = float(input("Введіть довжину другого катета першого трикутника: "))
a2 = float(input("Введіть довжину першого катета другого трикутника: "))
b2 = float(input("Введіть довжину другого катета другого трикутника: "))
hypotenuse1 = hypotenuse_length(a1, b1)
hypotenuse2 = hypotenuse_length(a2, b2)
print("Гіпотенуза першого трикутника:", hypotenuse1)
print("Гіпотенуза другого трикутника:", hypotenuse2)
if hypotenuse1 > hypotenuse2:
  print("Гіпотенуза першого трикутника більша.")
elif hypotenuse1 < hypotenuse2:
  print("Гіпотенуза другого трикутника більша.")
else:
  print("Гіпотенузи рівні.")
def is_inside_circle(x, y, a, b, R):
  return (x - a)**2 + (y - b)**2 < R**2
a = float(input("Введіть координату x центру кола (a): "))
b = float(input("Введіть координату y центру кола (b): "))
R = float(input("Введіть радіус кола (R): "))
p1 = float(input("Введіть координату x точки P (p1): "))
p2 = float(input("Введіть координату y точки P (p2): "))
f1 = float(input("Введіть координату x точки F (f1): "))
f2 = float(input("Введіть координату y точки F (f2): "))
l1 = float(input("Введіть координату x точки L (l1): "))
l2 = float(input("Введіть координату y точки L (l2): "))
count_inside = 0
if is_inside_circle(p1, p2, a, b, R):
  count_inside += 1
if is_inside_circle(f1, f2, a, b, R):
  count_inside += 1
if is_inside_circle(l1, l2, a, b, R):
  count_inside += 1
print("Кількість точок всередині кола:", count_inside)
import math
def calculate_quadrilateral_area(X, Y, Z, T):
  diagonal = math.sqrt(X**2 + Y**2)
  area1 = 0.5 * X * Y
  p = (diagonal + Z + T) / 2  # півпериметр
  area2 = math.sqrt(p * (p - diagonal) * (p - Z) * (p - T))
  return area1 + area2
X = float(input("Введіть довжину сторони X: "))
Y = float(input("Введіть довжину сторони Y: "))
Z = float(input("Введіть довжину сторони Z: "))
T = float(input("Введіть довжину сторони T: "))
area = calculate_quadrilateral_area(X, Y, Z, T)
print("Площа чотирикутника:", area)
def find_divisible_numbers(n, divisors):
  result = []
  for i in range(1, n + 1):
    is_divisible = True
    for divisor in divisors:
      if i % divisor != 0:
        is_divisible = False
        break
    if is_divisible:
      result.append(i)
  return result
n = int(input("Введіть натуральне число n: "))
divisors = []
while True:
  try:
    divisor = int(input("Введіть дільник (або 0, щоб завершити введення): "))
    if divisor == 0:
      break
    divisors.append(divisor)
  except ValueError:
    print("Невірний формат числа. Спробуйте ще раз.")
numbers = find_divisible_numbers(n, divisors)
print("Числа, що діляться на всі введені дільники:", numbers)