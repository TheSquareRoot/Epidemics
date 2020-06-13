import epidemics.cfg as cfg

import random
import math

from abc import abstractmethod
from uuid import uuid4
import os

# Parameters import
NETWORK_SIZE = cfg.NETWORK_SIZE

# TODO: Linux/Mac compatibility
# TODO: Take into account age groups

class Population:
    def __init__(self, habitants, agents, population_stats, size=0, fromjson=True):
        self.habitants = habitants
        self.agents = agents
        self.population_stats = population_stats
        self.size = size
        self.fromjson = fromjson

    @abstractmethod
    def generate(self):
        """ Generates global population"""
        pass

    @abstractmethod
    def generate_local(self, pos):
        pass

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
    def __init__(self, habitants, agents, population_stats, size=0, fromjson=True):
        super().__init__(habitants, agents, population_stats, size, fromjson)

    def generate(self):
        # Compiling c++ file
        os.chdir('C:/Users/victo/Desktop/PythonProjects/Epidemics/lib')
        os.system("echo ...compilating")
        os.system('g++ main.cpp')
        os.system("echo ...running")
        for pos in range(NETWORK_SIZE):
            self.generate_local(pos)
        # Reads population.txt and stores data in agents and habitants
        with open('C:/Users/victo/Desktop/PythonProjects/Epidemics/data/population.txt') as f:
            for line in f:
                values = list(map(int, line.split()))
                uid = random.randint(0, 1000000000)
                agent = {
                    'age': values[0],
                    'sex': values[1],
                    'prevposition': values[2],
                    'position': values[2],
                    'state': 1
                }
                self.agents[uid] = agent
                self.habitants[values[2]].add(uid)
        # Remove executable and .txt file
        os.system('del a.exe')
        os.chdir('../data')
        os.system('del population.txt')


    def generate_local(self, pos):
        if self.fromjson:
            size = self.population_stats[pos]['size']
        else:
            size = self.size
        # Runs c++ file
        os.system(f'a.exe {size} {pos} {random.randint(0,1000000)}')
