import json
from flask import Flask, request, jsonify, render_template
from flask_bootstrap import Bootstrap
from database import init_db, db_session
from models import User, Match
from schemas import UserSchema, MatchSchema
from services import EloService
from sqlalchemy import func

app = Flask(__name__)
init_db()
Bootstrap(app)

userSchema = UserSchema()
matchSchema = MatchSchema()
elo_service = EloService()


@app.route('/user', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        user = userSchema.load(request.json).data
        db_session.add(user)
        db_session.commit()
        return jsonify(**userSchema.dump(user).data)
    else:
        return render_template("user.html")


@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = db_session.query(User).get(user_id)
    return jsonify(**userSchema.dump(user).data)


@app.route('/match', methods=['GET', 'POST'])
def create_match():
    if request.method == 'POST':
        match = matchSchema.load(request.json).data
        elo_service.update(match, db_session)
        db_session.add(match)
        db_session.commit()
        return jsonify(**matchSchema.dump(match).data)
    else:
        users = db_session.query(User).all()
        return render_template("record_match.html", users=users)


@app.route('/match/<int:match_id>', methods=['GET'])
def get_match(match_id):
    match = db_session.query(Match).get(match_id)
    return jsonify(**matchSchema.dump(match).data)


@app.route('/leaderboard')
def get_leaderboard():
    users = sorted(db_session.query(User).all(), key=lambda user: user.elo, reverse=True)
    users = [{'id': user.id, 'name': user.name, 'elo': user.elo, 'rank': i + 1} for i, user in enumerate(users)]
    # print("users: ", users[0].name, users[0].elo, users[0].matches()[0].id, users[0].matches()[1].id)
    # wins_per_user = db_session.query(User.id, func.count(Match.id)).group_by(Match.winner).all()
    matches = db_session.query(Match).all()
    print("length: ", matches[0].winner.id)
    print("winner: ", len(list(filter(lambda match: match.winner == '1', matches))))

    users = list(map((lambda user: {'name': user.get('name'), 'elo': user.get('elo'), 'rank': user.get('rank'),
                                    'games': len(list(filter(lambda match: match.user_1.id == user.get('id')
                                                             or match.user_2.id == user.get('id'), matches))),
                                    'wins': len(list(filter(lambda match: match.winner.id == user.get('id'), matches)))})
                     , users))

    users = list(map((lambda user: {'name': user.get('name'), 'elo': user.get('elo'), 'rank': user.get('rank'),
                                    'games': user.get('games'), 'wins': user.get('wins'),
                                    'losses': user.get('games') - user.get('wins')}), users))

    print("wins per user: ", users)

    return render_template("leaderboard.html", users=users)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run(debug=True)
