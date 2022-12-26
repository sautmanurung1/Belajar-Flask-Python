from flask import Flask, render_template, url_for, redirect, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# config database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Sautmanurung234'
app.config['MYSQL_DB'] = 'belajarflask'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def dashboard():
    return render_template('logins.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('dosen'))
    return render_template('login.html')

@app.route('/dosen')
def dosen():
    return render_template('dosen.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)