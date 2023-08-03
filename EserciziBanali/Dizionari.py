# Scrivi una funzione che accetti una lista di dizionari rappresentante una scuola.
# Ogni dizionario rappresenta uno studente e contiene nome, cognome, classe e voti.
# La funzione deve stampare un elenco di tutti gli studenti e calcolare la media
# dei voti di ciascuno.

# Funzione che calcola la media dei voti in una lista di voti.
def mediaVote(voti):
    # Se la lista dei voti è vuota, restituisci 0 per evitare divisione per zero.
    if not voti:
        return 0
    # Calcola la somma dei voti e dividi per il numero di voti per ottenere la media.
    return sum(voti) / len(voti)


# Funzione che analizza la lista di studenti e stampa i loro dati e la media dei voti.
def analyzer_students(lista_studenti):
    # Itera attraverso ogni studente nella lista degli studenti.
    for i in lista_studenti:
        # Estrapola i dati dello studente da ciascun dizionario.
        nome = i.get('nome', '')
        cognome = i.get('cognome', '')
        classe = i.get('classe', '')
        voti = i.get('voti', [])

        # Stampa i dati dello studente (nome, cognome, classe) e i suoi voti.
        print(f"Studente: {cognome} {nome}, Classe: {classe}")
        print(f"Voti: {voti}")

        # Calcola la media dei voti dello studente chiamando la funzione mediaVoti.
        media_voti = mediaVote(voti)
        # Stampa la media dei voti con due decimali.
        print(f"Media voti: {media_voti:.2f}\n")


def main():
    # Esempio di lista di studenti con i loro dati.
    lista_studenti = [
        {
            'nome': 'Mario',
            'cognome': 'Rossi',
            'classe': '5A',
            'voti': [7, 8, 6, 9, 7],
        },
        {
            'nome': 'Giulia',
            'cognome': 'Verdi',
            'classe': '4B',
            'voti': [9, 8, 9, 10, 8],
        },
        {
            'nome': 'Luca',
            'cognome': 'Bianchi',
            'classe': '3C',
            'voti': [6, 7, 8, 7, 6],
        },
    ]

    # Chiamata alla funzione analyzer_students per analizzare e stampare i dati degli studenti.
    analyzer_students(lista_studenti)


# Punto di ingresso dell'applicazione.
if __name__ == '__main__':
    main()
