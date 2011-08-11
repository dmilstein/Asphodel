import random
import string

from nodes import System, StarLane, Galaxy, Universe

class GalaxySpec(object):
    """
    Describes the desired properties of a galaxy:
        - systems: how many systems will be in the galaxy
        - value_avg: the average population value of the system
        - value_spread: the maximum population difference from value_avg
        - connectivity: the number of "unnecessary" connections to make between
          systems. If 0, there will be len(systems) - 1 edges.
    """
    def __init__(self, name, systems, connectivity, value_avg, value_spread):
        self.name = name
        self.systems = systems
        self.value_avg = value_avg
        self.value_spread = value_spread
        self.connectivity = connectivity

class BridgeSpec(object):
    """
    Describes the desired properties of a bridge system between galaxies:
        - hops: how many planets are in the bridge?
        - galaxies_to_link: a list of all the galaxies being connected
    """
    def __init__(self, hops, galaxy_a, galaxy_b):
        self.hops = hops
        self.galaxies_to_link = [galaxy_a, galaxy_b]

class UniverseSpec(object):
    """
    Describes the desired properties of an game 'universe'
    """
    def __init__(self, galaxies, bridges):
        self.galaxies = galaxies
        self.bridges = bridges

class UniverseGenerator(object):
    """Holds some state about a generated universe"""
    def __init__(self):
        with open('star_names.txt') as f:
            self.name_pool = map(str.strip, f.readlines())
        random.shuffle(self.name_pool)

    def random_name(self):
        if not self.name_pool: # just in case
            return random.choice(string.ascii_uppercase)

        return self.name_pool.pop()

    def generate_system(self, value_avg, value_spread):
        """Returns a random star system"""
        population = max(0, random.randint(value_avg - value_spread, value_avg + value_spread))

        name = self.random_name()

        return System(name, population)

    def connect_systems(self, systems, connectivity):
        linked = systems[:]
        random.shuffle(linked)
        unlinked = [linked.pop()]
        lanes = []

        # Use this to avoid double-connecting systems
        connectivity_matrix = set()

        while unlinked:
            a = unlinked.pop()
            b = random.choice(linked)
            lanes.append(StarLane(a, b))

            connectivity_matrix.add((a, b))
            connectivity_matrix.add((b, a))

        max_connections = (len(systems) * (len(systems) - 1)) / 2
        connections = min(max_connections, connectivity + len(systems) - 1)
        while len(lanes) < connections:
            a = random.choice(systems)
            b = random.choice(systems)

            if a == b:
                continue
            if (a, b) in connectivity_matrix:
                continue

            lanes.append(StarLane(a, b))
            connectivity_matrix.add((a, b))
            connectivity_matrix.add((b, a))


        return lanes


    def generate_galaxy(self, spec):
        systems = [self.generate_system(spec.value_avg, spec.value_spread)
                for i in range(spec.systems)]
        lanes = self.connect_systems(systems, spec.connectivity)

        galaxy = Galaxy(spec.name, systems, lanes)
        for system in systems:
            system.galaxy = galaxy

        return galaxy

    def generate_bridge(self, spec, galaxy_a, galaxy_b):
        bridge_avg = 1
        bridge_spread = 4 # negative values get corrected to 0 or 1
        systems = [self.generate_system(bridge_avg, bridge_spread)]
        lanes = []

        for i in range(spec.hops - 1):
            next_system = self.generate_system(bridge_avg, bridge_spread)
            lanes.append(StarLane(next_system, systems[-1]))
            systems.append(next_system)

        # TODO: Support more than two galaxy connections per bridge?
        lanes.append(StarLane(
            systems[0], random.choice(galaxy_a.systems)))
        lanes.append(StarLane(
            systems[-1], random.choice(galaxy_b.systems)))

        return Galaxy(None, systems, lanes)

    def generate_universe(self, spec):
        galaxies = [self.generate_galaxy(galaxy_spec)
                for galaxy_spec in spec.galaxies]

        galaxy_by_spec = {}
        for galaxy, galaxy_spec in zip(galaxies, spec.galaxies):
            galaxy_by_spec[galaxy_spec] = galaxy

        bridges = [self.generate_bridge(
                bridge_spec,
                galaxy_by_spec[bridge_spec.galaxies_to_link[0]],
                galaxy_by_spec[bridge_spec.galaxies_to_link[1]])
            for bridge_spec in spec.bridges]

        return self.link_universe(galaxies + bridges)

    def link_universe(self, galaxies):
        for galaxy in galaxies:
            for lane in galaxy.lanes:
                a, b = lane.systems
                a.lanes[b] = lane
                b.lanes[a] = lane

        return Universe(galaxies)
