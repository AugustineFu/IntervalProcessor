# (A) INIT
# (A1) LOAD MODULES
from flask import Flask, render_template
import csv

# (A2) FLASK SETTINGS + INIT
HOST_NAME = "localhost"
HOST_PORT = 80
app = Flask(__name__)


# app.debug = True

# (B) DEMO - READ CSV & GENERATE HTML TABLE
@app.route("/")
def index():
    with open("static/tips.csv") as file:
        reader = csv.reader(file)
        return render_template("table.html", csv=reader)


# (C) START
if __name__ == "__main__":
    app.run(HOST_NAME, HOST_PORT)
