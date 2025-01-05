def banner(message, border="-"):
    line = border * len(message)
    print(line)
    print(message)
    print(line)


def main():
    banner("Norwegian Blue")
    print()
    banner("Sun, Moon and Stars", "*")
    print()
    banner("Stars, Moon and Sun", border="+")
    print()
    banner(border=".", message="Sun, Moon and Stars")


# csak akkor fut le ez a metódus, ha ez van main-ként (programként) futtatva.
if __name__ == '__main__':
    main()
