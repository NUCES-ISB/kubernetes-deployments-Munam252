from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def connect_db():
    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host="postgres-service",
        port="5432"
    )
    return conn

@app.route("/")
def index():
    return "Flask App Running with PostgreSQL!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
