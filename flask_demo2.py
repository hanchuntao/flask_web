# -*- coding:utf-8 -*-
from flask import Flask
app1 = Flask('first_flask_demo')


@app1.route('/user/<username>')         # 指定了格式
def demo1(username):                    # username是用户从地址上的输入
    return 'Welcome %s' % username


if __name__ == '__main__':
    app1.run(debug=True, host='0.0.0.0', port=8080)