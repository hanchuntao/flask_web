from flask import Flask, url_for
app1 = Flask('first_flask_demo')


@app1.route('/')
def index():
    png_url = url_for('static', filename='dog.jpeg')
    return 'The URL is [%s]' % png_url


if __name__ == '__main__':
    app1.run(debug=True, host='0.0.0.0', port=8080)
