from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import random
import string

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(200))

def init_db():
    db.create_all()

    # Peuple la base de données avec des données de produits initiales si elle est vide
    if Product.query.count() == 0:
        products = [
            Product(name="Laptop", description="A portable computer"),
            Product(name="Smartphone", description="A personal device that combines cellular and mobile computing functions"),
            Product(name="Headphones", description="A pair of small loudspeaker drivers worn on or around the head over a user's ears"),
            Product(name="Charger", description="A device used to charge electronic devices"),
            Product(name="Camera", description="A device used to capture images"),
        ]

        db.session.bulk_save_objects(products)
        db.session.commit()

def create_product_name(index):
    """Génère un nom de produit, incluant 'phone' pour 1 produit sur 10."""
    if index % 10 == 0:  # Assure que 1 000 produits sur 10 000 incluent 'phone'
        return 'Product Phone ' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    else:
        return 'Product ' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

def create_products(num_products=100000):
    db.create_all()  # Crée les tables si elles n'existent pas

    for i in range(num_products):
        name = create_product_name(i)
        description = 'Description for ' + name
        product = Product(name=name, description=description)
        db.session.add(product)
        # Pour éviter les erreurs d'interruption en cas de noms en double
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()  # Annule la transaction en cas d'erreur et continue

if __name__ == '__main__':
    with app.app_context():
        create_products()
        print(f'{Product.query.count()} products created in the database.')

        # init_db()
        # print('Database initialized and populated with initial data.')
