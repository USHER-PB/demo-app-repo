from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    version = os.environ.get('APP_VERSION', 'v2')
    return f"Hello from this Demo App! Running Version: {version}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
