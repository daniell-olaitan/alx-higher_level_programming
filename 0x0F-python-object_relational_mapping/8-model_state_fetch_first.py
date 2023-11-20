#!/usr/bin/python3
"""
lists the first State objects from the given database
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
    first_row = session.query(State).order_by(State.id).first()
    if first_row is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_row.id, first_row.name))
