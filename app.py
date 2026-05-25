from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "micro learning engine: Online and Tracking!"

if __name__ == '_main__':
    app.run(host='0.0.0.0', port=5000, debug=True)