import epidemics.population.population as population
import epidemics.cfg as cfg

import matplotlib.pyplot as plt
import numpy as np

import time


def benchmark():
    population_min = 100
    population_max = 100000
    step = 1000
    sample_size = 10

    pop_size = [i for i in range(population_min, population_max, step)]
    exec_time = []

    # Benchmarking
    for size in pop_size:
        sum_time = 0
        for _ in range(sample_size):
            habitants = [set() for _ in range(cfg.NETWORK_SIZE)]
            agents = {}
            pop = population.CppPopulation(habitants, agents, size=size, fromjson=False)
            # Execution timing
            start_time = time.time()
            pop.generate()
            sum_time += (time.time() - start_time)

        exec_time.append(sum_time / sample_size)
    # Linear fit
    coeffs = np.polyfit(pop_size, exec_time, deg=1)
    fit_time = [(coeffs[0] * i + coeffs[1]) for i in pop_size]
    # Plot
    plt.clf()
    plt.plot(pop_size, exec_time, color='b', marker='o', label='c++ generation')
    plt.plot(pop_size, fit_time, color='r', label=f'linear fit (a={coeffs[0], 2})')

    plt.title('Population generation methods benchmark')
    plt.xlabel('population per node')
    plt.ylabel('execution time (s)')
    plt.legend()

    plt.grid()
    plt.tight_layout()

    plt.show()


if __name__ == '__main__':
    benchmark()
