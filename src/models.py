from flask_sqlalchemy import SQLAlchemy
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class FavouritePlanets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    planet_id = db.Column(db.Integer, ForeignKey('planets.id'))
    
    def __repr__(self):
        return '<FavouritePlanets %r>' % self.character_id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id
        }

class FavouriteCharacters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    character_id = db.Column (db.Integer, ForeignKey('characters.id'))

    def __repr__(self):
        return '<FavouriteCharacters %r>' % self.character_id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(250), nullable=False)
    planet_climate = db.Column(db.String(250), nullable=False)
    planet_gravity = db.Column(db.String(250), nullable=False)
    planet_orbital_period = db.Column(db.Integer)
    planet_population = db.Column(db.Float)

    def __repr__(self):
        return '<Planets %r>' % self.planet_name

    def serialize(self):
        return {
            "id": self.id,
            "planet_name": self.planet_name,
            "planet_climate": self.planet_climate,
            "planet_gravity": self.planet_gravity,
            "planet_orbital_period": self.planet_orbital_period,
            "planet_population": self.planet_population
        }

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(250), nullable=False)
    character_gender = db.Column(db.String(250), nullable=False)
    character_skin_color = db.Column(db.String(250), nullable=False)
    character_birthdate = db.Column(db.String(250), nullable=False)
    character_eye_color = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Characters %r>' % self.character_name

    def serialize(self):
        return {
            "id": self.id,
            "character_name": self.character_name,
            "character_gender": self.character_gender,
            "character_skin_color": self.character_skin_color,
            "character_birthdate": self.character_birthdate,
            "character_eye_color": self.character_eye_color
        }