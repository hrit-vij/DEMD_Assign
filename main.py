from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def base_route():
    return "Welcome to praxis"

@app.route("/my_name/<name>")
def print_name(name):
    return f"Welcome {name}"


if __name__ =="__main__":
    app.run(host = "0.0.0.0", port = 8000)