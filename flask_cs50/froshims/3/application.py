import csv
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
    name=request.form.get("name") #POST -> request.form.get; GET -> request.args.get
    dorm=request.form.get("dorm")
    
    if not name or not dorm:
        return render_template("failure.html")
    file=open("registered.csv", "a")
    writer=csv.writer(file)
    writer.writerow((name,dorm))
    file.close()
    return render_template("success.html")

@app.route("/registered")
def registered():
    with open("registered.csv", "r") as file:
        reader=csv.reader(file)
        students=list(reader)
    return render_template('registered.html', students=students)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=1234, debug=True)