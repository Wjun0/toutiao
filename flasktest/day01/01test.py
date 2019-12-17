from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    print('hello')
    return 'hello flask'

if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask
#
# apps = Flask(__name__)
#
#
# @apps.route('/index')
# def home():
#     return 'index'
#
#
# if __name__ == '__main__':
#     apps.run(debug=True)