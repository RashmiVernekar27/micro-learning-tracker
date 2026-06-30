import os
from flask import Flask, jsonify, render_template, request, redirect

app = Flask(__name__)

learning_modules = [ { "id": 1, "topic": "Git Fundamentals", "status" : "Completed"},
                    {"id" : 2, "topic": "Flask REST APIs", "status" : "In-progress"},
                    {"id": 3, "topic" : "AWS Cloud Integration", "status": "Not Started"}
                    ]

@app.route('/')
def home():
    return render_template('index.html', modules=learning_modules)

@app.route('/api/modules', methods=['GET'])
def get_modules():
    return jsonify({
        "status" : "success", "total_modules" : len(learning_modules), "data" : learning_modules
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


# Route 3: Handle Form Submissions to Add New Modules
@app.route('/add', methods=['POST'])
def add_module():
    # 1. Grab the text typed into the input box named "topic"
    new_topic = request.form.get('topic')
    
    # 2. Build a new dictionary object for it
    new_item = {
        "id": len(learning_modules) + 1,
        "topic": new_topic,
        "status": "Not-Started"
    }
    
    # 3. Append it right into our live data array
    learning_modules.append(new_item)
    
    # 4. Refresh the home page to show the updated list!
    return redirect('/')