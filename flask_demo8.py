from flask import Flask, render_template
app1 = Flask('first_flask_demo')


@app1.route('/')
def index():
    data = [
        {"href": "back.html", "caption": "back"},
        {"href": "forward.html", "caption": "forward"},
    ]
    return render_template('hello3.html', href_list=data)


if __name__ == '__main__':
    app1.run(debug=True, host='0.0.0.0', port=8080)