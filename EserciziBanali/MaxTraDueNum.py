# Scrivi un programma che chieda per 5 volte  due numeri all'utente tramite la funzione
# input e mostri il più grande tra i due utilizzando la funzione print.
# Per quanto Python disponga di una funzione max(), siete invitati ad utilizzare
# le istruzioni istruzioni if, elif ed else per la scrittura dell algoritmo.

def main():
    try:
        for i in range(5):
            num1 = int(input("Inserisci il primo numero:"))
            num2 = int(input("Inserisci il secondo numero:"))

            if num1 > num2:
                print("Il primo numero è più grande", num1)
            elif num2 > num1:
                print("Il secondo numero è il piu grande",num2)
            else:
                print("I due numeri sono uguali")
    except ValueError:
        print("Hai inserito un valore non valido. Assicurati di inserire numeri.")


if __name__ == "__main__":
    main()