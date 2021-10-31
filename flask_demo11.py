# -*- coding:utf-8 -*-
from flask import Flask
from flask import request
import json

app = Flask(__name__)


# 设置访问路由
@app.route('/hello',methods=['GET','POST'])
def get_post_handler():
    # GET请求逻辑
    if request.method == 'GET':
        # 获取GET请求的参数id 如果没有则赋值字符串null
        _id = request.args.get('id','null')
        # 获取Header里的'Host'
        print(request.headers['Host'])
        # 访问curl http://127.0.0.1:8888/hello?id=abc 结果返回id is : abc
        return "id is : %s" %  _id
    # POST请求逻辑
    if request.method == 'POST':
        # 获取POST表单参数id 如果没有则赋值字符串null,
        # 这种方法只能获取标准的from表单或者 x-www-form-urlencoded 结构数据
        _postid = request.form.get('id','null')
        # 访问curl -X POST -d "id=abc" http://127.0.0.1:8888/hello
        # 结果返回_postid is: abc
        return "_postid is: %s" % (_postid)


@app.route('/json', methods=['POST'])
def json_handler():
    if request.method == 'POST':
        jsondata = request.data
        print(jsondata)
        data = json.loads(jsondata)
        print(type(data))
        return "ok"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8888)