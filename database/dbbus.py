#-*- coding: utf-8 -*-

import sys

#import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()

engine = create_engine('mysql+mysqldb://root:zhuta08oo928@localhost:3306/test')
DBSession = sessionmaker(bind = engine)

class DBBus:
    '''
    This class for DataBase API
    '''
    def __init__(self):
        self.session = None

    def createTable(self):
        BaseModel.metadata.create_all(engine)


    def dropTable(self):
        BaseModel.metadata.drop_all(engine)


    def openSession(self):
        self.session = DBSession()


    def closeSession(self):
        if self.session:
            self.session.close()
            self.session = None


    def executeSql(self, sql, no = None):
        ret = self.session.execute(sql)

        return ret

        
    def adddata(self, TABLE):
        self.session.add(TABLE)
        self.session.commit()

        


#########################################################################
class Test(BaseModel):
    __tablename__ = 'mytest'

    id = Column(Integer, primary_key = True)
    name = Column(String(20))


    
    
def test():
    db =DBBus()

    db.createTable()
    db.openSession()

    ret = db.executeSql('desc mytest')
    for i in ret:
        print i

    i = 0
    while i < 100:
        test = Test(name = 'test name %d' % i)
        db.adddata(test)
        i = i + 1
        
    ret = db.executeSql('select * from mytest')
    for i in ret:
        print i

    db.closeSession()
    db.dropTable()
    

        
if __name__ == '__main__':
    if len(sys.argv) == 1:
        exit()

    if sys.argv[1] == 'test':
        test()