import io
from PIL import Image
from flask import Flask, jsonify, render_template, request
import numpy as np
from sklearn.cluster import KMeans


app = Flask(__name__)


def extract_top_colors(image_bytes, k=10, resize_to=(200, 200)):
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    if resize_to:
        img = img.resize(resize_to)

    pixels = np.array(img).reshape(-1, 3)

    kmeans = KMeans(n_clusters=k, n_init="auto", random_state=42)
    labels = kmeans.fit_predict(pixels)
    centers = kmeans.cluster_centers_.astype(int)

    counts = np.bincount(labels)
    order = np.argsort(counts)[::-1]
    top_colors = centers[order]

    hex_colors = [f"#{r:02X}{g:02X}{b:02X}" for r, g, b in top_colors]
    return hex_colors


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/extract", methods=["POST"])
def extract():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]
    image_bytes = file.read()

    try:
        colors = extract_top_colors(image_bytes, k=10)
        return jsonify({"colors": colors})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
