import flask
import psycopg2;


app = flask.Flask(__name__)

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="omosunj",
    user="omosunj",
    password="nose648ruby"
)

#
@app.route('/hello')
def my_function():
    return "Hello World!"

@app.route('/display/<word1>/<word2>')
def my_display(word1, word2):
    the_string = "The words are: " + word1 + " and " + word2;
    return the_string

@app.route('/color/<word1>')
def my_color(word1):
    return '<h1 style="color:Green">' + word1 + '</h1>'

@app.route('/add/<num1>/<num2>')
def my_sum(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    sumNum = num1 + num2
    sumNum = str(sumNum)
    return sumNum

@app.route('/pop/<abbrev>')
def my_pop(abbrev):
    my_abbreviation = abbrev
    cur = conn.cursor()
    commands = '''
        
        DROP TABLE IF EXISTS statepop;
        CREATE TABLE statepop (
            code text,
            state text,
            pop int,
        ) as state_pop;

        '''
    flaskdb = '''SELECT * FROM state_pop WHERE '%s' = code ''' %(my_abbreviation)
    cur.execute(commands);
    cur.execute(flaskdb);
    result = cur.fetchall()
    return (str(result))

if __name__ == '__main__':
    my_port = 5130
    app.run(host='0.0.0.0', port = my_port) 
