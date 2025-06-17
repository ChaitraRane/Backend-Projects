from flask import Flask, request, jsonify
import json, os

app = Flask(__name__)
DATA_FILE = 'data.json'

@app.route('/')
def home():
    return "Welcome to Flask API on Render!"

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json
    
    # Save to JSON file
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)

    with open(DATA_FILE, 'r') as f:
        existing_data = json.load(f)

    existing_data.append(data)

    with open(DATA_FILE, 'w') as f:
        json.dump(existing_data, f, indent=4)

    return jsonify({'status': 'success', 'data': data})
