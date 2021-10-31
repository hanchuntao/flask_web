# -*- coding:utf-8 -*-
from flask import Flask, render_template
app1 = Flask('first_flask_demo')


@app1.route('/')
def index():
    args = {                            # 给模板的参数
        'name': "alex",
        'gender': "male",
        'age': 18
    }
    return render_template('ifdemo1.html', **args)        # 使用模板


if __name__ == '__main__':
    app1.run(debug=True, host='0.0.0.0', port=8080)