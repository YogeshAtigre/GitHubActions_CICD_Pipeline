from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Jenkins CI/CD Pipeline with Flask Application!'

if __name__ == '__main__':
    app.run(host='34.238.160.181', port=5000, debug=True)
