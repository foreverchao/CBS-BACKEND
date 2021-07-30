from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask HI HI"

@app.route("/test")
def test():
    return "Hello Flask test"

if __name__ == "__main__":
    app.run()