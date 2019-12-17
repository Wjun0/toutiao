from flask import Flask

app = Flask(__name__)
# 1,url 必须以/开头
# 2,可以根据methods参数设置路由的请求
@app.route('/index',methods=['POST','GET'])
def index():
    return 'index'



if __name__ == '__main__':
    #3，可以通过app.url_map属性来获取所有的路由规则
        # （url资源段  支持的请求方式 视图函数的标记）
    print(app.url_map)
    for rule in app.url_map.iter_rules():
        print(rule.rule,rule.methods,rule.endpoint)
    app.run(debug=True)
