import numpy as np

# All constants and parameters shared across modules

# network param.
NETWORK_SIZE = 95

# disease param.
K = 5
PTRANS = 0.2
GAMMA = 5

# simulation param.
STEPS = 50

# Paths
POP_PATH = 'C:/Users/victo/Desktop/PythonProjects/Epidemics/data/france_dep.json'
NEIGHBOURS_PATH = 'C:/Users/victo/Desktop/PythonProjects/Epidemics/data/voisin.json'
# network edge matrix
"""edges = np.array([[0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                  [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0],
                  [1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                  [0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0],
                  [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
                  [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]])"""