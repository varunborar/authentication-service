import os
import json


class env:
    _CONF = None

    def __init__(self):
        env._CONF = {}

    @staticmethod
    def get(key=None, default="SHOULD_NOT_USE"):
        if key is None:
            return env._CONF
        elif key in env._CONF:
            return env._CONF[key]
        elif default != "SHOULD_NOT_USE":
            return default
        else:
            raise KeyError(f"Key [{key}] not found in configuration")

    @staticmethod
    def set(key, value):
        env._CONF[key] = value

    @staticmethod
    def loadEnv():
        for key in os.environ:
            env.set(key, os.environ[key])
        return env

    @staticmethod
    def loadFile(path):
        with open(path, 'r') as f:
            for line in f:
                key, value = line.split('=')
                env.set(key, value.strip())
        return env

    @staticmethod
    def loadJson(path):
        env._CONF.update(json.load(open(path, 'r')))
        return env

    @staticmethod
    def loadFromFolder(path):
        for filename in os.listdir(path):
            if filename.endswith('.txt'):
                with open(path + '/' + filename, 'r') as f:
                    env.set(filename.replace('.txt', ''), f.read().strip())
            elif filename.endswith('.json'):
                with open(path + '/' + filename, 'r') as f:
                    env.set(filename.replace('.json', ''), json.load(f))
        return env

    @staticmethod
    def loadFromJson(path):
        env._CONF.update(json.load(open(path, 'r')))
        return env

