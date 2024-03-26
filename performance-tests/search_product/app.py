from flask import request, jsonify
from database_manager import Product, app



# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    # Charge tous les produits en mémoire et filtre en Python
    # all_products = Product.query.all()
    # filtered_products = [product for product in all_products if query.lower() in product.name.lower()]

    # On va plutôt faire une requête SQL pour optimiser
    filtered_products = Product.query.filter(func.lower(Product.name).ilike(f'%{query.lower()}%')).all()
    return jsonify([{'id': product.id, 'name': product.name} for product in filtered_products])

if __name__ == '__main__':
    app.run(debug=True)