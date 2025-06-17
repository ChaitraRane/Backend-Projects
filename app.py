from flask import Flask, request, jsonify
import json, os
import requests

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


@app.route('/transfer', methods=['POST'])
def transfer_data():
    try:
        # Read data from local JSON file
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)

        # Replace this with your actual company API endpoint
        company_api_url = "https://https://webhook.site/a23c775b-b4e9-4f11-97f9-e822f43beac8/store"

        # Optional: include headers if needed
        headers = {
            "Content-Type": "application/json"
            # "Authorization": "Bearer YOUR_TOKEN"  # <-- Add this if needed
        }

        # Send data to the company API
        response = requests.post(company_api_url, headers=headers, json=data)

        return jsonify({
            'status': 'success',
            'sent_records': len(data),
            'company_status_code': response.status_code,
            'company_response': response.text
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})
