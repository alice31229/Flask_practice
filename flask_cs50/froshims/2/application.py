import os
import smtplib
from flask import Flask, render_template,request

app=Flask(__name__) #, template_folder="templates")

students=[]

@app.route("/")
def index(): # http://0.0.0.0:1234/?name=alice
    return render_template("index.html")
    #  name=request.args.get("name", 'somebody')
    #  return render_template("index.html", name_html=name)

# send email part need to set security settings and set .env for password
@app.route("/register", methods=["POST"])
def register():
    # check the data is right but not spam
    name=request.form.get("name")
    dorm=request.form.get("dorm")
    email=request.form.get("email")
    if not name or not dorm or not email:
        return render_template("failure.html")
    msg="Congrats for registered!"
    server=smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    #set .env variable
    #https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5
    server.login("alice31229@yahoo.com.tw", os.getenv("PASSWORD"))
    server.sendmail("alice31229@yahoo.com.tw", email, msg)
    
    students.append(f"{name} from {dorm}")
    return render_template("success.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=1234, debug=True)