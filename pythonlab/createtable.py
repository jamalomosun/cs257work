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
            population int,
            latitute real,
            longitude real
        );
    
        DROP TABLE IF EXISTS states;
        CREATE TABLE states (
            state text,
            abbreviations text
        );
        '''
    

    cur.execute(commands);

    conn.commit();

    print("W")


    print();

def main():

    connection()
    create_tables()

main()