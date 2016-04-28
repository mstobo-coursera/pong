from database import db_session
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema
from models import User, Match

class UserSchema(ModelSchema):
    class Meta:
        model = User
        sqla_session = db_session


class MatchSchema(ModelSchema):
    class Meta:
        model = Match
        sqla_session = db_session
