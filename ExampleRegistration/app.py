from flask import request, render_template, redirect, url_for


uri = "mongodb+srv://miniello:pericle@cluster0.1lorjnu.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.DBUtenti
coll = db.utenti

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Salva i dati nel database MongoDB
        db.users.insert_one({"username": username, "password": password})
        return redirect(url_for('login'))
    return render_template('register.html')
