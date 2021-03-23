def sum_func(a: int, b: int) -> int:
    return a + b



def main():

    a = int(input('Введите первое число'))
    operator = input('Введите оперпацию')
    b = int(input('Введите второе число'))

    if operator == '+':
        print(sum_func(a, b))

if __name__ == '__main__':
    main()