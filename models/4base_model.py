#!/usr/bin/python3

"""
This is the Base class
"""
from models.__init__ import storage
from uuid import uuid4
from datetime import datetime

class BaseModel:

    def __init__(self, *args, **kwargs):
        """
        Inicialize first values for
        atributes: id, created_at, updated_at
        """
        if not kwargs: # Here goes an exeption
            # What if kwargs is empty?
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

        else:
            self.__dict__ = kwargs # unittest, What if not atribute __class__ in dictionary
            if "__class__" in self.__dict__.keys():
                self.__dict__.pop("__class__")
                formato = "%Y-%m-%dT%H:%M:%S.%f"
            self.updated_at = datetime.strptime(self.updated_at, formato)
            self.created_at = datetime.strptime(self.created_at, formato)


    def __str__(self):
        """
        returns string type representation of object instance
        """
        format = "[{}] ({}) {}"

        return format.format(BaseModel.__name__, self.id, self.__dict__)


    def save(self):
        """ updates the public instance attribute updated_at\
         with the current datetime """
        self.updated_at = datetime.utcnow() # "datetime.datetime({})".format(datetime.isoformat(datetime.now()))
        storage.new(self)
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance """
        self.new_dict = self.__dict__.copy()
        self.new_dict["__class__"] = BaseModel.__name__
        self.new_dict["updated_at"] = self.updated_at.isoformat()
        self.new_dict["created_at"] = self.created_at.isoformat()
        return self.new_dict





my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
