from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1 style='color: red'>hello Flask</h1>"

if __name__ == "__main__":
    app.run()

