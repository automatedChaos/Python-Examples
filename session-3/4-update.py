#!/usr/bin/python

import psycopg2
from config import config


def update_pet(pet_id, pet_name, pet_age, pet_type):
    """ update pet name based on the pet id """
    sql = """ UPDATE pets
                SET pet_name = %s,
                    pet_age = %s,
                    pet_type = %s
                WHERE pet_id = %s"""

    conn = None
    updated_rows = 0

    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql, (pet_name, pet_age, pet_type, pet_id))
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows


if __name__ == '__main__':
    # insert one vendor
    update_pet("1", "Diesy", 7, "Belgian Shepherd")
