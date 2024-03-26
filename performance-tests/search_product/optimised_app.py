from flask import request, jsonify
from database_manager import Product, app


@app.route('/search', methods=['GET'])
def search_optimized():
    query = request.args.get('query')
    # Utilise une requête SQL pour filtrer les produits
    filtered_products = Product.query.filter(Product.name.ilike(f'%{query}%')).all()
    return jsonify([{'id': product.id, 'name': product.name} for product in filtered_products])


if __name__ == '__main__':
    app.run(debug=True)