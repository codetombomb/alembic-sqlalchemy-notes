from datetime import datetime
from models import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from random import randint

engine = create_engine("sqlite:///data.db")
Session = sessionmaker(engine)

fake = Faker()  # https://faker.readthedocs.io/en/master/fakerclass.html#upgrade-guide

users = [
    User(first_name="tombomb", last_name="tobar", birthday=datetime(1985, 9, 7)),
    User(first_name="mommytoad", last_name="tobar", birthday=datetime(1989, 3, 21)),
    User(first_name="kitty", last_name="tobar", birthday=datetime(2009, 12, 11)),
    User(first_name="buddy", last_name="tobar", birthday=datetime(2014, 3, 17)),
    User(first_name="quinny", last_name="tobar", birthday=datetime(2020, 6, 11)),
]

for _ in range(10):
    user = User(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        birthday=datetime(randint(1950, 2016), randint(1, 12), randint(1, 28))
    )
    users.append(user)

if __name__ == "__main__": # If this file is called directly
    with Session() as session:
        session.query(User).delete()
        session.commit()
        session.add_all(users) # Add all users in the users list
        session.commit()
        
        # ---- Using a loop ----
        # for user in users:
        #     session.add(user)
        #     session.commit()
