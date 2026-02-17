from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

BASE_API = "https://api.openbrewerydb.org/v1/breweries/search"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/search")
def search_api():
    q = request.args.get("q", "").strip()
    if not q:
        return jsonify([])

    try:
        res = requests.get(
            BASE_API,
            params={"query": q, "per_page": 50},
            timeout=10,
            headers={"User-Agent": "BreweryFinder/1.0"},
        )
        res.raise_for_status()
        return jsonify(res.json())
    except requests.RequestException as e:
        # Log the upstream error for debugging
        print("[ERROR] Open Brewery DB API failed:", e)
        return jsonify({"error": "Upstream API error"}), 502


if __name__ == "__main__":
    app.run(debug=True)
