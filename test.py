import mysql.connector
import base64
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
def post(time, up, down):
    db = mysql.connector.connect(host=str(config['MYSQL']['host']),
                                 user=str(config['MYSQL']['user']),
                                 passwd=(base64.b64decode(str(config['MYSQL']['passwd']).encode('ascii')).decode('ascii'))
                                 )
    #db = mysql.connector.connect(host= "192.168.0.107", user="charles", passwd = str(input("password: ")))
    cursor = db.cursor()
    cursor.execute("show databases")
    cursor.execute("USE tor_logging") #db name
    cursor.execute("INSERT INTO log(%s,%s,%s)" % (str(datetime.now().strftime("%H:%M")),  ))
    for i in cursor:
        print(i)