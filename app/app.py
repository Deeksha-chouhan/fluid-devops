from flask import Flask
import redis
import os

app = Flask(__name__)

r = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=6379
)

@app.route("/")
def home():
    count = r.incr("hits")
    return f"Hello Fluid AI! Visits: {count}"

@app.route("/health")
def health():
    return "OK"

app.run(host="0.0.0.0", port=5000)
