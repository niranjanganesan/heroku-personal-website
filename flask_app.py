from flask import Flask, render_template, request, redirect
import smtplib, ssl
from flask_mail import Mail, Message
import os

app = Flask(__name__)
user_name=os.environ.get('username')
password=os.environ.get('password')

app.config.update(dict(
    MAIL_SERVER = 'smtp.googlemail.com',
    MAIL_PORT = 465,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = user_name,
    MAIL_PASSWORD = password
))

mail = Mail(app)
@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route("/thankyou", methods=["GET", "POST"])
def my_form():
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")
        message_body = "Name: %s \n Email: %s \n Subject: %s \n Message: %s" %(name, email, subject, message)
        msg = Message('Msg from website', sender='madninja.business@gmail.com', recipients=['niranjan27494@gmail.com'])
        msg.body = message_body
        mail.send(msg)
    return render_template("thankyou.html")

@app.route("/cineplex_project")
def cineplex_project():
    return render_template("cineplex_project.html")

@app.route("/bigdata_project")
def bigdata_project():
    return render_template("bigdata_project.html")

@app.route("/cloud_project")
def cloud_project():
    return render_template("cloud_project.html")

if __name__ == "__main__":
    app.run(debug=True)
