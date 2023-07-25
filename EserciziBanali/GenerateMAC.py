# Un indirizzo MAC (Media Access Control address) è un indirizzo univoco associato dal produttore,
# a un chipset per comunicazioni wireless (es WiFi o Bluetooth), composto da 6 coppie di cifre
# esadecimali separate da due punti.
# Un esempio di MAC è 02:FF:A5:F2:55:12.
# Scrivi una funzione genera_mac() che generi degli indirizzi MAC pseudo casuali utilizzando il modulo random.
from random import randint, random, choice


def genera_mac():
    mac = ""
    for _ in range(6):
        coppia_cifre = [choice("0123456789ABCDEF") for _ in range(2)]
        mac += ":".join(coppia_cifre)
    return mac[1:]  # Rimuovi il primo ":" dal risultato


def main():
    print("Ecco il tuo MAC ADDRESS:", genera_mac())


if __name__ == '__main__':
    main()
