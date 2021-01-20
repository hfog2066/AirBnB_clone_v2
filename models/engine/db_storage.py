#!/usr/bin/python3
"""implement new storage engine to interact with database using sqlalchemy
ORM - DBStorage"""

from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.user import User


CLASSES = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class DBStorage:
    """interacts with the MySQL server"""
    __engine = None
    __session = None

    def __init__(self):
        USER = getenv('HBNB_MYSQL_USER')
        PWD = getenv('HBNB_MYSQL_PWD')
        HOST = getenv('HBNB_MYSQL_HOST')
        DB = getenv('HBNB_MYSQL_DB')
        ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(USER, PWD, HOST, DB),
                                      pool_pre_ping=True)
        if ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        if cls is None:
            for c in CLASSES.values():
                for obj in self.__session.query(c).all():
                    key = type(obj).__name__ + "." + obj.id
                    del obj.__dict__["_sa_instance_state"]
                    new_dict[key] = obj
        else:
            for obj in self.__session.query(cls).all():
                key = type(obj).__name__ + "." + obj.id
                del obj.__dict__["_sa_instance_state"]
                new_dict[key] = obj

            return (new_dict)

    def new(self, obj):
        """add obj to the current database session."""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database and initialize session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.close()
