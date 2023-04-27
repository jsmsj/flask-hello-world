from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route('/hello')
def hello():
    return "Hello ElonBarbs, thankyou for telling me that vercel supports flask. love ya."
