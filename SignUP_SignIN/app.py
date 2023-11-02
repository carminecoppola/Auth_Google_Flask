# Import necessari
from flask import Flask, request, render_template, redirect, url_for, session
from pymongo import MongoClient
import secrets  # Importa il modulo secrets per generare una chiave segreta per le sessioni

# Inizializza un'applicazione Flask
app = Flask(__name__)

# Imposta una chiave segreta per le sessioni
app.secret_key = secrets.token_hex(16)

# URI per la connessione a MongoDB
uri = "mongodb+srv://miniello:pericle@cluster0.1lorjnu.mongodb.net/?retryWrites=true&w=majority"

# Crea un nuovo client MongoDB e connettiti al server MongoDB
client = MongoClient(uri)

# Invia un ping per confermare una connessione riuscita al server MongoDB
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Seleziona il database 'utenti' e la collezione 'utenti' nel database
db = client['utenti']
collection = db['utenti']


# Pagina di registrazione
@app.route('/registrazione', methods=['GET', 'POST'])
def registrazione():
    if request.method == 'POST':
        # Ottieni i dati del modulo di registrazione
        username = request.form['username']
        password = request.form['password']

        # Verifica se l'utente esiste già nel database
        if collection.find_one({'username': username}):
            return 'Questo nome utente esiste già. Scegli un altro nome utente.'

        # Inserisci l'utente nel database
        new_user = {'username': username, 'password': password}
        collection.insert_one(new_user)

        return 'Registrazione avvenuta con successo! <a href="/">Torna alla pagina principale</a>'

    return render_template('registrazione.html')


# Pagina di login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Ottieni il nome utente e la password inviati dal modulo di login
        username = request.form['username']
        password = request.form['password']

        # Cerca un utente nel database con il nome utente e la password forniti
        user = collection.find_one({'username': username, 'password': password})

        if user:
            # Login riuscito, crea una sessione e memorizza il nome utente
            session['username'] = username
            return 'Login riuscito! Benvenuto, {}! <a href="/">Torna alla pagina principale</a>'.format(username)
        else:
            return 'Credenziali errate. Riprova o <a href="/registrazione">registrati</a>.'

    return render_template('login.html')


# Pagina principale
@app.route('/')
def index():
    if 'username' in session:
        return 'Sei loggato come ' + session['username'] + '. <a href="/logout">Esci</a>'
    return 'Benvenuto! <a href="/login">Accedi</a> o <a href="/registrazione">registrati</a>.'


# Pagina di logout
@app.route('/logout')
def logout():
    # Rimuovi il nome utente dalla sessione (effettua il logout)
    session.pop('username', None)
    return 'Sei stato disconnesso. <a href="/">Torna alla pagina principale</a>'


# Avvia l'applicazione Flask in modalità di debug
if __name__ == '__main__':
    app.run(debug=True)
