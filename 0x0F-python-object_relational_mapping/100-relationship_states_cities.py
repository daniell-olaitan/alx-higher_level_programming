#!/usr/bin/python3
"""Creates a city and links it to a state
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name='California')
    san_franscisco = City(name='San Francisco')
    san_franscisco.state = california

    session.add(san_franscisco)
    session.commit()
    session.close()
