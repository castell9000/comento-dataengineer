from dataLogger.logger import logger as datalog
from dataConnector.connect import connect as db
import pandas

if __name__ == '__main__':

    # DB Connection 가져오기
    db_connect = db()
    sql = 'select * from users'

    # pandas sql query
    result = pandas.read_sql_query(sql, db_connect)

    # console, slack 에 결과 보내기
    print(datalog().warn(result.to_json()))
