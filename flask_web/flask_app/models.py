import time

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer(), unique=True, nullable=False)
    name = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(11), nullable=False)
    created_time = db.Column(db.Integer(), default=int(time.time()), nullable=False)

    def __str__(self):
        return 'User{name=%s,phone=%s}' % (self.name, self.phone)
