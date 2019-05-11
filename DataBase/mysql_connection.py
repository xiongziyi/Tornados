from sqlalchemy import create_engine
from  CONFIGS import configs
import  pymysql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
db_url = 'mysql+pymysql://{}:{}@{}/{}?charset=utf8'.format(configs['USERNAME'],configs['PASSWORD'],configs['HOSTNAME'],configs['DATABASE'])
engine = create_engine(db_url)
Base = declarative_base(engine)  ####基类
##增删改查
#创建会话
Session = sessionmaker(engine)
session = Session()  #实例
if __name__=="__main__":
    connection = engine.connect()
    result = connection.execute('select 1')
    print(result.fetchone())












class  SQL_CONNECTION():
    def __int__(self):
        self.username = configs['USERNAME']
        self.password = configs['PASSWORD']
        self.hostname = configs['HOSTNAME']
        self.database = configs['DATABASE']
        self.egine= create_engine('mysql+pymysql://{}:{}@{}/{}?charset=utf8'.format(self.username,self.password,self.hostname,self.database))


        connection = self.egine.connect()
        result = connection.execute('select * from user_info ')
        print( result.fetchall())







# conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='project')
# cursor = conn.cursor()
# name = "xzy"
# password = "123456"
# temp = "insert into user_info (user_name,user_password) values ('%s','%s')" % (name, password)
# effect_row = cursor.execute(temp)
# result = cursor.fetchone()
# conn.commit()
# cursor.close()
# conn.close()