import os
import pymysql
from flask import jsonify

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')


def open_connection():
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    try:
        print("------hjgjf0--------",os.environ.get('GAE_ENV'))
        if os.environ.get('GAE_ENV') == 'standard':
            conn = pymysql.connect(user=db_user, password=db_password,
                                unix_socket=unix_socket, db=db_name,
                                cursorclass=pymysql.cursors.DictCursor
                                )
    except pymysql.MySQLError as e:
        print(e)

    return conn


def get_inspiring_women_in_category(specialization):
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM inspiringwomen WHERE specialization = {};',specialization)
        iw = cursor.fetchall()
        if result > 0:
            got_iw = jsonify(iw)
        else:
            got_iw = 'No inspiring women in DB'
    conn.close()
    return got_iw

def add_inspiring_women(iw):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute('INSERT INTO inspiringwomen (name, field, bio, age, country, specialization) VALUES(%s, %s, %s, %s, %s, %s)', (iw["name"], iw["field"], iw["bio"], iw["age"], iw["country"], iw["specialization"]))
    conn.commit()
    conn.close()