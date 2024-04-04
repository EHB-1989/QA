from flask import Flask, request, jsonify
from database_manager import init_db, ajouter_livre_db, get_livres_db, emprunter_livre_db, retourner_livre_db, get_db_connection

app = Flask(__name__)

# Route pour ajouter un livre à la base de données via une requête POST.
# Attend un JSON avec 'titre' et 'auteur'.
@app.route('/ajouter', methods=['POST'])
def ajouter_livre():
    data = request.json
    ajouter_livre_db(data['titre'], data['auteur'])
    return jsonify({'message': 'Livre ajouté avec succès'}), 201

# Route pour lister tous les livres disponibles via une requête GET.
@app.route('/livres', methods=['GET'])
def lister_livres():
    livres = get_livres_db()
    return jsonify([dict(livre) for livre in livres])

# Route pour emprunter un livre spécifique via une requête POST.
# Attend un JSON avec 'titre'. Retourne un message selon la disponibilité.
@app.route('/emprunter', methods=['POST'])
def emprunter_livre():
    titre = request.json['titre']
    if emprunter_livre_db(titre):
        return jsonify({'message': 'Livre emprunté avec succès'}), 200
    else:
        return jsonify({'message': 'Livre non disponible'}), 404

# Route pour retourner un livre spécifique via une requête POST.
# Attend un JSON avec 'titre'. Retourne un message selon le statut du livre.
@app.route('/retourner', methods=['POST'])
def retourner_livre():
    titre = request.json['titre']
    if retourner_livre_db(titre):
        return jsonify({'message': 'Livre retourné avec succès'}), 200
    else:
        return jsonify({'message': 'Livre non trouvé ou déjà retourné'}), 404

# Initialise la base de données et lance l'application Flask.
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
