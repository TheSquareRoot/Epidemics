import epidemics.cfg as cfg

from abc import abstractmethod
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Parameters imports
NETWORK_SIZE = cfg.NETWORK_SIZE


class Display:
    @abstractmethod
    def display_network(self):
        pass


class DisplayPlot(Display):
    def __init__(self, x, y, edges):
        self.x = x
        self.y = y
        self.edges = edges

    def display_network(self):
        # Plotting
        plt.clf()
        for i in range(NETWORK_SIZE):
            for j in range(i, NETWORK_SIZE):
                if self.edges[i,j]==1:
                    plt.plot([self.x[0, i], self.x[0, j]],
                             [self.y[0, i], self.y[0, j]],
                             color='b', linewidth='0.5')
        plt.scatter(self.x, self.y, marker='.', color='k')

        plt.title('France network')

        plt.show()


class DisplayX(Display):
    def __init__(self, N, pos):
        self.N = N  # Graph
        self.pos = pos

    def display_network(self):
        plt.clf()

        nx.draw(self.N, self.pos,
                with_labels=False,
                node_size=70,
                width=0.4)

        plt.savefig('network.svg')

        plt.show()
