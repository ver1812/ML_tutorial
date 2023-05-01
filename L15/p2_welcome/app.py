from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    if request.args.get("na"):
        name = request.args.get("na")
        msg = "Good Evening " + name
        return render_template("home.html")
    else:
        return render_template("home.html")
    
if __name__ == "__main__":
    app.run(debug=True,use_reloader=True)