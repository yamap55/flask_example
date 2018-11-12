from flask import Flask
app = Flask(__name__)


@app.route('/')
def root():
    return 'Hello World'


@app.route('/about')
def about():
    return '<h1>About</h1>'


@app.route('/hello/<string:name>')
def hello(name):
    return f'<h1>Hello {name}</h1>'


if __name__ == "__main__":
    app.debug = True
    app.run()
