from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from src.contact import NotificationManager


app = Flask(__name__)
bootstrap = Bootstrap5(app)


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/experience")
def experience():
    return render_template("experience.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")

    if request.method == "POST":
        form_name = request.form["fullname"]
        form_email = request.form["email"]
        form_phone = request.form["phone"]
        form_subject = request.form["subject"]
        form_message = request.form["message"]
        NotificationManager(
            name=form_name, email=form_email, phone=form_phone, subject=form_subject, message=form_message
        ).send_email()
        return render_template("contact_submitted.html")


# To use while editing
if __name__ == "__main__":
    app.run(debug=True)
