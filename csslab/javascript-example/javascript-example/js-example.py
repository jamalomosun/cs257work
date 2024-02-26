from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    message = "Welcome good sir. It is time to go to sleep now."
    return render_template("sleepy.html", messText= message)


@app.route('/Hello')
def hello():
    message = "Welcome good sir. It is time to go to sleep now"
    return render_template("sleepy.html", )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5130) 
