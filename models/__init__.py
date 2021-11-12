#!/bin/usr/python3
"""
Module for initializing model modules
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

