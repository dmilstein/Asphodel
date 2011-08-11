class StarLane(object):
    """
    A Star Lane connects two systems, allowing fast, easy travel between them.
    Lanes are initially inactive, and are never 'owned' by an individual
    player.
    """
    def __init__(self, system_a, system_b):
        self.systems = set([system_a, system_b])

class System(object):
    """
    A star system is the smallest stepping stone in the universe. Its
    population determines the resource value of the system.
    """
    def __init__(self, name, population):
        self.name = name
        self.population = population
        self.lanes = {} # maps destination planet -> lane

class Universe(object):
    """
    The game universe. Consists of a number of star systems and star lanes
    """
    def __init__(self, systems, lanes):
        self.systems = systems
        self.lanes = lanes
