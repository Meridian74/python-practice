def wrong_add_spam(menu=[]):
    menu.append("spam")
    return menu


def add_spam(menu=None):
    if menu is None:
        menu = []
    menu.append('spam')
    return menu


def main():
    print("Wrong function default value declaration:")
    menu = wrong_add_spam()
    print(menu)
    menu = wrong_add_spam()
    print(menu)
    print("-------------------------------------------")
    print("Correct function default value declaration:")
    menu = add_spam()
    print(menu)
    menu = add_spam()
    print(menu)
    breakfast = ['bacon', 'eggs']
    breakfast = add_spam(breakfast)
    print(breakfast)


# csak akkor fut le ez a metódus, ha ez van main-ként (programként) futtatva.
if __name__ == '__main__':
    main()
