from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

conn_info = "dbname=products user=postgres password=password host=0.0.0.0"
db = psycopg2.connect(conn_info)


@app.route('/brands')
def hello_world():
    cur = db.cursor()
    cur.execute('SELECT brand_id, brand_name FROM brand')
    rows = cur.fetchall()
    cur.close()
    return jsonify([{'brand_id': row[0], 'brand_name': row[1]} for row in rows])
