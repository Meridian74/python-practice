

def main():
    t = [6, 372, 8862, 14880, 2096886]
    for p in enumerate(t):
        print(p)

    for i, v in enumerate(t):
        print(f'index:{i}, value: {v}')


# csak akkor fut le ez a metódus, ha ez van main-ként (programként) futtatva.
if __name__ == '__main__':
    main()
