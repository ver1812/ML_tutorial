from flask import *
app = Flask(__name__)

@app.route("/")
def home():
    if request.args.get("num"):
        num = float(request.args.get("num"))
        sqr = num * num
        msg = "square = " + str(round(sqr,2))
        return render_template("home.html", m=msg)
    else:
        return render_template("home.html")
if __name__=="__main__":
    app.run(debug=True, use_reloader=True)