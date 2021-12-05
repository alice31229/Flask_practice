from flask import Flask, render_template, request, jsonify

app=Flask(__name__)

WORDS=[]
with open("large.txt", 'r') as file:
    for line in file.readlines():
        WORDS.append(line.rstrip())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    q=request.args.get('q')
    words=[word for word in WORDS if q and word.startswith(q)]
    return render_template('search.html', words=words)
    #return jsonify(words)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=1234, debug=True)    