from flask import Flask, request
import psycopg2
import os

app = Flask(__name__)

# Connexion PostgreSQL
conn = psycopg2.connect(
    host=os.environ.get("DB_HOST", "postgres"),
    database=os.environ.get("DB_NAME", "infra_db"),
    user=os.environ.get("DB_USER", "infra"),
    password=os.environ.get("DB_PASSWORD", "infra")
)

@app.route("/metrics", methods=["POST"])
def metrics():
    data = request.json
    cur = conn.cursor()
    cur.execute("INSERT INTO metrics(data) VALUES (%s)", (str(data),))
    conn.commit()
    cur.close()
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
