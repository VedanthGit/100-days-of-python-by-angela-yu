import os
from flask import Flask, render_template, request, jsonify
import stripe
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
DOMAIN = os.getenv("DOMAIN", "http://127.0.0.1:5000")

PRODUCTS = [
    {
        "id": "p1",
        "name": "T-Shirt",
        "price": 1999,
        "image": "https://picsum.photos/300?1",
    },
    {
        "id": "p2",
        "name": "Hoodie",
        "price": 3999,
        "image": "https://picsum.photos/300?2",
    },
    {"id": "p3", "name": "Cap", "price": 1499, "image": "https://picsum.photos/300?3"},
]


@app.route("/")
def home():
    return render_template(
        "index.html",
        products=PRODUCTS,
        publishable_key=os.getenv("STRIPE_PUBLISHABLE_KEY"),
    )


@app.route("/create-checkout-session", methods=["POST"])
def create_checkout_session():
    data = request.json
    cart = data.get("cart", [])

    line_items = []
    for item in cart:
        product = next(p for p in PRODUCTS if p["id"] == item["id"])
        line_items.append(
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {"name": product["name"]},
                    "unit_amount": product["price"],
                },
                "quantity": item["qty"],
            }
        )

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=line_items,
        mode="payment",
        success_url=DOMAIN + "/success",
        cancel_url=DOMAIN + "/cancel",
    )

    return jsonify({"url": session.url})


@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/cancel")
def cancel():
    return render_template("cancel.html")


if __name__ == "__main__":
    app.run(debug=True)
