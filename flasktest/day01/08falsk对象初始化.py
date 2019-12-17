from flask import Flask
import sys

#记录模块的查询路径。 包含 项目目录，接收器目录，第三方包的安装目录
print(sys.path)

app = Flask(__name__, #导入名称，flask会根据该参数查询静态/模板文件存储路径
            static_folder='static1',    #设置静态文件的存储路径
            static_url_path='/res/img', #设置静态文件的访问路径
            template_folder='templates' #设置模板文件的存储路径
            )
