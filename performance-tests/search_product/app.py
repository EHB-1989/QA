from flask import Flask, request, jsonify
from database_manager import Product, app
from flask_sqlalchemy import SQLAlchemy


@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("query")
    # Charge tous les produits en mémoire et filtre en Python
    all_products = Product.query.all()
    filtered_products = [
        product for product in all_products if query.lower() in product.name.lower()
    ]
    return jsonify(
        [{"id": product.id, "name": product.name} for product in filtered_products]
    )


if __name__ == "__main__":
    app.run(debug=True)
