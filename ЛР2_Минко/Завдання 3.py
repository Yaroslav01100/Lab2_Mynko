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