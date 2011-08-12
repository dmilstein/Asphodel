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
        self.galaxy = None
        self.name = name
        self.population = population
        self.lanes = {} # maps destination planet -> lane

    def full_name(self, hide_population):
        if self.galaxy and self.galaxy.name:
            name = "%s %s" % (self.galaxy.name, self.name)
        else:
            name = self.name

        if hide_population:
            return name
        else:
            return "%s (%s)" % (name, self.population)

class Galaxy(object):
    """A galaxy is a loose grouping of star systems"""
    def __init__(self, name, systems, lanes):
        self.name = name
        self.systems = systems
        self.lanes = lanes

class Universe(object):
    """
    The game universe. Consists of a number of star systems and star lanes
    """
    def __init__(self, galaxies):
        self.galaxies = galaxies

        self.systems = []
        self.lanes = []
        for galaxy in galaxies:
            self.systems.extend(galaxy.systems)
            self.lanes.extend(galaxy.lanes)
