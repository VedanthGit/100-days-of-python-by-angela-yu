from pathlib import Path
from uuid import uuid4
from flask import Flask, jsonify, render_template, request
import json

app = Flask(__name__)
DATA_PATH = Path("data/todos.json")

if not DATA_PATH.exists():
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    DATA_PATH.write_text("[]")


def load_todos():
    if not DATA_PATH.exists():
        return []

    try:
        raw = DATA_PATH.read_text().strip()
        if not raw:
            return []
        return json.loads(raw)
    except json.JSONDecodeError:
        # Auto-heal corrupted file instead of crashing the API
        return []


def save_todos(todos):
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    DATA_PATH.write_text(json.dumps(todos, indent=2))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/todos", methods=["GET"])
def get_todos():
    return jsonify(load_todos())


@app.route("/api/todos", methods=["POST"])
def create_todo():
    payload = request.json
    title = payload.get("title", "").strip()
    if not title:
        return jsonify({"error": "Title required"}), 400

    todos = load_todos()
    todo = {"id": str(uuid4()), "title": title, "completed": False}
    todos.append(todo)
    save_todos(todos)
    return jsonify(todo), 201


@app.route("/api/todos/<todo_id>", methods=["PATCH"])
def toggle_todo(todo_id):
    todos = load_todos()
    for t in todos:
        if t["id"] == todo_id:
            t["completed"] = not t["completed"]
            save_todos(todos)
            return jsonify(t)
    return jsonify({"error": "Not found"}), 404


@app.route("/api/todos/<todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    todos = load_todos()
    new_todos = [t for t in todos if t["id"] != todo_id]
    if len(new_todos) == len(todos):
        return jsonify({"error": "Not found"}), 404
    save_todos(new_todos)
    return jsonify({"status": "deleted"}), 200


if __name__ == "__main__":
    app.run(debug=True)
