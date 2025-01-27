from flask import Flask, request, jsonify
from utilisateur import Utilisateur
from tache import Tache
from gestionnaire_de_taches import GestionnaireDeTaches

app = Flask(__name__)
gestionnaire = GestionnaireDeTaches("taches.db")


@app.route("/utilisateurs", methods=["POST"])
def creer_utilisateur():
    data = request.json
    utilisateur = Utilisateur(nom=data["nom"], email=data["email"])
    gestionnaire.ajouter_utilisateur(utilisateur)
    return jsonify({"message": "Utilisateur créé avec succès"}), 201


@app.route("/taches", methods=["POST"])
def ajouter_tache():
    data = request.json
    tache = Tache(
        titre=data["titre"],
        description=data["description"],
        utilisateur_email=data["utilisateur_email"],
    )
    gestionnaire.ajouter_tache(tache)
    return jsonify({"message": "Tâche ajoutée avec succès"}), 201


@app.route("/taches/<utilisateur_email>", methods=["GET"])
def recuperer_taches(utilisateur_email):
    taches = gestionnaire.recuperer_taches(utilisateur_email)
    return jsonify(taches)


if __name__ == "__main__":
    app.run(debug=True)
