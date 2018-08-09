#!/usr/bin/python

import psycopg2
from config import config


def insert_pet(pet_name, pet_age, pet_type):
    """ insert a new pet into the petss table """
    sql = """INSERT INTO pets(pet_name, pet_age, pet_type)
             VALUES(%s, %s, %s) RETURNING pet_id;"""
    conn = None
    pet_id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (pet_name, pet_age, pet_type))
        # get the generated id back
        pet_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return pet_id


if __name__ == '__main__':
    # insert one vendor
    insert_pet("asdfasdf", 7, "asdfasdfasf")
