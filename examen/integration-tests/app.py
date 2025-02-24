# app.py
from flask import Flask, request, jsonify
from database_manager import init_db, ajouter_livre_db, get_livres_db, emprunter_livre_db, retourner_livre_db, get_db_connection

app = Flask(__name__)

# @app.route('/ajouter', methods=['POST'])
# def ajouter_livre():
#     data = request.json
#     ajouter_livre_db(data['titre'], data['auteur'])
#     return jsonify({'message': 'Livre ajouté avec succès'}), 201
#
# @app.route('/livres', methods=['GET'])
# def lister_livres():
#     livres = get_livres_db()
#     return jsonify([dict(livre) for livre in livres])

## Before integration tests ##
# @app.route('/emprunter', methods=['POST'])
# def emprunter_livre():
#     titre = request.json['titre']
#     if emprunter_livre_db(titre):
#         return jsonify({'message': 'Livre emprunté avec succès'}), 200
#     else:
#         return jsonify({'message': 'Livre non disponible'}), 404



# @app.route('/retourner', methods=['POST'])
# def retourner_livre():
#     titre = request.json['titre']
#     if retourner_livre_db(titre):
#         return jsonify({'message': 'Livre retourné avec succès'}), 200
#     else:
#         return jsonify({'message': 'Livre non trouvé ou déjà retourné'}), 404


## After integration tests ##
@app.route('/ajouter', methods=['POST'])
def ajouter_livre():
    data = request.get_json()
    titre = data.get('titre')
    auteur = data.get('auteur')

    if not titre or not auteur:
        return jsonify({'message': "Les champs 'titre' et 'auteur' sont requis."}), 400

    ajouter_livre_db(titre, auteur)
    return jsonify({'message': 'Livre ajouté avec succès'}), 201


@app.route('/livres', methods=['GET'])
def lister_livres():
    livres = get_livres_db()
    return jsonify([dict(livre) for livre in livres])


@app.route('/emprunter', methods=['POST'])
def emprunter_livre():
    data = request.get_json()
    titre = data.get('titre')

    if not titre:
        return jsonify({"message": "Le champ 'titre' est requis."}), 400

    if emprunter_livre_db(titre):
        return jsonify({'message': 'Livre emprunté avec succès'}), 200
    else:
        return jsonify({'message': 'Livre non disponible'}), 404


@app.route('/retourner', methods=['POST'])
def retourner_livre():
    data = request.get_json()
    titre = data.get('titre')

    if not titre:
        return jsonify({"message": "Le champ 'titre' est requis."}), 400

    if retourner_livre_db(titre):
        return jsonify({'message': 'Livre retourné avec succès'}), 200
    else:
        return jsonify({'message': 'Livre non trouvé ou déjà retourné'}), 404

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
