from flask import Flask, render_template,request

app=Flask(__name__) #, template_folder="templates")

@app.route("/")
def index(): # http://0.0.0.0:1234/?name=alice
    return render_template("index.html")
    #  name=request.args.get("name", 'somebody')
    #  return render_template("index.html", name_html=name)

@app.route("/register", methods=["POST"])
def register():
    # check the data is right but not spam
    if not request.form.get("name") or not request.form.get("dorm"):
        return render_template("failure.html")
    return render_template("success.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=1234, debug=True)