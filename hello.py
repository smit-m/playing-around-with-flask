from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return("Hello World!")

@app.route("/me")
def hello_me():
    return("Hello Smit!")
    

if __name__ == "__main__":
    app.run()