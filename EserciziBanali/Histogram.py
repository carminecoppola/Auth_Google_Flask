# Scrivi una semplice funzione che, data una lista di numeri, fornisca in output un
# istogramma basato su questi numeri, usando asterischi per disegnarlo.
# Data ad esempio la lista [3, 7, 9, 5], la funzione dovrà produrre questa sequenza:
#   ***
#   *******
#   *********
#   *****

from random import randint


def histogram(lista):
    for i in lista:
        print('*' * i)


def main():
    list_num = []

    for i in range(4):
        list_num.append(randint(1, 10))

    print("\nEcco la lista: ", list_num)

    print("\nRappresentazione tramite istogramma:")
    histogram(list_num)


if __name__ == '__main__':
    main()