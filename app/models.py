from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    country = db.Column(db.String(120), index=True)
    business_cases = db.relationship('BusinessCase', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<user {}>'.format(self.username)


class BusinessCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), index=True)
    problem = db.Column(db.String(250))
    solution = db.Column(db.String(250))
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'))
