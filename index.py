# app.py
from flask import Flask

app = Flask(__name__) # <-- Vercel ищет именно эту переменную 'app'

@app.route('/')
def home():
    return 'Hello, World!'