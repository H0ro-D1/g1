def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b
if __name__ == "__main__":
    print("Калькулятор запущен")
    print("6 + 2 =", add(6, 2))
    print("28 / 4 =", divide(28, 4))
    # test
