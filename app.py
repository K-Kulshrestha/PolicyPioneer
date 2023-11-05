from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run()

@app.route('/about')
def about():
    return 'This is the About page.'

@app.route('/contact')
def contact():
    return 'Contact us at example@example.com'

from flask import render_template

@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', username=username)
