from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    """
    Method returning json message.
    """
    message = { "message": "Hello World!"}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')