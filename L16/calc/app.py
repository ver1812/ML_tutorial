from flask import Flask, render_template, request,flash

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/", methods=["POST"])
def calculate():
    num = float(request.form["num"])
    if num < 0:
        
        msg = "Negative numbers are not allowed."
    elif request.form["submit_button"] == "Square":
        result = num * num
        msg = "square = " + str(round(result, 2))
    elif request.form["submit_button"] == "Cube":
        result = num * num * num
        msg = "cube = " + str(round(result, 2))
    elif request.form["submit_button"] == "Square Root":
        result = num ** 0.5
        msg = "square root = " + str(round(result, 2))
    return render_template("home.html", m=msg)


if __name__ == "__main__":
    app.run(debug=True)