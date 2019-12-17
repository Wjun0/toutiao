from flask import Flask
from user import new_blu

app = Flask(__name__)

app.register_blueprint(new_blu)

if __name__ == '__main__':
    app.run(debug=True)