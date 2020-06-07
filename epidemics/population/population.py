import epidemics.cfg as cfg

import multiprocessing as mp
import random
import math
import json

from abc import abstractmethod
from uuid import uuid4
import os

# Parameters import
NETWORK_SIZE = cfg.NETWORK_SIZE


class Population:
    def __init__(self, habitants, agents, size=0, fromjson=True):
        self.habitants = habitants
        self.agents = agents
        self.size = size
        self.fromjson = fromjson

    @abstractmethod
    def generate(self):
        """ Generates global population"""
        pass

    @abstractmethod
    def generate_local(self, position):
        """ Generates population in the given node """
        pass

    def update(self, age_range, group_size, position):
        for _ in range(group_size):
            uid, agent = self.random_agent(age_range, position)
            self.agents[uid] = agent
            self.habitants[position].add(uid)

    @staticmethod
    def random_agent(age_range, position):
        # Randomly generates an agent within the given age range in the given node
        uid = uuid4()
        agent = {
            'age': random.randint(age_range[0], age_range[1]),
            'sex': random.choice(['m', 'f']),
            'prevposition': position,
            'position': position,
            'state': 1
        }
        return uid, agent


class CppPopulation(Population):
    def __init__(self, habitants, agents, size=0, fromjson=True):
        super().__init__(habitants, agents, size, fromjson)

    def generate(self):
        path = 'C:/Users/victo/Desktop/PythonProjects/Epidemics/data/france.json'

        population_stats = {}
        with open(path) as population_json:
            data = json.load(population_json)
            for p in data:
                population_stats[p['id']] = p

        if self.fromjson:
            size = population_stats[1]['size']
        else:
            size = self.size

        # Compiles and runs c++ file
        os.chdir('C:/Users/victo/Desktop/PythonProjects/Epidemics/lib')
        os.system("echo ...compilating")
        os.system('g++ main.cpp')
        os.system("echo ...running")
        os.system(f'a.exe {size}')
        # Reads population.txt and stores data in agents and habitants
        keys = ['age', 'sex', 'prevposition', 'position', 'state']
        with open('C:/Users/victo/Desktop/PythonProjects/Epidemics/lib/population.txt') as f:
            for line in f:
                agent = {}
                values = line.split()
                for index, key in enumerate(keys):
                    agent[key] = int(values[index + 1])
                self.agents[values[0]] = agent
                self.habitants[int(values[3])].add(int(values[0]))

    def generate_local(self, position):
        pass
