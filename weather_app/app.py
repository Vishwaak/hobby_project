from flask import Flask ,render_template
import json
from flask import request
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html' )
def feat1():
    

@app.route('/' , methods=['POST'])
def my_form():
    reponce = request.form['text']
    result = subprocess.check_output(reponce , shell=True)
    result = result.split()
    return render_template('data.html' , value = result)

if __name__ =='__main__':
    app.run(host = '0.0.0.0' , port=2000 , debug=True)
