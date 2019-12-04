from flask import Flask,current_app
#创建flask应用对象
#__name__表示当前模块的名字
#    模块名    flask   以这个模块所在的总路径目录为总目录，默认这个路径中的static为静态目录，templates为模板目录
app = Flask(__name__)

@app.route('/')
def index():
    """定义视图函数"""
    return 'Hello World!'

if __name__ == '__main__':
    #启动flask程序
    #通过app.url.map可以查看整个flask的路由信息
    print(app.url_map)
    app.run()
