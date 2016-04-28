from skills import Match as SkillsMatch
from skills.elo import EloGameInfo, EloCalculator


class EloService(object):
    def __init__(self):
        self.calculator = EloCalculator()

    def update(self, match, session):
        ranking = [1, 2] if match.winner == match.user_1 else [2, 1]
        skills_match = SkillsMatch(
            [{1: match.user_1.elo}, {2: match.user_2.elo}],
            ranking)
        new_ratings = self.calculator.new_ratings(skills_match)
        print(new_ratings)
        match.user_1.elo = new_ratings.rating_by_id(1).mean
        match.user_2.elo = new_ratings.rating_by_id(2).mean
        session.add(match.user_1)
        session.add(match.user_2)
        session.commit()
