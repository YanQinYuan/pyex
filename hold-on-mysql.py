# coding=utf-8
import gen-num

import mysql.connector


def saveNum(date):
    conn = mysql.connector.connect(user='root', password='password', datebase='test',use_unitcode=True)
    for i in data:
        cursor.execute('insert into acNum(acNum) values (%s), i')

    cursor.commit()
    cursor.close()


if __name__ == '__main__':
    data = generate(200)
    saveNum(data)

