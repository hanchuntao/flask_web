from flask import Flask, url_for, render_template
app1 = Flask('first_flask_demo')


@app1.route('/')
def index():
    return render_template('hello.html')


if __name__ == '__main__':
    app1.run(debug=True, host='0.0.0.0', port=8080)