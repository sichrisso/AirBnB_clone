#!/usr/bin/env python3
"""
models module documentation

storage is a singleton to FileStorage
and reload objects to file.json
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
