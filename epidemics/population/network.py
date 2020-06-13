import epidemics.cfg as cfg

import networkx as nx
import numpy as np
import math

from abc import abstractmethod

# Parameters import
NETWORK_SIZE = cfg.NETWORK_SIZE


class Network:
    def __init__(self, population_stats, neighbours):
        self.population_stats = population_stats
        self.neighbours = neighbours

    @abstractmethod
    def graph_nodes(self):
        pass

    @abstractmethod
    def graph_edges(self):
        pass

    @staticmethod
    def convert_coordinates(coordinate):
        coord = coordinate.split('-')
        decimal_coord = int(coord[0]) + (int(coord[1]) / 60) + (int(coord[2]) / 600)
        try:
            if coord[3]=='S' or coord[3]=='O':
                decimal_coord = -decimal_coord
            return decimal_coord
        except IndexError:
            return decimal_coord

    @staticmethod
    def distance(x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


class NetworkPlot(Network):
    def __init__(self, population_stats, neighbours):
        super().__init__(population_stats, neighbours)

    def graph_nodes(self):
        x = np.zeros([1,NETWORK_SIZE])
        y = np.zeros([1, NETWORK_SIZE])
        for i, node in self.population_stats.items():
            x[0, node['id'] - 1] = (self.convert_coordinates(node['longitude']))
            y[0, node['id'] - 1] = (self.convert_coordinates(node['latitude']))
        return x, y

    def graph_edges(self):
        edges = np.zeros([NETWORK_SIZE, NETWORK_SIZE])
        for i in range(1, NETWORK_SIZE + 1):
            for node in self.neighbours[i]:
                edges[i-1][node-1] = 1
                edges[node-1][i-1] = 1
        return edges


class NetworkX(Network):
    def __init__(self, population_stats, neighbours):
        super().__init__(population_stats, neighbours)

    def graph(self):
        N = nx.Graph()
        pos = self.graph_nodes()
        edges = self.graph_edges()
        N.add_nodes_from(pos.keys())
        N.add_edges_from(edges)
        return N, pos

    def graph_nodes(self):
        pos = dict()
        for k, v in self.population_stats.items():
            pos[k] = (self.convert_coordinates(v['longitude']),
                      self.convert_coordinates(v['latitude']))
        return pos

    def graph_edges(self):
        edges = set()
        for i in range(1, NETWORK_SIZE):
            for node in self.neighbours[i]:
                edges.add((i, node))
        return edges
