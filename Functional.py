import sys
import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Coef:
    a: float
    b: float
    c: float


def read_coef(name, index):
    if len(sys.argv) > index:
        try:
            return float(sys.argv[index])
        except ValueError:
            print(f"Некорректное значение {name} в командной строке, "
                  f"введите с клавиатуры")
    while True:
        try:
            return float(input(f"Введите коэффициент {name}: "))
        except ValueError:
            print("Ошибка: введите действительное число")


def _sqrt_pair(t):
    """Корни x^2 = t (при t >= 0)."""
    r = math.sqrt(t)
    return {round(-r, 10), round(r, 10)}


def solve(coeffs: Coef):
    match coeffs:
        # A ≠ 0 — квадратное относительно t
        case Coef(a=a, b=b, c=c):
            D = b * b - 4 * a * c
            print(f"Дискриминант D = {D}")
            match D:
                case _ if D < 0:
                    return ("none", None)
                case 0:
                    t = -b / (2 * a)
                    if t < 0:
                        return ("none", None)
                    return ("roots", sorted(_sqrt_pair(t)))
                case _:
                    sq = math.sqrt(D)
                    ts = ((-b + sq) / (2 * a), (-b - sq) / (2 * a))
                    roots = set()
                    for t in ts:
                        if t >= 0:
                            roots |= _sqrt_pair(t)
                    if not roots:
                        return ("none", None)
                    return ("roots", sorted(x + 0.0 for x in roots))


def main():
    coeffs = Coef(
        read_coef("A", 1),
        read_coef("B", 2),
        read_coef("C", 3),
    )
    while coeffs.a == 0:
        coeffs = Coef(
        read_coef("A", 1),
        read_coef("B", 2),
        read_coef("C", 3),
    )
    print(f"Уравнение: {coeffs.a}*x^4 + {coeffs.b}*x^2 + {coeffs.c} = 0")

    match solve(coeffs):
        case ("none", _):
            print("Действительных корней нет")
        case ("roots", roots):
            print("Действительные корни:")
            for r in roots:
                print(f"  x = {r}")


if __name__ == "__main__":
    main()
