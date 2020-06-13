import epidemics.population.population as population
import epidemics.population.network as network
import epidemics.cfg as cfg
import display

import json


# Parameters import
NETWORK_SIZE = cfg.NETWORK_SIZE
POP_PATH = cfg.POP_PATH
NEIGHBOURS = cfg.NEIGHBOURS_PATH

def main():
    # Population stats dictionnary
    print('... loading data')
    population_stats = dict()
    with open(POP_PATH) as json_file:
        data = json.load(json_file)
        for p in data:
            population_stats[int(p)] = data[p]
    neigbours = dict()
    with open(NEIGHBOURS) as json_file:
        data = json.load(json_file)
        for p in data:
            neigbours[int(p)] = data[p]

    # Network generation
    print('... generating network')
    net = network.NetworkX(population_stats, neigbours)
    N, pos = net.graph()

    # Population generation
    print('... generating population')
    habitants = [set() for _ in range(NETWORK_SIZE)]
    agents = dict()
    pop = population.CppPopulation(habitants, agents, population_stats)
    pop.generate()

if __name__ == '__main__':
    main()
