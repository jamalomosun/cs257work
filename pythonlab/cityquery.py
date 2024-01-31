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
            latitude real,
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

def citySearch():
    conn = connection()
    if conn is not None:
        conn = connection()
        cur = conn.cursor()
        print("Determine if Northfield is present in the database. If it is, print its location (Latitude and Longitude). If it is not, print an appropriate message for the user.")
        cur.execute("SELECT city, population, latitude, longitude FROM cities WHERE city = 'Northfield'; ")
        result = cur.fetchone()

        print("Print out the name of the city with the largest population.")
        cur.execute("SELECT city, MAX(population) FROM cities; ")
        result = cur.fetchone()

        print("Print out the name of the city in Minnesota with the smallest population.")
        cur.execute("SELECT city, MIN(population), state FROM cities WHERE state = 'Minnesota';")
        result = cur.fetchone()

        print("Print out the names of the cities that is furthest North, furthest East, furthest South, and furthest West")
        cur.execute("SELECT city FROM cities WHERE MAX(longitude) OR MIN(longitude) OR MAX(latitude) OR MIN(latitude);")
        result = cur.fetchall()

        print("Print out the names of the cities that is furthest North, furthest East, furthest South, and furthest West")
        cur.execute("SELECT city FROM cities WHERE MAX(longitude) OR MIN(longitude) OR MAX(latitude) OR MIN(latitude);")
        result = cur.fetchall()

        print("Have the user enter a State from the keyboard. Print the Total population of all the cities in that state. The user should be able to enter either an abbreviation or the full name of the sate. If the user enters an abbreviation, then you should look up the abbreviation in the second table to learn the full name of the state.")
        stateInput = input("Please enter a state or abbreviation")

        if len(stateInput) == 2:
            stateInput = stateInput.upper()
        else:
            stateInput = stateInput.capitalize()

        sql = '''

            SELECT SUM(population)
            FROM (
                SELECT *
                FROM states table1
                    JOIN cities table2 on table2.state = table1.state
                WHERE '%s' = table1.abbreviations
                    OR '%s' = table2.state
            ) as popProportion;

        ''' % (stateInput, stateInput)


        cur.execute(sql)
        result = cur.fetchall()

def main():

    connection()
    create_tables()
    citySearch()

    



main()