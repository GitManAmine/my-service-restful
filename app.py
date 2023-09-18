from flask import Flask, jsonify

app = Flask(__name__)

# Liste fictive de pays
pays = [
    {"nom": "États-Unis", "code": "US"},
    {"nom": "Canada", "code": "CA"},
    {"nom": "Royaume-Uni", "code": "UK"},
    {"nom": "France", "code": "FR"},
    {"nom": "Allemagne", "code": "DE"}
]

@app.route('/api/pays', methods=['GET'])
def get_pays():
    return jsonify({'pays': pays})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
