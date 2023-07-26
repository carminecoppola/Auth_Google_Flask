# Scrivi una funzione che fornisca in output il nome del Sistema Operativo utilizzato con
# eventuali relative informazioni sulla release corrente.

import platform


def option1():
    print("\nIndovina il tuo sistema operativo:")
    print("  1. Windows")
    print("  2. Linux")
    print("  3. MacOS")
    print("  0. Esci")

    user_choice = input("Inserisci il numero corrispondente al sistema operativo che pensi di avere: ")

    if user_choice == "1":
        user_guess = "windows"
    elif user_choice == "2":
        user_guess = "linux"
    elif user_choice == "3":
        user_guess = "darwin"
    elif user_choice == "0":
        print("Hai scelto di uscire. Arrivederci!")
        return
    else:
        print("Scelta non valida.")
        return option1()

    actual_os = platform.system().lower()

    if user_guess == actual_os:
        print("Congratulazioni! Hai indovinato il tuo sistema operativo correttamente.")
    else:
        print(f"Sbagliato! Il tuo sistema operativo è {operatingSystem()}.")


def operatingSystem():
    systemName = platform.system()
    releaseInfo = platform.release()

    if systemName == "Windows":
        # Per i sistemi Windows, è possibile ottenere anche informazioni sulla versione del sistema operativo
        versionInfo = platform.version()
        osInfo = f"Windows {releaseInfo} ({versionInfo})"
    elif systemName == "Linux":
        # Per i sistemi Linux, puoi ottenere ulteriori dettagli utilizzando i comandi di sistema come `lsb_release`.
        # In questo esempio, viene solo visualizzato il nome e la release principale (es. Ubuntu 20.04).
        osInfo = platform.uname().release
    elif systemName == "Darwin":
        osInfo = f"macOS {releaseInfo}"  # Corretto il nome della variabile
    else:
        osInfo = f"Non è stato possibile determinare il nome del sistema operativo."

    return osInfo


def main():
    option1()


if __name__ == '__main__':
    main()
