from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    return "Welcome to your first containerized web app!

if __name__ == "__main__":
    app.run()
