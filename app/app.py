
from flask import Flask, request, render_template_string
import pymysql
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "mysql")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "rootpass")
DB_NAME = os.getenv("DB_NAME", "fluiddb")

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
<title>Fluid AI DevOps App</title>
<style>
body{font-family:Arial;background:#eef2ff;padding:40px}
.container{max-width:600px;margin:auto;background:white;padding:30px;border-radius:14px;box-shadow:0 4px 18px #999}
h1{text-align:center;color:#1e3a8a}
input,textarea,button{width:100%;padding:12px;margin-top:12px;border-radius:8px;border:1px solid #ccc}
button{background:#2563eb;color:white;font-weight:bold}
.item{padding:10px;border-bottom:1px solid #ddd}
</style>
</head>
<body>
<div class="container">
<h1>Fluid AI DevOps Demo</h1>
<p>This app stores messages in MySQL running in another Kubernetes container.</p>
<form method="POST">
<input type="text" name="name" placeholder="Enter your name" required>
<textarea name="message" placeholder="Enter your message" required></textarea>
<button type="submit">Save to MySQL Database</button>
</form>
<h3>Stored Data from MySQL:</h3>
{% for item in items %}
<div class="item">{{ item[0] }}: {{ item[1] }}</div>
{% endfor %}
</div>
</body>
</html>
"""

def get_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

@app.route("/", methods=["GET", "POST"])
def home():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            message TEXT
        )
    """)

    if request.method == "POST":
        name = request.form["name"]
        message = request.form["message"]
        cursor.execute(
            "INSERT INTO messages (name, message) VALUES (%s, %s)",
            (name, message)
        )
        conn.commit()

    cursor.execute("SELECT name, message FROM messages")
    items = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template_string(HTML_PAGE, items=items)

@app.route("/health")
def health():
    return "OK"

app.run(host="0.0.0.0", port=5000)

