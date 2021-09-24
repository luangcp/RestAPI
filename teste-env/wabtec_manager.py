#!/usr/bin/env python

import random
import requests
from genericpath import isfile
from os.path import dirname, realpath, isfile
from json import dump, load


class JsonManager:

    def __init__(self):
        self.path = dirname(realpath(__file__)) + '/'

    def create_json(self, file):
        
        wabtec_manager = {"DDDs": [], "CNPJs": []}
        path_wabtec_manager_json = self.path + file

        if not isfile(path_wabtec_manager_json):
            with open(path_wabtec_manager_json, 'w') as f:
                dump(wabtec_manager, f, indent=2)
            return True
        else:
            return False


# Lendo o JSON

    def read_json(self, file):
        if isfile(self.path + file):
            with open(self.path + file) as f:
                data = load(f)
            return data
        else:
            return False


if __name__ == '__main__':
    jmanager = JsonManager()
    jmanager.create_json('data/data.json')

    # Lendo ddds

    DDDs = (jmanager.read_json('data/data.json')['ddds'])
    print(DDDs)

    aleatorio = random.choice(DDDs)
    print(random.choice(DDDs))

    # Lendo cnpjs
    #print(jmanager.read_json('data/data.json')['cnpjs'])

    