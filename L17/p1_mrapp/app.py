
from flask import * 
from sqlite3 import *
app = Flask(__name__)
@app.route("/")
def home():
    if request.args.get("mn") and request.args.get("rv"):
        mn = request.args.get("mn")
        rv = request.args.get("rv")
        con = None
        try:
            con = connect("mr.db")
            sql = "insert into movie values('%s','%s')"
            cursor = con.cursor()
            cursor.execute(sql % (mn,rv))
            con.commit()
            msg = "thank u for ur feedback"
            return render_template("home.html", m=msg) 
        except Exception as e:
            con.rollback()
            msg = "issue " + str(e)
            return render_template("home.html", m=msg)
        finally:
            if con is not None:
                con.close()
    else:
        return render_template("home.html")
    
if __name__=="__main__":
    app.run(debug=True, use_reloader=True,port=8080)





