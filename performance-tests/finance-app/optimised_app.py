from flask import Flask, jsonify
from flask_caching import Cache
import time

app = Flask(__name__)

config = {
    "CACHE_TYPE": "simple", 
    "CACHE_DEFAULT_TIMEOUT": 300, 
}
cache = Cache(app)
cache.init_app(app, config=config)

def generate_financial_report(company_id):
    """Simule la génération d'un rapport financier coûteux."""
    time.sleep(5) 
    return {
        "company_id": company_id,
        "report": "Rapport financier détaillé ici..."
    }

@app.route('/financial_report/<company_id>')
@cache.cached(timeout=300, key_prefix="financial_report_") #5 minutes
def financial_report(company_id):
    report = generate_financial_report(company_id)
    return jsonify(report)

if __name__ == '__main__':
    app.run(debug=True)
