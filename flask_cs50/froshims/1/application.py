from flask import Flask, render_template,request,redirect

app=Flask(__name__) #, template_folder="templates")

students=[]

@app.route("/")
def index(): # http://0.0.0.0:1234/?name=alice
    return render_template("index.html")
    #  name=request.args.get("name", 'somebody')
    #  return render_template("index.html", name_html=name)

@app.route("/registrants")
def registrants():
    return render_template("registered.html", students=students)

@app.route("/register", methods=["POST"])
def register():
    # check the data is right but not spam
    name=request.form.get("name")
    dorm=request.form.get("dorm")
    if not name or not dorm:
        return render_template("failure.html")
    students.append(f"{name} from {dorm}")
    return redirect("/registrants")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=1234, debug=True)