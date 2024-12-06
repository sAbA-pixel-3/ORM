# Second here



from sqlalchemy import String, Integer, Column, ForeignKey, Date, create_engine
from sqlalchemy.orm import relationship, sessionmaker, Mapped, mapped_column, DeclarativeBase
from config1 import MYSQL_URL


class Base(DeclarativeBase):
    pass

# class Country(Base):
#     __tablename__ = "countries"

#     id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
#     name: Mapped[str] = mapped_column(String(50), nullable=False)
#     president: Mapped[str] = mapped_column(String(50))
#     population: Mapped[int] = mapped_column(Integer, nullable=False)
#     language: Mapped[str] = mapped_column(String(50), nullable=False)
#     flag: Mapped[str] = mapped_column(String(50), nullable=False)
#     date_of_creation: Mapped[Date] = mapped_column(Date) 
#     cities = relationship("City", back_populates="country") 

# class City(Base):
#     __tablename__ = "cities"

#     id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
#     name: Mapped[str] = mapped_column(String(50), nullable=False)
#     population: Mapped[int] = mapped_column(Integer, nullable=False)

#     country_id: Mapped[int] = mapped_column(ForeignKey("countries.id"))
#     country = relationship("Country", back_populates="cities")

# engine = create_engine(MYSQL_URL, echo=True)

# Base.metadata.create_all(engine) 




class Charcter(Base): # URL
    __tablename__ = "characters"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    char_class: Mapped[str] = mapped_column(String(30), nullable=False) 
    status: Mapped[str] = mapped_column(String(30), nullable=False)
    abilities = relationship("Ability", back_populates="character") 

class Ability(Base): # MOVIES, SERIES 
    __tablename__ = "abilities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    ability1: Mapped[str] = mapped_column(String(30), nullable=False)
    ability2: Mapped[str] = mapped_column(String(30), nullable=False)
    ability3: Mapped[str] = mapped_column(String(30), nullable=False) 

    character_id: Mapped[int] = mapped_column(ForeignKey("characters.id"))
    character = relationship("Charcter", back_populates="abilities") 

engine = create_engine(MYSQL_URL, echo=True)
Base.metadata.create_all(engine) 

























