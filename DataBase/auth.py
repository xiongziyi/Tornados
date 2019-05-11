from mysql_connection import session
from models import User
def add_user():
    #person = User(username = 'xps',password='123')
    #session.add(person)  #增加一条数据
    session.add_all([    #增加多条数据
        User(username = 'xpss',password='123'),
        User(username = 'xpss',password='123'),
        User(username = 'xpsss',password='123'),
    ])
    session.commit() #提交
def search__user():
    rows = session.query(User).all()  ###查询所有
    #rows = session.query(User).first()  ###查询一条
    print(rows)
def update_user():
    rows = session.query(User).filter(User.username == 'xpss').update({User.password:1})# 过滤掉name=xpss， 其余的密码改为1
    session.commit()
def delete_user():
    rows = session.query(User).filter(User.username =='xpss')[0]
    print(rows)
    session.delete(rows)   #删除第一条记录
    #rows.deleted()   #批量删除
    session.commit()

