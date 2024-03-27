import sympy as sp

x = sp.symbols('x')

def calc(a, b, c):

    func = a * x ** 2 + b * x + c
    d = b ** 2 - 4 * a * c
    if d < 0:
        result = sp.solve(func, x)
        print(result[0])
        print(result[1])
    elif d == 0:
        result = sp.solve(func, x)
        print("중근을 갖습니다.")
        print(result)
    else:
        print("근이 존재하지 않습니다.")


if __name__ == "__main__":
    calc(1,2,1)