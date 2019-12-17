
from flask import Flask, make_response, json, redirect, url_for
from flask.json import jsonify

app = Flask(__name__)

@app.route('/demo')
def demo():
    response = make_response('demo')
    response.headers['a'] = 1
    return response

@app.route('/demo2')
def demo2():
    dict = {'name':'zs','age':12}
    # return json.dumps(dict)

    return jsonify(name='zs',age=12)

@app.route('/demo3')
def demo3():
    # return redirect("http://www.baidu.com")

    # 可以根据视图函数的标记查询url路径
    url1 = url_for('demo2')
    return  redirect(url1)


@app.route('/demo5')
def demo5():
    # return 响应体，状态码，响应头
    return 'demo5',700,{'B':2}



if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)