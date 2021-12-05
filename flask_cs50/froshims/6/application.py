import csv
from flask import Flask, render_template,request

app=Flask(__name__) 

students=[]

@app.route("/")
def index(): 
    return render_template("index.html")
    

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
    app.run(debug=True)
