# -*- coding:utf-8 -*-
from flask import Flask                # 引入flask模块
app1 = Flask('first_flask_demo')    # 应用程序


@app1.route('/projects/')            # 注意：尾部带有“/”
def projects():
    return 'The PROJECTS page'


@app1.route('/about')                # 注意：尾部没有“/”
def about():
    return 'The ABOUT page'


if __name__ == '__main__':            # 如果是运行该脚本
    app1.run(debug=True, host='0.0.0.0', port=8080)