from  flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=["POST","GET"])
def index():
    if request.method == "POST":
        userDetails =request.form
        name = userDetails['name']
        email = userDetails['email']
        return name, email
       
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True, port="5050")