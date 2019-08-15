from flask import Flask, render_template 
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home.html")

@app.route("/me")
def hello_me():
    return("Hello Smit!")
    

if __name__ == "__main__":
    app.run()