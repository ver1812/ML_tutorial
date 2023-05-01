from flask import Flask, request, render_template
app = Flask (__name__)
@app.route("/")
def home():
    if request.args.get("na"):
        name = request.args.get("na")
        py = request.args.get("py")
        js = request.args.get("is")
        ja = request.args.get("ja")
        lang ="" 
        if py:
            lang = lang + " python "
        if js:
            lang = lang + " javascript "
        if ja:
            lang = lang + " java"
        msg = "name =" + name + " languages " + lang
        return render_template("home.html", m=msg)
    else:
        return render_template("home.html")
    
if __name__ == "__main__":
    app.run(debug=True)