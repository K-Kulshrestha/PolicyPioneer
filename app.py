from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient 
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

llm = OpenAI(openai_api_key="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")


# Replace these placeholders with your actual MongoDB connection details
MONGO_URI = "mongodb+srv://HackUTDx:hack23@cluster0.8ykqrpw.mongodb.net/HackUTD_X_StateFarm_Database?retryWrites=true&w=majority"

# Create a MongoClient instance
client = MongoClient(MONGO_URI)

# Select your MongoDB database and collection (use the name of your database and collection)
db = client.HackUTD_X_StateFarm_Database
collection = db.your_collection

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

@app.route('/get_data', methods=["GET"])
def get_data():
    data = collection.find()
    # Process the data or return it as needed
    return render_template('data.html', data=list(data))

@app.route('/chat', methods=["POST"])
def chat():
    user_input = request.form.get('user_input')  # Get user input from the web interface
    response = chat_model.predict(user_input)  # Use the chat model to generate a response
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run()

