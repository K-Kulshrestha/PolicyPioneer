from flask import Flask, render_template
from pymongo import MongoClient

# Replace these placeholders with your actual MongoDB connection details
MONGO_URI = "mongodb+srv://HackUTDx:hack23@cluster0.8ykqrpw.mongodb.net/HackUTD_X_StateFarm_Database?retryWrites=true&w=majority"

# Create a MongoClient instance
client = MongoClient(MONGO_URI)

# Select your MongoDB database and collection (use the name of your database and collection)
db = client.HackUTD_X_StateFarm_Database
collection = db.your_collection

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Flask!'

@app.route('/liabilities')
def liabilities():
    return render_template('liabilities.html')
    
@app.route('/propertyCoverage')
def propertyCoverage():
    return render_template('propertyCoverage.html')

@app.route('/about')
def about():
    return 'This is the About page.'

@app.route('/contact')
def contact():
    return 'Contact us at example@example.com'

@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', username=username)

@app.route('/get_data')
def get_data():
    data = collection.find()
    # Process the data or return it as needed
    return str(list(data))

if __name__ == '__main__':
    app.run()

# Insert data  
data = {"name": "John", "age": 30}
collection.insert_one(data)

# Retrieve data
result = collection.find_one({"name": "John"})
print(result)