from sqlalchemy import Column, Integer, String, DateTime,Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import  datetime
from mysql_connection import  Base

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20))
    password = Column(String(50))
    creatime = Column(DateTime, default=datetime.now)
    def __repr__(self):  ##
        return """<User(id=%s,username=%s,password=%s,creatime=%s)>
            """ % (
            self.id,
            self.username,
            self.password,
            self.creatime,
        )

if __name__=='__main__':
    Base.metadata.create_all()



