import json
from flask import Flask, request, jsonify, render_template
from flask_bootstrap import Bootstrap
from flask_util_js import FlaskUtilJs
from database import init_db, db_session
from models import User, Match
from schemas import UserSchema, MatchSchema
from services import EloService


app = Flask(__name__)
init_db()
Bootstrap(app)
fujs = FlaskUtilJs(app)

userSchema = UserSchema()
matchSchema = MatchSchema()
elo_service = EloService()

@app.context_processor
def inject_fujs():
    return dict(fujs=fujs)


@app.route('/user', methods=['POST'])
def create_user():
    user = userSchema.load(request.json).data
    db_session.add(user)
    db_session.commit()
    return jsonify(**userSchema.dump(user).data)


@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = db_session.query(User).get(user_id)
    return jsonify(**userSchema.dump(user).data)


@app.route('/match', methods=['POST'])
def create_match():
    match = matchSchema.load(request.json).data
    elo_service.update(match, db_session)
    db_session.add(match)
    db_session.commit()
    return jsonify(**matchSchema.dump(match).data)


@app.route('/match/<int:match_id>', methods=['GET'])
def get_match(match_id):
    match = db_session.query(Match).get(match_id)
    return jsonify(**matchSchema.dump(match).data)


@app.route('/leaderboard')
def get_leaderboard():
    return render_template("leaderboard.html", users=[{"rank": 0, "name": "Corey", "rating": 1200, "wins": 100, "losses": 50}])


@app.route('/record_match', methods=["GET", "POST"])
def record_match():
    print(request.path)
    print(request.json)
    return render_template("record_match.html",
                           users=[{"id": 0, "rank": 0, "name": "Corey", "rating": 1200, "wins": 100, "losses": 50},
                                  {"id": 1, "rank": 1, "name": "Matt", "rating": 1200, "wins": 100, "losses": 50}])


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run(debug=True)
