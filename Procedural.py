import sys
import math


def get_coef(name, index):
    """Читает коэффициент: сначала из argv, иначе с клавиатуры (с повтором)."""
    if len(sys.argv) > index:
        try:
            return sys.argv[index]
        except ValueError:
            print(f"Некорректное значение {name} в командной строке, "
                  f"введите с клавиатуры")
    while True:
        try:
            return input(f"Введите коэффициент {name}: ")
        except ValueError:
            print("Ошибка: введите действительное число")


def solve_biquad(a, b, c):
    """Возвращает список действительных корней или None, если решений бесконечно много."""
    # Решаем A*t^2 + B*t + C = 0
    while a == 0:
        a = get_coef('A', 1)

    D = b * b - 4 * a * c
    print(f"Дискриминант D = {D}")

    if D < 0:
        return []

    roots = set()
    if D == 0:
        t = -b / (2 * a)
        if t >= 0:
            r = math.sqrt(t)
            roots.add(round(-r, 10))
            roots.add(round(r, 10))
    else:
        sq = math.sqrt(D)
        for t in ((-b + sq) / (2 * a), (-b - sq) / (2 * a)):
            if t >= 0:
                r = math.sqrt(t)
                roots.add(round(r, 10))
                roots.add(round(-r, 10))

    return sorted(x + 0.0 for x in roots)


def main():
    a = float(get_coef("A", 1))
    b = float(get_coef("B", 2))
    c = float(get_coef("C", 3))
    print(f"Уравнение: {a}*x^4 + {b}*x^2 + {c} = 0")

    roots = solve_biquad(a, b, c)

    if roots is None:
        print("Бесконечно много решений (A = B = C = 0)")
    elif not roots:
        print("Действительных корней нет")
    else:
        print("Действительные корни:")
        for r in roots:
            print(f"  x = {r}")


if __name__ == "__main__":
    main()
