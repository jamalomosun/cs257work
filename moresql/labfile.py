import psycopg2;

def connection():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="omosunj",
        user="omosunj",
        password="nose648ruby"
    )
    if conn is not None:
        print( "Connection Worked!" )
    else:
        print( "Problem with Connection" )

    return conn;

    

def create_tables():
    conn = connection();

    cur = conn.cursor();


    commands = '''
        
        DROP TABLE IF EXISTS cities;
        CREATE TABLE cities (
            city text,
            state text,
            city_pop int,
            latitutde real,
            longitude real
        );
    
        DROP TABLE IF EXISTS states;
        CREATE TABLE states (
            state text,
            abbreviations text
        );

        DROP TABLE IF EXISTS state-pop;
        CREATE TABLE state-pop (
            code text
            state text
            state_pop int
        );
        '''
    

    cur.execute(commands);

    conn.commit();

    print("W")


    print();

def runQueries():
    conn = connection();
    cur = conn.cursor();

    if conn is not None:
        cur.execute("CREATE VIEW cities_states AS SELECT * FROM cities JOIN state-pop on cities.state = state-pop.state;")
        cur.execute("SELECT  city-pop,  CAST(city-pop AS REAL) AS realcitypop FROM cities_states;")
        cur.execute("SELECT   realcitypop,  (realcitypop / state_pop) AS pop_prop FROM cities_states;")



    print()

def main():

    connection()
    create_tables()

main()