from flask import Flask, render_template

from infrastructure import EnvironmentManager


app = Flask('flask-boilerplate')


@app.route('/')
def hello():
    return render_template('hello.html', hello='Hello from Flask')


@app.route('/secret')
def secret():
    em = EnvironmentManager()
    return em.get('TEST_SECRET')


if __name__ == '__main__':
    app.run()
