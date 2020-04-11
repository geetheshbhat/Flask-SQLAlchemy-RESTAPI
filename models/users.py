import sqlite3
from db import db

class UserRegister(db.Model):
    __tablename__='users'

    id=db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(80))
    last_name=db.Column(db.String(80))
    age=db.Column(db.Integer)

    def __init__(self, first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    
    def json(self):
        return {'first_name':self.first_name,'last_name':self.last_name,'age':self.age}
    
    @classmethod
    def find_by_name(cls,first_name):
        return cls.query.filter_by(first_name=first_name).first()

    def insert_user(self):
        db.session.add(self)
        db.session.commit()

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()
