def sum_func(a: int, b: int) -> int:
    return a + b

def sub_func(a: int, b: int) -> int:
    return a - b

def mul_func(a: int, b: int) -> int:
    return a * b



def main():

    print('Такс, че тут кого, посмотри как робишь? попытка вторая')

    a = int(input('Введите первое число'))
    operator = input('Введите оперпацию')
    b = int(input('Введите второе число'))

    if operator == '+':
        print(sum_func(a, b))
    elif operator == '-':
        print(sum_func(a, b))
    elif operator == '*':
        print(mul_func(a, b))


if __name__ == '__main__':
    main()