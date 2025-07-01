from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin POSTs

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form or request.json
    name = data.get('name')
    email = data.get('email')
    # Process your data here (e.g. save to DB)
    return jsonify({
        'status': 'success',
        'received': {'name': name, 'email': email}
    }), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)