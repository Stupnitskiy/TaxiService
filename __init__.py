from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, I love Digital Ocean!"

@app.route("/isit?")
def lol():
    return "It work's?"

@app.route("/yes")
def yes():
    return "yes"

if __name__ == "__main__":
    app.config['DEBUG'] = True
    app.run(port=8000)