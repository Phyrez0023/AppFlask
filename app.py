from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necesario para manejar sesiones

# Usuarios simulados
users = {'Marcos2000': 'tigre12', 'Marcos2001': 'tigre13'}

@app.route('/')
def home():
    # Si el usuario ya está autenticado, redirigirlo a la página de bienvenida
    if 'username' in session:
        return redirect(url_for('welcome'))
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Verificar si las credenciales son válidas
    if username in users and users[username] == password:
        session['username'] = username
        return redirect(url_for('welcome'))
    else:
        return "Nombre de usuario o contraseña incorrectos. Inténtalo de nuevo."

@app.route('/welcome')
def welcome():
    if 'username' in session:
        username = session['username']
        return render_template('welcome.html', username=username)
    else:
        return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
