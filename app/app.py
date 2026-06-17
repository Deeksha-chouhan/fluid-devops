from flask import Flask, request, render_template_string
import redis
import os

app = Flask(__name__)

r = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=6379,
    decode_responses=True
)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Fluid AI DevOps App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #eef2ff, #dbeafe);
            padding: 40px;
        }
        .container {
            max-width: 600px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 14px;
            box-shadow: 0 4px 18px rgba(0,0,0,0.12);
        }
        h1 {
            color: #1e3a8a;
            text-align: center;
        }
        input, textarea, button {
            width: 100%;
            padding: 12px;
            margin-top: 12px;
            border-radius: 8px;
            border: 1px solid #ccc;
        }
        button {
            background: #2563eb;
            color: white;
            font-weight: bold;
            cursor: pointer;
        }
        .data {
            margin-top: 25px;
            padding: 15px;
            background: #f8fafc;
            border-radius: 8px;
        }
        .item {
            padding: 10px;
            border-bottom: 1px solid #ddd;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Fluid AI DevOps Demo</h1>
        <p>This web app stores user messages in Redis running in another Kubernetes container.</p>

        <form method="POST">
            <input type="text" name="name" placeholder="Enter your name" required>
            <textarea name="message" placeholder="Enter your message" required></textarea>
            <button type="submit">Save to Database</button>
        </form>

        <div class="data">
            <h3>Stored Data from Redis:</h3>
            {% for item in items %}
                <div class="item">{{ item }}</div>
            {% endfor %}
        </div>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        message = request.form["message"]
        r.rpush("messages", f"{name}: {message}")

    items = r.lrange("messages", 0, -1)
    return render_template_string(HTML_PAGE, items=items)

@app.route("/health")
def health():
    return "OK"

app.run(host="0.0.0.0", port=5000)

