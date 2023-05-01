from flask import * 

app = Flask(__name__)

@app.route("/")
def home():
    if request.args.get("num"):
        num = int(request.args.get("num"))
        if num % 2 == 0:
            res ="even"
        else:
            res = "odd"
        msg = "num " +str(num) + " is " +res
        return render_template("home.html",m = msg)
    else:
        return render_template("home.html")

if __name__=="__main__":
    app.run(debug=True, use_reloader=True,port=8080)

