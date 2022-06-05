from flask import Flask, render_template,url_for
from flask import request as req
import requests

app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def index():
    return render_template("index.html")

@app.route("/Summarize", methods=['GET', 'POST'])
def Summarize():
    if req.method == 'POST':
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": "Bearer xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}

        data = req.form["data"]

        maxl = int(req.form["maxl"])
        minl = maxl // 4

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query({

            "inputs": data,
            "parameters": {'min_length': minl, 'max_length': maxl},
        })[0]

        return render_template("index.html", result=output['summary_text'])
    else:
        return render_template("index.html")



if __name__ == '__main__':
    app.debug=True
    app.run()
