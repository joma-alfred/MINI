from flask import Flask, request, jsonify
import requests
import mysql.connector
import os

app = Flask(__name__)

db_config = {
    "host": "mysql",
    "user": "root",
    "password": "password",
    "database": "dbname"
}
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

@app.route('/users', methods=['GET'])
def get_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return jsonify(users)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    service_url = os.getenv("SERVICE_URL", "http://service:8000")
    response = requests.post(f"{service_url}/predict", json=data)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
