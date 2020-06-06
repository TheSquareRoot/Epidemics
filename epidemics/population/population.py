import epidemics.cfg as cfg

import random
import math

import json
import uuid


class Population:
    def __init__(self, habitants, agents):
        self.habitants = habitants
        self.agents = agents

    def generate(self):
        PATH = 'C:/Users/victo/Desktop/PythonProjects/Epidemics/data/france.json'

        population_stats = {}
        with open(PATH) as population_json:
            data = json.load(population_json)
            for p in data:
                population_stats[p['id']] = p

        for i in range(cfg.NETWORK_SIZE):
            local_habitants = set()
            SIZE = population_stats[i]['size']
            # Computes size of each age group from total population
            GROUP1SIZE = math.floor(population_stats[i]['0to19'] * SIZE / 100)
            GROUP2SIZE = math.floor(population_stats[i]['20to39'] * SIZE / 100)
            GROUP3SIZE = math.floor(population_stats[i]['40to59'] * SIZE / 100)
            GROUP4SIZE = math.floor(population_stats[i]['60to74'] * SIZE / 100)
            GROUP5SIZE = SIZE - GROUP1SIZE - GROUP2SIZE - GROUP3SIZE - GROUP4SIZE
            # Generates agents for each age group and adds them to the local population
            for _ in range(GROUP1SIZE):
                self.random_agent(0, 19, i)
            for _ in range(GROUP2SIZE):
                self.random_agent(20, 39, i)
            for _ in range(GROUP3SIZE):
                self.random_agent(40, 59, i)
            for _ in range(GROUP4SIZE):
                self.random_agent(60, 74, i)
            for _ in range(GROUP5SIZE):
                self.random_agent(75, 90, i)

    def random_agent(self, min_age, max_age, position):
        # Randomly generates an agent within the given age range in the given node
        uid = uuid.uuid4()
        age = random.randint(min_age, max_age)
        sex = random.choice(['m', 'f'])
        position = position
        state = 1
        # Updates agent dictionnary
        self.agents[uid] = {
            'age': age,
            'sex': sex,
            'prevposition': position,
            'position': position,
            'state': state
        }
        # Updates habitants
        self.habitants[position].add(uid)


habitants = [set() for _ in range(cfg.NETWORK_SIZE)]
agents = dict()

p = Population(habitants, agents)
p.generate()

print(agents)
