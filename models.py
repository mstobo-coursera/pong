import sqlalchemy as db
from sqlalchemy.orm import relationship, backref
from database import Base


class PongMixin(object):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), onupdate=db.func.now())


class User(PongMixin, Base):
    __tablename__ = 'users'
    name = db.Column(db.String(255), unique=True, nullable=False)
    elo = db.Column(db.Float, nullable=False, default=1000)

    def matches(self):
        return self.matches1 + self.matches2


class Match(PongMixin, Base):
    __tablename__ = 'matches'
    user_1_id = db.Column(
        db.Integer, db.ForeignKey('users.id'), nullable=False)
    user_2_id = db.Column(
        db.Integer, db.ForeignKey('users.id'), nullable=False)
    winner_id = db.Column(
        db.Integer, db.ForeignKey('users.id'), nullable=False)
    user_1_score = db.Column(db.Integer, nullable=False)
    user_2_score = db.Column(db.Integer, nullable=False)

    user_1 = relationship(
        'User', foreign_keys=[user_1_id], backref=backref('matches1'))
    user_2 = relationship(
        'User', foreign_keys=[user_2_id], backref=backref('matches2'))
    winner = relationship('User', foreign_keys=[winner_id])
