from flask import Flask
import sys 

app = Flask(__name__)

fdata = "ashi"

@app.route("/info")
def lw():
    return f"welcome to myapp {from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)


ip="172.17.0.2"
user="ashik"
password="redhat"
dbname="awdb"

app.config['MYSQL_DATABASE_USER'] = user
app.config['MYSQL_DATABASE_HOST'] = ip
app.config['MYSQL_DATABASE_PASSWORD'] = password
app.config['MYSQL_DATABASE_DB'] = dbname

mysql = MySQL()
mysql.init_app(app)

@app.route("/data")
def awdata():
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("select * from students")
        data = cursor.fetchall()
        return str(data)

app.run(host='0.0.0.0')fdata}"

if __name__ == "__main__":
    app.run(host = '0.0.0.0')

