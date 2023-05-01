from flask import * 
from sqlite3 import *
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form[ "na"]
        education = request. form["e"]
        lang = "" 
        if request.form.get("python"):
            lang = lang + " Python "
        if request.form.get("js"):
            lane = lane + " JavaScript "
        if request.form.get("java"):
            lang = lang + " Java "
        if request.form.get("c"):
            lang = lang + " C"
        con = None
        try:
            con = connect("profile.db")
            sql = "insert into candidate values ('%s', '%s', '%s')"
            cursor = con.cursor()
            cursor.execute(sql % (name, education, lang))
            con.commit()
            msg = "record saved"
            return render_template("home.html", m=msg) 
        except Exception as e:
            con.rollback()
            msg = "issue" + str(e)
            return render_template("home.html", m=msg) 
        finally:
            if con is not None:
                con.close()
    else:
        return render_template("home.html")
    
if __name__=="__main__":
    app.run(debug=True, use_reloader=True,port=8080)


