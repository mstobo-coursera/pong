from database import db_session
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema
from models import User, Match

class UserSchema(ModelSchema):
    ratings = fields.Method('get_ratings')

    class Meta:
        model = User
        sqla_session = db_session

    def get_ratings(self, user):
        return {'elo': 1000}


class MatchSchema(ModelSchema):
    class Meta:
        model = Match
        sqla_session = db_session
