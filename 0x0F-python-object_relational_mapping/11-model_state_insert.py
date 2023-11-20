#!/usr/bin/python3
"""
Script adds a state object to the given database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    db_uri = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = State(
        name="Louisiana"
    )

    session.add(state)
    session.commit()
    print(state.id)
    session.close()
