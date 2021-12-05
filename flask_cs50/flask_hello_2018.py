# before flask
# from http.server import BaseHTTPRequestHandler, HTTPServer

# class HTTPServer_RequestHandler(BaseHTTPRequestHandler):

#     def do_GET(self):
#         self.send_response(200)
#         self.send_header("Content-type", "text/html")
#         self.end_headers();

#         self.wfile.write(b"<!DOCTYPE html>")
#         self.wfile.write(b"<html lang='en'>")
#         self.wfile.write(b"<head>")
#         self.wfile.write(b"<title>hello, title</title>")
#         self.wfile.write(b"</head>")
#         self.wfile.write(b"<body>")
#         self.wfile.write(b"Hello, world")
#         self.wfile.write(b"</body>")
#         self.wfile.write(b"</html>")

# port=8080
# server_address=("0.0.0.0", port)
# httpd=HTTPServer(server_address, HTTPServer_RequestHandler)

# httpd.serve_forever()



### Basic structure of flask ###
#!!! export FLASK_APP=cs50_flask_2018.py



from flask import Flask, render_template,request

app=Flask(__name__) #, template_folder="templates")

@app.route("/")
def index(): # http://0.0.0.0:1234/?name=alice
#    return "Hello, world"
     name=request.args.get("name", 'somebody')
     return render_template("index.html", name_html=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=1234, debug=True)