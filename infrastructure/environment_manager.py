import os

from infrastructure.exceptions import VariableNotFound


class EnvironmentManager:
    def __init__(self):
        pass

    def get(self, key):
        try:
            return os.environ[key]
        except KeyError:
            raise VariableNotFound(f'{key} variable not found')
