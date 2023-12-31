from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method=="POST":
        return "Yes!! Its POST Request."
    return "Yes!! Received"

if __name__=="__main__":
    app.run(debug = True, port = 5006)



