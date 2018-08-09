import psycopg2
from config import config

def get_pets():
    """ query data from the vendors table """
    conn = None
    row = {}
    pets = []

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT pet_id, pet_name, pet_age, pet_type FROM pets ORDER BY pet_name")
        print("The number of parts: ", cur.rowcount)

        while row is not None:
            #print(row)
            row = cur.fetchone()

            if (row != None):
                pets.append(row)

        print(pets)

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    # insert one vendor
    get_pets()
