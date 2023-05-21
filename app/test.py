from flask import Flask
from flask_mysqldb import MySQL





app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pluto'
app.config['MYSQL_DB'] = 'cchs'
mysql = MySQL(app)

@app.route('/test')
def test():

    cur = mysql.connection.cursor()
    cur.callproc('register_student', 
                         ['Dami', 'Lola', '2000-01-15', '-O', 'AA', 'Islam', 'Obada',
                           '08050771951', 'Hausa', 'Obada', 'koko', 1])
    mysql.connection.commit()
    cur.close()
    return 'Data inserted'

if __name__ == '__main__':
    app.run(debug=True)
