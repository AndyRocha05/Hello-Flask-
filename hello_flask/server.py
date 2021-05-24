from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello!"

@app.route("/<name>")
def hello_person(name):
    print("*"*75)
    print ("in the hello function")
    return f"Hello {name}"

if __name__ == "__main__":
    app.run(debug=True)