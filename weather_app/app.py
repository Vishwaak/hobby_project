from flask import Flask ,render_template
import logging
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html' )

@app.route('/' , methods=['POST'])
def my_form():
    text = request.form['text']
    process_text = text.upper()
    return render_template('data.html' , value = process_text)

if __name__ =='__main__':
    app.run(host = '0.0.0.0' , port=8080 , debug=True)
