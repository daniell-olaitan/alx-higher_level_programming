#!/usr/bin/python3
"""
Defines City class that maps to city table of the given database
"""

import sys
from relationship_state import Base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey


class City(Base):
    """Defines a class that maps to city table of a db"""

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
