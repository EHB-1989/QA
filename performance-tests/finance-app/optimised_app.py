from flask import Flask, jsonify
from flask_caching import Cache
import time

app = Flask(__name__)

# app.config['CACHE_TYPE'] = 'RedisCache'
# app.config['CACHE_REDIS_URL'] = 'redis://localhost:6379/0'

app.config['CACHE_TYPE'] = 'simple'
cache = Cache(app)

cache = Cache(app)

def generate_financial_report(company_id):
    """Simule toujours la génération d'un rapport financier coûteux."""
    time.sleep(5)
    return {
        "company_id": company_id,
        "report": "Rapport financier détaillé ici..."
    }

@app.route('/financial_report/<company_id>')
@cache.cached(timeout=3600, key_prefix='financial_report_')
def financial_report(company_id):
    report = generate_financial_report(company_id)
    return jsonify(report)

if __name__ == '__main__':
    app.run(debug=True)
