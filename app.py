import os
from flask import Flask, jsonify

app = Flask(__name__)

learning_modules = [ { "id": 1, "topic": "Git Fundamentals", "status" : "Completed"},
                    {"id" : 2, "topic": "Flask REST APIs", "status" : "In-progress"},
                    {"id": 3, "topic" : "AWS Cloud Integration", "status": "Not Started"}
                    ]

@app.route('/')
def home():
    return "micro learning engine: Online and Tracking!"

@app.route('/api/modules', methods=['GET'])
def get_modules():
    return jsonify({
        "status" : "success", "total_modules" : len(learning_modules), "data" : learning_modules
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)