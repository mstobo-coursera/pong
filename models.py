from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from database import Base


class PongMixin(object):
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now())

class User(PongMixin, Base):
    __tablename__ = 'users'
    name = Column(String(255), unique=True, nullable=False)

    def matches(self):
        return self.matches1 + self.matches2


class Match(PongMixin, Base):
    __tablename__ = 'matches'
    user_1_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user_2_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    winner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user_1_score = Column(Integer, nullable=False)
    user_2_score = Column(Integer, nullable=False)

    user_1 = relationship(
        'User', foreign_keys=[user_1_id], backref=backref('matches1'))
    user_2 = relationship(
        'User', foreign_keys=[user_2_id], backref=backref('matches2'))
    winner = relationship('User', foreign_keys=[winner_id])
