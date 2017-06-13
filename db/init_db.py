from sqlalchemy import Column, CHAR, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(CHAR(30))
    fullname = Column(CHAR(30))
    password = Column(CHAR(30))

    def __repr__(self):
       return "<User(name='%s', fullname='%s', password='%s')>" % (
                            self.name, self.fullname, self.password)
	

engine = create_engine('mysql+mysqldb://root:123456@127.0.0.1:3306/practise')
Base.metadata.create_all(engine)


