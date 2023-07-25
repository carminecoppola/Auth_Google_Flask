# Scrivi un programma che chieda all'utente una lista di numeri e fornisca in output il maggiore tra tutti.

from random import randint


def main():
    lista = []

    for i in range(3):
        lista.append(randint(1, 100))

    print("List: ")
    for i in lista:
        print(i)

    print("Max Element is: ", max(lista))
    print("Min Element is: ", min(lista))


if __name__ == "__main__":
    main()
