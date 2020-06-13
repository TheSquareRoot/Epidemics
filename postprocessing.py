import epidemics.cfg as cfg


# Parameters import
NETWORK_SIZE = cfg.NETWORK_SIZE

class Statistics:
    def __init__(self, S, I, R, population_stats):
        self.S = S
        self.I = I
        self.R = R
        self.population_stats = population_stats

    #
    # ------------------------- Time Plots -------------------------
    #
