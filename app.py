#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install flask flask-cors nest_asyncio')


# In[21]:


from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
import nest_asyncio

nest_asyncio.apply()  
app = Flask(__name__)
CORS(app)

DATA_FILE = 'form_data.json'


# In[18]:


@app.route('/bulk', methods=['POST'])
def bulk_insert():
    bulk_data = request.json.get("data", [])

    with open(DATA_FILE, 'r') as f:
        existing_data = json.load(f)

    existing_data.extend(bulk_data)

    with open(DATA_FILE, 'w') as f:
        json.dump(existing_data, f, indent=4)

    return jsonify({"message": "Bulk insert successful"}), 200


@app.route('/all', methods=['GET'])
def get_all():
    with open(DATA_FILE, 'r') as f:
        existing_data = json.load(f)
    return jsonify(existing_data)


# In[19]:


from threading import Thread

def run():
    app.run(port=5000)

Thread(target=run).start()


# In[20]:


import requests

url = 'http://localhost:5000/submit'

sample_data = {
    "full_name": "Chaitra Rane",
    "email": "chai@example.com",
    "mobile": "9876543210",
    "alternate_contact": "",
    "dob": "2003-05-10",
    "gender": "Male",
    "state": "Maharashtra",
    "city": "Mumbai",
    "pin_code": "400001",
    "nationality": "Indian"
}

response = requests.post(url, json=sample_data)
print(response.json())


# In[15]:


response = requests.get("http://localhost:5000/all")
data = response.json()
for i in data:
    print(i)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# In[ ]:




