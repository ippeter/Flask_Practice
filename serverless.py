from flask import Flask
from flask import request
from werkzeug.utils import secure_filename

import numpy as np
import cv2

app = Flask(__name__)

@app.route('/picture', methods=['GET', 'POST'])
def picture():
    if (request.method == 'POST'):
        print(request.files)
        file = request.files['data']
        img_str = file.read()
        nparr = np.fromstring(img_str, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
        print(img_np.shape)
    return "Image processed."

@app.route('/simple', methods=['GET', 'POST'])
def simple():
    if (request.method == 'POST'):
        print("Args len =", len(request.form))
        #searchword = request.args.get('param1', '')
        print("Args received:", request.form)
    return ",".join(list(request.form.keys()))