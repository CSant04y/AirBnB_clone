#!/usr/bin/python3
"""[This class serializes instances to a JSON file and deserializes JSON file to instances]
"""

import json
import os.path


class FileStorage:
    """[This serializes instances to a JSON file
        and deserializes JSON file to instances]
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """[This Returns the dictonary called __objects]
        """
        return self.__objects

    def new(self, obj):
        """[Adding an object in the dictionary object]

        Args:
            obj: [This is the object set into __objects
            with key <obj class name>.id]
        """
        self.__objects[type(obj).__name__ + "." + str(obj.id)] = obj

    def save(self):
        """[This serializes __objects to the JSON file]
        """
        new_dict = {}
        for key in self.__objects:
            new_dict[key] = self.__objects[key].to_dict()

        with open(self.__file_path, "w") as FILE:
            FILE.write(json.dumps(new_dict))
    
    def reload(self):
        """[deserializes the JSON file to __objects]
        """
        dict_grayson = {}

        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as FILE:
                dict_grayson = json.loads(FILE.read())
                print("This is dict_grayson = {}".format(dict_grayson))

                for x in dict_grayson:
                    tmp = dict_grayson[x]
                    print("This is tmp {}".format(tmp["__class__"]))
                    self.__objects[x] = tmp["__class__"](x)
                    self.new(tmp)
