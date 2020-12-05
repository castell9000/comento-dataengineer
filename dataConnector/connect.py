import json
import pymysql
import sqlalchemy as db

def connect():
    ''' DB 커넥션 만들기, pymysql 패키지가 필요함 '''
    with open('config.json', 'r') as f:
        config = json.load(f)

    db_host = config['database']['host']
    db_user = config['database']['user']
    db_port = config['database']['port']
    db_password = config['database']['password']
    db_database = config['database']['database']
    conn = pymysql.connect(host=db_host, port=db_port, user=db_user, password=db_password, db=db_database)

    return conn