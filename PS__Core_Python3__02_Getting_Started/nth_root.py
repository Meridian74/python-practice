import math


def nth_root(radicand, n):
    return radicand ** (1 / n)


def ordinal_suffix(value):
    s = str(value)
    if s.endswith('11') or s.endswith('12' or s.endswith('13')):
        return 'th'
    if s.endswith('1'):
        return 'st'
    if s.endswith('2'):
        return 'nd'
    if s.endswith('3'):
        return 'rd'
    return 'th'


def ordinal(value):
    return str(value) + ordinal_suffix(value)


def display_nth_root(radicand, n):
    root = nth_root(radicand, n)
    message = 'The ' + ordinal(n) + ' root of ' + str(radicand) + ' is ' + str(root)
    print(message)


def main():
    base_num = int(input("Give a number: "))
    n = int(input("Give ordinal root value: "))
    display_nth_root(base_num, n)


# csak akkor fut le ez a metódus, ha ez van main-ként (programként) futtatva.
if __name__ == '__main__':
    main()
