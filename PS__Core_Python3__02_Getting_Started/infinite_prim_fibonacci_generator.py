from math import sqrt


def lucas():
    yield 1
    a = 1
    b = 1
    while True:
        yield b
        a, b = b, a + b


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def main():
    counter = 1
    for x in (p for p in lucas() if is_prime(p)):
        print(f'counter: {counter}, number: {x}')
        print("--------------------------------------------------------")
        counter += 1
        if counter > 20:
            break


# csak akkor fut le ez a metódus, ha ez van main-ként (programként) futtatva.
if __name__ == '__main__':
    main()
