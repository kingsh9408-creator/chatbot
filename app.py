
from flask import Flask



app = Flask(__name__)



@app.route("/")

def home():

return "Hello! I'm the mini chatbot for the Cloud Infrastructure"



if __name__ == "__main__":

app.run(host="0.0.0.0", port=5000)

