from flask import Flask, request, jsonify
from integration_tests.gestion_app.utilisateur import Utilisateur
from integration_tests.gestion_app.tache import Tache
from integration_tests.gestion_app.gestionnaire_de_taches import GestionnaireDeTaches

def create_app(db_path=':memory:'):
    app = Flask(__name__)
    gestionnaire = GestionnaireDeTaches(db_path)

    @app.route('/utilisateurs', methods=['POST'])
    def creer_utilisateur():
        data = request.json
        utilisateur = Utilisateur(nom=data['nom'], email=data['email'])
        gestionnaire.ajouter_utilisateur(utilisateur)
        return jsonify({"message": "Utilisateur créé avec succès"}), 201

    @app.route('/taches', methods=['POST'])
    def ajouter_tache():
        data = request.json
        tache = Tache(titre=data['titre'], description=data['description'], utilisateur_email=data['utilisateur_email'])
        gestionnaire.ajouter_tache(tache)
        return jsonify({"message": "Tâche ajoutée avec succès"}), 201

    @app.route('/taches/<utilisateur_email>', methods=['GET'])
    def recuperer_taches(utilisateur_email):
        taches = gestionnaire.recuperer_taches(utilisateur_email)
        return jsonify(taches)

    app.gestionnaire = gestionnaire  # Attach to app for test access
    return app

# Default app instance (not used in tests)
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
