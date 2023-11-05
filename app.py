from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/liabilities', methods=["POST", "GET"])
def liabilities():
    return render_template('liabilities.html')
    
@app.route('/propertyCoverage', methods=["POST", "GET"])
def propertyCoverage():
    return render_template('propertyCoverage.html')

@app.route('/about', methods=["POST", "GET"])
def about():
    return render_template('about.html')

@app.route('/contact', methods=["POST", "GET"])
def contact():
    return render_template('contact.html')

# Add a new route to render the HTML page with the map
@app.route('/map', methods=["GET"])
def show_map():
    return render_template('location.html')

if __name__ == '__main__':
    app.run()

