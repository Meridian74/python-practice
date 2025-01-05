import time


def show_default(arg=time.ctime()):
    print(arg)


def main():
    show_default()


# csak akkor fut le ez a metódus, ha ez van main-ként (programként) futtatva.
if __name__ == '__main__':
    main()
