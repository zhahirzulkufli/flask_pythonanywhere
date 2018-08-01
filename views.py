from flask import request, redirect, url_for, abort, render_template, flash

@app.route("/")
def base():
    return render_template("base.html")
