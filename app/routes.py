from app import app
from flask import render_template, request, redirect, url_for


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route("/submit", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        return render_template(
            "contact.html",
            success=True, name=name, email=email, message=message
        )
    else:
        return redirect(url_for('contact'))
