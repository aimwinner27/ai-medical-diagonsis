from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///medical.db'
db = SQLAlchemy(app)

@app.route('/api/diagnose', methods=['POST'])
def diagnose():
    data = request.get_json()
    symptoms = data.get('symptoms', [])
    if 'fever' in symptoms and 'cough' in symptoms:
        return jsonify({"prediction": "Flu"})
    return jsonify({"prediction": "Unknown"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

