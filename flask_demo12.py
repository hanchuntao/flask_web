from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'

# Run the Flask application to serve up http pages
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
#
# if __name__ == '__main__':
#     app.debug = True
#     app.run(host='0.0.0.0', port=8080)