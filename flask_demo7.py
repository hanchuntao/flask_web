from flask import Flask, url_for, render_template
app1 = Flask('first_flask_demo')


@app1.route('/<username>')
def index(username):
    return render_template('hello2.html', username=username)


if __name__ == '__main__':
    app1.run(debug=True, host='0.0.0.0', port=8080)