from flask import *
from datetime import datetime
import pymongo
import json

app = Flask(__name__)

# before we do anything lets set up our db's!


#app picker
@app.route("/")
def index():
    return render_template("index.html")

#insert and routing
@app.route("/insert/")
def insert_today():
    today = datetime.now().strftime("%d-%m-%Y")
    return redirect(url_for("insert", date=today))

@app.route("/insert/<string:date>")
def insert(date):
    return render_template("date.html", date = date)

#mongod assimilation
@app.route("/mongod", methods = ["GET", "POST"])
def mongoose():
    if request.method == "GET":
        return render_template("mongod_select.html")
    req = request.form.get("var_to_send_to_server") 
    return render_template("result.html", query = req, data = data)


if __name__ == "__main__":
    app.run(debug=True)
