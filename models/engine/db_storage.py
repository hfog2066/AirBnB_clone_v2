#!/usr/bin/python3
import sys
import os
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import *
from models.base_model import Base
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        uname = os.environ['HBNB_MYSQL_USER']
        upass = os.environ['HBNB_MYSQL_PWD']
        dbname = os.environ['HBNB_MYSQL_DB']
        host = os.environ['HBNB_MYSQL_HOST']
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(uname, upass, host, dbname))
        if 'HBNB_MYSQL_ENV' in os.environ and \
           os.environ['HBNB_MYSQL_ENV'] == "test":
            Base.metadata.drop_all(self.__engine)

        self.__classes = {"User": User,
                          "Amenity": Amenity, "City": City,
                          "Place": Place, "Review": Review,
                          "State": State}
        self.storage_type = "db"

    def all(self, cls=None):
        retval = {}
        if cls:
            for instance in self.__session.query(self.__classes[cls]):
                retval.update({instance.id: instance})
            return (retval)
        else:
            for cls in ["User", "State", "City", "Amenity", "Place", "Review"]:
                cls = getattr(sys.modules["models"], cls)
                for instance in self.__session.query(cls):
                    retval.update({instance.id: instance})
            return(retval)

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def close(self):
        self.__session.remove()

    def reload(self):
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine))
