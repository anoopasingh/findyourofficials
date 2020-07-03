# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template, session
from flask import request, redirect, url_for
from dotenv import load_dotenv #import a function
load_dotenv() #using function-- finds .env, pulls in info
import model as m
import os

# -- Initialization section --
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# -- Routes section --
@app.route('/')
@app.route('/index', methods=['GET', 'POST']) #not get required
def index():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        form = request.form
        address = form.get("address","10021") #dict method with default value
        response = m.access_API(address) #name spaces
        session["officials"] = response
        print(session)
        return redirect(url_for("results"))


@app.route('/results')
def results():
    data = {}
    data["representatives"] = session["officials"]
    return render_template("results.html", data=data)
