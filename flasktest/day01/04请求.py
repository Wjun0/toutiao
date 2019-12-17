
from flask import Flask, request

app = Flask(__name__)



@app.route('/index',methods=['POST','GET'])
def home():
    print(request.url)
    print(request.method)
    print(request.headers)
    print(request.headers.get("Host"))

    return 'index'


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