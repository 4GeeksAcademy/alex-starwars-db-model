from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'usuarios'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

    # planetas: Mapped['Planetas'] = relationship('Planetas', back_populates = 'user')
    # personajes: Mapped['Personajes'] = relationship('Personajes', back_populates = 'user')
    favoritos: Mapped[list['Favoritos']] = relationship('Favoritos', back_populates = 'user')


    def serialize(self):
        return {
            "id": self.id,
            "name" : self.name,
            "email": self.email,
        }

class Personajes(db.Model):
    __tablename__ = 'personajes'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    hair_color: Mapped[str] = mapped_column(nullable=False)
    eye_color: Mapped[str] = mapped_column(nullable=False)
    gender: Mapped[str] = mapped_column(nullable=False)

    # user: Mapped['User'] = relationship('User', back_populates = 'personajes')

    def serialize(self):
        return {
            "id": self.id,
            "hair_color" : self.hair_color,
            "eye_color": self.eye_color,
            "gender": self.gender,
        }
    
class Planetas(db.Model):
    __tablename__ = 'planetas'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    diameter: Mapped[float] = mapped_column(nullable=False)
    population: Mapped[int] = mapped_column(nullable=False)
    gravity: Mapped[float] = mapped_column(nullable=False)

    # user: Mapped['User'] = relationship('User', back_populates = 'planetas')

    def serialize(self):
        return {
            "id": self.id,
            "name" : self.name,
            "diameter" : self.diameter,
            "population": self.population,
            "gravity": self.gravity,

        }

class Favoritos(db.Model):
    __tablename__ = 'favoritos'
    id: Mapped[int] = mapped_column(primary_key=True)
    usuario: Mapped[int] = mapped_column(ForeignKey("usuarios.id"), nullable=False)
    planeta: Mapped[int] = mapped_column(ForeignKey("planetas.id"), nullable=False)
    personaje: Mapped[int] = mapped_column(ForeignKey("personajes.id"), nullable=False)

    user: Mapped['User'] = relationship('User', back_populates = 'favoritos')

    def serialize(self):
        return {
            "id": self.id,
            "usuario" : self.usuario,
            "planeta": self.planeta,
            "personaje": self.personaje,

        }