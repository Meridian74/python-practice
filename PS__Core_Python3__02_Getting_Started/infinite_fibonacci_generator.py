def lucas():
    yield 1
    a = 1
    b = 1
    while True:
        yield b
        a, b = b, a + b


def main():
    counter = 1
    for x in lucas():
        print(f'counter: {counter}, number: {x}')
        print("--------------------------------------------------------")
        counter += 1
        if counter > 200:
            break


# csak akkor fut le ez a metódus, ha ez van main-ként (programként) futtatva.
if __name__ == '__main__':
    main()
