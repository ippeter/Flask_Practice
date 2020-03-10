from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return "Index Page"

@app.route('/simple', methods=['GET', 'POST'])
def simple():
    if (request.method == 'POST'):
        print("Args len =", len(request.form))
        #searchword = request.args.get('param1', '')
        print("Args received:", request.form)
    return ",".join(list(request.form.keys()))