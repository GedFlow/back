from flask import Flask
from flask_cors import CORS
import pymysql
import os

app = Flask(__name__)
CORS(app)
# cors = CORS(app, resources={r"/*": {"origins": "*"}})

server = os.environ['DB_SERVER']
dbport = os.environ['DB_PORT']
dbuser = os.environ['DB_USER']
dbname = os.environ['DB_NAME']
dbpass = os.environ['MYSQL_ROOT_PASSWORD']


db = pymysql.connect(host=server,
                     port=int(dbport),
                     user=dbuser,
                     passwd=dbpass,
                     db=dbname,
                     charset='utf8')

cursor = db.cursor()

@app.route("/hello")
def hello():
    sql = """SELECT * FROM test"""
    cursor.execute(sql)
    dbResult = cursor.fetchall()
    result = {"code": 200, "message": dbResult}

    return result

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001)


