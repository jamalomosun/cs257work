from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index.html")
    #return render_template("storygen.html")

@app.route('/test')
def name():
    listOfNames = ["Alice","Bob", "Jessica", "James", "Jack", "Zoe"]
    listOfAdjectives = ["Wise", "Foolish", "Proud", "Accomplished", "Shameless", "Brave"]
    
    num = random.randint(0, 6) 
    num2 = random.randint(0, 6)
    year = random.randint(1940,2022)

    story = listOfNames[num] + " the " + listOfAdjectives[num2] + " was born in [blank] in " + str(year)
    return render_template("storygen.html", randStory = story);



@app.route('/rand/<low>/<high>')
def rand(low, high):
    #Input values that come from a URL (i.e., @app.route)
    #   are always strings so I need to convert the type to int
    low_int = int(low)
    high_int = int(high)
    
    num = random.randint(low_int, high_int)
    return render_template("random.html", randNum = num)

if __name__ == '__main__':
    my_port = 5130
    app.run(host='0.0.0.0', port = my_port) 
