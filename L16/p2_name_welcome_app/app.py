from flask import Flask, render_template, request
from datetime import *
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def home():
    if "na" in request. form:
        name = request.form["na"]
        d = datetime.now()
        hr = d.hour
        if hr < 12:
            m = "Good Morning"
        elif hr < 16:
            m = "Good Afternoon"
        else:
            m= "Good Evening"
            msg = m + "" + name
        return render_template("home.html", m=msg)
    else:
        return render_template("home.html")
if __name__=="__main__":
    app.run(debug=True, use_reloader=True)