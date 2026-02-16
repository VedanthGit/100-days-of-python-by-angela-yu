import json
from pathlib import Path
from flask import Flask, jsonify, render_template, request


app = Flask(__name__)
DATA_PATH = Path("data/cafes.json")


def load_cafes():
    if DATA_PATH.exists():
        return json.loads(DATA_PATH.read_text())
    return []


def save_cafes(cafes):
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    DATA_PATH.write_text(json.dumps(cafes, indent=2))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/cafes", methods=["POST"])
def add_cafe():
    payload = request.json
    required = ["name", "city", "has_wifi", "has_power", "seats", "map_url"]
    if not all(k in payload for k in required):
        return jsonify({"error": "Invalid payload"}), 400

    cafes = load_cafes()
    cafes.append(payload)
    save_cafes(cafes)
    return jsonify({"Status": "ok"}), 201


if __name__ == "__main__":
    app.run(debug=True)
