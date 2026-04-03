from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
# Render will provide this from your Environment Variables
app.config['DATABASE_URI'] = os.environ.get('postgresql://postgres:zIXYDXoRaDoXjNPn@db.dwbphotswgudwvnbrjay.supabase.co:5432/postgres')
db = SQLAlchemy(app)

class Leaderboard(db.Model):
    id = db.Model.Column(db.Model.Integer, primary_key=True)
    username = db.Model.Column(db.Model.String(50))
    score = db.Model.Column(db.Model.Integer)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    # Basic validation
    if not data or 'username' not in data or 'score' not in data:
        return jsonify({"error": "Invalid data"}), 400
        
    entry = Leaderboard(username=data['username'], score=data['score'])
    db.session.add(entry)
    db.session.commit()
    return jsonify({"message": "Score saved to Supabase!"}), 201
