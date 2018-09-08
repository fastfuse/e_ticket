from datetime import datetime

import pytz
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from application import db, login
import enum


class BaseMixin:
    """
    Add some convenience methods
    """

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class User(db.Model, BaseMixin, UserMixin):
    """
    Model represents User instance
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column('username', db.String(20), unique=True)
    password_hash = db.Column('password', db.String)

    is_admin = db.Column('admin', db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Ticket(db.Model, BaseMixin):
    """
    Model represents E-Ticket (RFID Tag) object
    """

    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column('uid', db.String, unique=True)
    added = db.Column('added', db.DateTime, default=datetime.utcnow)
    available_trips = db.Column('available_trips', db.Integer, default=1)


class Reader(db.Model, BaseMixin):
    """
    Model represents RFID reader device (w/ unique ID)
    """
    __tablename__ = 'readers'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column('uid', db.String, unique=True)


class Vehicle(db.Model, BaseMixin):
    """
    Model represents public transport vehicle (w/ unique ID)
    """
    __tablename__ = 'vehicles'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column('uid', db.String, unique=True)


class Transaction(db.Model, BaseMixin):
    """
    Model represents payment transaction.
    Required for validation
    """
    __tablename__ = 'transactions'

    class Statuses(enum.Enum):
        success = 'Success'
        failure = 'Failure'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String, unique=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    ticket_id = db.Column(db.Integer, db.ForeignKey('tags.id'))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    status = db.Column(db.Enum(Statuses))

    ticket = db.relationship('Ticket',
                             backref=db.backref('transactions', lazy='dynamic'))

    vehicle = db.relationship('Vehicle',
                              backref=db.backref('transactions', lazy='dynamic'))

    def __init__(self, uid, ticket_id, vehicle_id, status='failure'):
        self.uid = uid
        self.ticket_id = ticket_id
        self.vehicle_id = vehicle_id
        self.status = status
        self.timestamp = pytz.timezone('Europe/Kiev').fromutc(datetime.now().replace(microsecond=0))
