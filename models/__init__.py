#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""

from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.city import City


TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')
if TYPE_STORAGE == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
