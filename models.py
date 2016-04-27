from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    slack_name = Column(String(255), unique=True)


class Match(Base):
    __tablename__ = 'matches'
    id = Column(Integer, primary_key=True)
    user_1_id = Column(Integer, ForeignKey('users.id'))
    user_2_id = Column(Integer, ForeignKey('users.id'))

    user_1 = relationship(
        'User', foreign_keys=[user_1_id], backref=backref('matches'))
    user_2 = relationship('User', foreign_keys=[user_2_id])
