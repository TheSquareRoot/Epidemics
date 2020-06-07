import epidemics.population.population as population
import epidemics.cfg as cfg

import matplotlib.pyplot as plt
import numpy as np

import time


def benchmark():
    population_min = 100
    population_max = 100000
    step = 1000
    sample_size = 1

    pop_size = [i for i in range(population_min, population_max, step)]
    seq_exec_time = []
    par_exec_time = []
    cpp_exec_time = []

    # Benchmarking
    for size in pop_size:
        seq_sum_time = 0
        par_sum_time = 0
        cpp_sum_time = 0
        for _ in range(sample_size):
            habitants = [set() for _ in range(cfg.NETWORK_SIZE)]
            agents = {}
            pop_seq = population.SequentialPopulation(habitants, agents, size=size, fromjson=False)
            pop_par = population.ParallelPopulation(habitants, agents, size=size, fromjson=False)
            pop_cpp = population.CppPopulation(habitants, agents, size=size, fromjson=False)
            # Sequential execution timing
            start_time = time.time()
            pop_seq.generate()
            seq_sum_time += (time.time() - start_time)
            # Cpp execution timing
            start_time = time.time()
            pop_cpp.generate()
            cpp_sum_time += (time.time() - start_time)

        seq_exec_time.append(seq_sum_time / sample_size)
        cpp_exec_time.append(cpp_sum_time / sample_size)
    # Linear fit
    # coeffs = np.polyfit(pop_size, exec_time, deg=1)
    # fit_time = [(coeffs[0] * i + coeffs[1]) for i in pop_size]
    # Plot
    plt.clf()
    plt.plot(pop_size, seq_exec_time, color='b', marker='o', label='sequential generation')
    plt.plot(pop_size, cpp_exec_time, color='r', marker='o', label='c++ generation')
    # plt.plot(pop_size, fit_time, color='r', label=f'linear fit (a={coeffs[0], 2}')

    plt.title('Population generation methods benchmark')
    plt.xlabel('population per node')
    plt.ylabel('execution time (s)')
    plt.legend()

    plt.grid()
    plt.tight_layout()

    plt.show()


if __name__ == '__main__':
    benchmark()
