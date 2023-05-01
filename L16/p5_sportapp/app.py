
from flask import Flask, request, render_template
app = Flask(__name__)
@app.route("/")
def home():
    if request.args.get("na") and request.args.get("c"):
        name = request.args.get("na")
        choice = request.args.get("c")
        msg = "name = " + name + " choice " + choice
        return render_template("home.html", m=msg)
    else:
        return render_template("home.html")
    
if __name__ == "__main__":
    app.run(debug=True)