from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import not_, or_, and_, any_, func
from sqlalchemy.orm import load_only

app = Flask(__name__)
# 设置数据库连接地址
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:mysql@127.0.0.1:3306/test"
# 设置是否跟踪数据库改变
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = False
# 创建数据库连接
db = SQLAlchemy(app)


# 自定义类 继承db.Model  对应 表
class User(db.Model):
    __tablename__ = "users"  # 表名 默认使用类名的小写
    # 定义类属性 记录字段
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    age = db.Column(db.Integer)

    def __repr__(self):  # 自定义 交互模式 & print() 的对象打印
        return "(%s, %s, %s, %s)" % (self.id, self.name, self.email, self.age)


@app.route('/')
def index():

    # 查询所有用户数据
    # users = User.query.all()
    # print(users)

    # 查询有多少个用户
    # count = User.query.count()
    # print(count)

    # 查询第1个用户
    # user = User.query.first()
    # print(user)

    # 查询id为4的用户[3种方式]
    # user = User.query.get(4)
    user = User.query.filter_by(id=4).first()
    # user = User.query.filter(User.id==4).first()
    print(user)

    # 查询名字结尾字符为g的所有用户[开始 / 包含]
    # user = User.query.filter(User.name.startswith('g')).all()
    # user1 = User.query.filter(User.name.endswith('g')).all()
    # user2 = User.query.filter(User.name.contains('g')).all()
    # print(user,user1,user2)

    # 查询名字和邮箱都以li开头的所有用户[2种方式]
    # user = User.query.filter(User.name.startswith('li'),User.email.startswith('li')).all()
    # print(user)


    # 查询age是25 或者 `email`以`itheima.com`结尾的所有用户
    # user = User.query.filter(User.age == 25,User.email.endswith('itheima.com')).all()
    # print(user)


    # 查询名字不等于wang的所有用户[2种方式]
    # user = User.query.filter(User.name !='wang').all()
    # print(user)
    # user = User.query.filter(not_(User.name =='wang')).all()
    # print(user)

    # 查询id为[1, 3, 5, 7, 9]的用户
    # user = User.query.filter(User.id.in_([1,3,5,7,9])).all()
    # print(user)

    # 所有用户先按年龄从小到大, 再按id从大到小排序, 取前5个
    # user = User.query.order_by(User.age,User.id.desc()).limit(5).all()
    # print(user)

    # 查询年龄从小到大第2-5位的数据
    # user = User.query.order_by(User.age).offset(1).limit(4).all()
    # print(user)


    # 分页查询, 每页3个, 查询第2页的数据
    # pn = User.query.paginate(2,3)
    # print(pn.items)

    # 查询每个年龄的人数    select age, count(name) from t_user group by age  分组聚合
    # user = db.session.query(User.age,func.count(id)).group_by(User.age).all()
    # print(user)

    # 只查询所有人的姓名和邮箱  优化查询   默认使用select *
    user = db.session.query(User.name,User.email).all()
    print(user)

    user = User.query.options(load_only(User.name,User.email)).all()
    print(user)

    return 'index'


if __name__ == '__main__':
    # 删除所有表
    # db.drop_all()
    # # 创建所有表
    # db.create_all()
    # # 添加测试数据
    # user1 = User(name='wang', email='wang@163.com', age=20)
    # user2 = User(name='zhang', email='zhang@189.com', age=33)
    # user3 = User(name='chen', email='chen@126.com', age=23)
    # user4 = User(name='zhou', email='zhou@163.com', age=29)
    # user5 = User(name='tang', email='tang@itheima.com', age=25)
    # user6 = User(name='wu', email='wu@gmail.com', age=25)
    # user7 = User(name='qian', email='qian@gmail.com', age=23)
    # user8 = User(name='liu', email='liu@itheima.com', age=30)
    # user9 = User(name='li', email='li@163.com', age=28)
    # user10 = User(name='sun', email='sun@163.com', age=26)
    #
    # # 一次添加多条数据
    # db.session.add_all([user1, user2, user3, user4, user5, user6, user7, user8, user9, user10])
    # db.session.commit()
    app.run(debug=True)