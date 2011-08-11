from gen_map import UniverseGenerator, UniverseSpec, GalaxySpec, BridgeSpec
from render import render_universe

def main():
    homeA = GalaxySpec("Red", 4, 1, 24, 10)
    homeB = GalaxySpec("Blue", 4, 1, 24, 10)
    hub = GalaxySpec("Hub", 9, 3, 15, 5)
    goldmineA = GalaxySpec("Alpha", 6, 2, 36, 20)
    goldmineB = GalaxySpec("Omega", 6, 2, 42, 14)
    galaxies = [homeA, homeB, hub, goldmineA, goldmineB]

    bridges = [
            BridgeSpec(2, homeA, hub),
            BridgeSpec(2, homeB, hub),
            BridgeSpec(4, goldmineA, hub),
            BridgeSpec(4, goldmineB, hub),
            ]

    universe_spec = UniverseSpec(galaxies, bridges)

    generator = UniverseGenerator()
    universe = generator.generate_universe(universe_spec)
    with open('universe.dot', 'w') as f:
        f.write(render_universe(universe))

if __name__ == '__main__':
    main()