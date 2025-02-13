from flask import Flask, render_template
app = Flask(__name__)

# HOME PAGE
@app.route('/')
def hello_world():
    return render_template("hero.html")

# ABOUT PAGE
@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)