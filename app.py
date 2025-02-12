from flask import Flask
app = Flask(__name__)

# HOME PAGE
@app.route('/')
def hello_world():
    return 'Hello, World!'


# ABOUT PAGE
@app.route('/about')
def about():
    return 'MET FIRSTS CREATE!!!!'


if __name__ == '__main__':
    app.run(debug=True)