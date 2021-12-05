from flask import Flask, render_template,request

app=Flask(__name__) 

@app.route("/")
def index():
#    return "Hello, world"
     name=request.args.get("name", 'somebody')
     return render_template("index.html", name_html=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=1234, debug=True)
