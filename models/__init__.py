#!/usr/bin/python3
import models.engine.file_storage as file_storage
from models.base_model import BaseModel
dict_of_classes = {"BaseModel": BaseModel}
storage = file_storage.FileStorage()
storage.reload()
