# -*- coding:utf-8 -*-
from flask import Flask                    # 引入Flask
app1 = Flask('first_flask_demo')        # 创建应用程序


@app1.route('/user/<int:userid>')        # 限定参数userid只能是整数
def demo1(userid):
    return 'Welcome you [User %d]' % userid


if __name__ == '__main__':
    app1.run(debug=True, host='0.0.0.0', port=8080)