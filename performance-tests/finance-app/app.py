from flask import Flask, jsonify
import time  # Utilisé pour simuler un calcul lourd

app = Flask(__name__)

def generate_financial_report(company_id):
    """Simule la génération d'un rapport financier coûteux."""
    time.sleep(5)  # Simule un calcul long de 5 secondes
    return {
        "company_id": company_id,
        "report": "Rapport financier détaillé ici..."
    }

@app.route('/financial_report/<company_id>')
def financial_report(company_id):
    report = generate_financial_report(company_id)
    return jsonify(report)

if __name__ == '__main__':
    app.run(debug=True)
