from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def home():
    if request.args.get("num"):
        num = int(request.args.get("num"))
        if num % 2 == 0:
            res = "even"
        else:
            res = "odd"
            msg = "num =" + str(num) + " res = " + res
            return render_template("home.html", m=msg)
    else:
        return render_template("home.html")

if __name__ =="__main__":
    app.run(debug=True, use_reloader=True)