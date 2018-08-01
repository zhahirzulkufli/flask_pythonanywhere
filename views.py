from flask import Flask, request, redirect, url_for, abort, render_template, flash

app = Flask(__name__)

@app.route("/")
def base():
    return render_template("base.html")
