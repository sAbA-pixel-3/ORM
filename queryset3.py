# Third here


from models2 import * 
from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session



# session = Session(engine)  
# def add_country(name,president,population,language,flag,date_of_creation):
#     new_country = Country(name=name,president=president,
#     population=population,language=language,flag=flag,
#     date_of_creation=date_of_creation)
#     session.add(new_country)
#     session.commit()

# add_country('Ukraine','Zelensky',40000000,'Ukrainian','Ukraine','1945-01-01')
# add_country('USA', 'Obama', 330000000, 'English', 'USA', '1945-01-01')
# add_country('France', 'Macron', 67000000, 'French', 'France', '1945-01-01')

# def add_city(name, population, country_id):
#     new_city = City(name=name, population=population, country_id=country_id)
#     session.add(new_city)
#     session.commit()

# add_city("Kyiv", 30000, 1)
# add_city("New York", 1341252,  2)
# add_city("Paris", 23785, 3) 


# def get_all_countries():
#     return session.scalars(select(Country)).all()
# countries = get_all_countries()
# for country in countries:
#     print(country.name)


# def get_all_cities():
#     return session.scalars(select(City)).all() 
# cities = get_all_cities()
# for city in cities:
#     print(city.name) 







session = Session(engine) 
def add_character(name, char_class, status):
    new_character = Charcter(name=name, char_class=char_class, status=status)
    session.add(new_character)
    session.commit()
add_character("Superman", "Kryptonian", "active")
add_character("Flash", "Speedster", "retired")
add_character("Aquaman", "Water", "half-active")

def add_ability(ability1, ability2, ability3, character_id):
    new_ability = Ability(ability1=ability1, ability2=ability2, ability3=ability3, character_id=character_id)
    session.add(new_ability)
    session.commit()
add_ability("Immunity", "Heat-vision", "Levitation", 1)
add_ability("Super-speed", "Time-interaction", "Tornado-creation", 2)
add_ability("Wave-control", "Fish-command", "Under-water-breath", 3) 
