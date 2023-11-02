import os.path
import pathlib

import cachecontrol
import google
from flask import Flask, session, abort, redirect, request
from google.auth.transport.requests import Request
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
import requests

# Creazione dell'app Flask
app = Flask("Google Login App")
app.secret_key = "CodeSpecialist.com"

# Impostazione di un ambiente di trasporto non sicuro per scopi di sviluppo
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

# ID del client Google OAuth (Assicurati che questo valore corrisponda alle tue credenziali OAuth)
GOOGLE_CLIENT_ID = "374607879800-i650u9di0huvkvp0oh85nbohavlm53gi.apps.googleusercontent.com"

# Percorso al file delle segrete del client (Assicurati che questo file esista e contenga le credenziali OAuth)
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

# Configurazione dell'oggetto Flow per l'autenticazione OAuth
flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email",
            "openid"],
    redirect_uri="http://127.0.0.1:5000/callback"
)


# Decoratore per verificare se l'utente è autenticato
def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)  # Autorizzazione richiesta
        else:
            return function()

    return wrapper


# Pagina di accesso
@app.route('/login')
def login():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)


# Callback dopo l'autenticazione Google
@app.route('/callback')
def callback():
    flow.fetch_token(authorization_response=request.url)

    if not session['state'] == request.args['state']:
        abort(500)  # Stato non corrispondente

    credentials = flow.credentials
    request_session = requests.Session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials.id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )

    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    return redirect("/protected_area")


# Pagina di logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")


# Pagina iniziale
@app.route('/')
def index():
    return "Hello World <a href='/login'> <button> Login </button> </a>"


# Pagina protetta che richiede l'autenticazione
@app.route('/protected_area')
@login_is_required
def protected_area():
    return "Area Protetta <a href='/logout'> <button> Logout </button> </a>"


# Esecuzione dell'app Flask
if __name__ == '__main__':
    app.run(debug=True)
