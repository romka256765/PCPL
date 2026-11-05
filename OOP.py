import sys
import math


class CoeffRead:
    """Класс для получения коэффициентов."""

    def __init__(self, argv):
        self._argv = argv

    def read(self, name, index):
        if len(self._argv) > index:
            try:
                return float(self._argv[index])
            except ValueError:
                print(f"Некорректное значение {name} в командной строке, "
                      f"введите с клавиатуры")
        while True:
            try:
                return float(input(f"Введите коэффициент {name}: "))
            except ValueError:
                print("Ошибка: введите действительное число")


class Biquad:
    """Класс биквадратного уравнения."""

    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def Discr(self):
        return self.b * self.b - 4 * self.a * self.c

    def solve(self):
        """Возвращает список действительных корней."""
        a, b, c = self.a, self.b, self.c

        D = self.Discr()
        print(f"Дискриминант D = {D}")

        if D < 0:
            return []

        roots = set()
        if D == 0:
            t = -b / (2 * a)
            if t >= 0:
                r = math.sqrt(t)
                roots.update({round(-r, 10), round(r, 10)})
        else:
            sq = math.sqrt(D)
            for t in ((-b + sq) / (2 * a), (-b - sq) / (2 * a)):
                if t >= 0:
                    r = math.sqrt(t)
                    roots.update({round(-r, 10), round(r, 10)})
        return sorted(x + 0.0 for x in roots)

    def __str__(self):
        return f"{self.a}*x^4 + {self.b}*x^2 + {self.c} = 0"


class App:
    def __init__(self, argv):
        self._reader = CoeffRead(argv)

    def run(self):
        a = self._reader.read("A", 1)
        while a == 0:
            a = self._reader.read("A", 1)
        b = self._reader.read("B", 2)
        c = self._reader.read("C", 3)

        eq = Biquad(a, b, c)
        print(f"Уравнение: {eq}")

        roots = eq.solve()
        if not roots:
            print("Действительных корней нет")
        else:
            print("Действительные корни:")
            for r in roots:
                print(f"  x = {r}")


if __name__ == "__main__":
    App(sys.argv).run()
