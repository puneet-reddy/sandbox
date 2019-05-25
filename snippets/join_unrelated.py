#!/usr/bin/env pyton

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)
    def __repr__(self):
       return "<User(name='%s', fullname='%s', password='%s')>" % (
                            self.name, self.fullname, self.password)

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, nullable=False)
    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address

engine = create_engine('sqlite:///:memory:', echo=True)

Session = sessionmaker(bind=engine)
sess = Session()

Base.metadata.create_all(engine)

u1 = User(id=1, name='Ein')
sess.add(u1)
u2 = User(id=2, name='Zwei')
sess.add(u2)

a1 = Address(id=1, email_address='test1@test.com', user_id=1)
sess.add(a1)
a2 = Address(id=2, email_address='test2@test.com', user_id=1)
sess.add(a2)
a3 = Address(id=3, email_address='test3@test.com', user_id=1)
sess.add(a3)
sess.commit()

#Here's the magic!
res = sess.query(User, Address).\
    join(Address, User.id == Address.user_id)\
    .filter(Address.id==1).all()
