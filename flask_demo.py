from flask import Flask

app1 = Flask('first_flask_demo')


@app1.route('/')
def demo1():
    return 'Welcome to python in one'


@app1.route('/api_demo2')  # 定义另外一个路由
def api_demo2():
    return 'you are visiting api_demo2'


if __name__ == '__main__':
    app1.run()