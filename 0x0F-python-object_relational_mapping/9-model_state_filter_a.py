#!/usr/bin/python3
"""
lists all State objects from the given database that contain 'a'
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()
    for row in session.query(State).filter(
            State.name.contains('a')).order_by(State.id):
        print("{}: {}".format(row.id, row.name))
