from gen_map import UniverseGenerator, UniverseSpec, GalaxySpec, BridgeSpec
from render import render_universe

def main():
    homeA = GalaxySpec("Red", 3, 1, 24, 5)
    homeB = GalaxySpec("Blue", 3, 1, 24, 5)
    hub = GalaxySpec("Alpha", 6, 3, 15, 5)
    goldmineA = GalaxySpec("Lambda", 4, 1, 36, 20)
    goldmineB = GalaxySpec("Mu", 4, 1, 42, 14)
    galaxies = [homeA, homeB, hub, goldmineA, goldmineB]

    bridges = [
            BridgeSpec(2, 2, homeA, hub),
            BridgeSpec(2, 2, homeB, hub),
            BridgeSpec(3, 4, goldmineA, hub),
            BridgeSpec(3, 4, goldmineB, hub),
            ]

    universe_spec = UniverseSpec(galaxies, bridges)

    generator = UniverseGenerator()
    universe = generator.generate_universe(universe_spec)
    with open('universe.dot', 'w') as f:
        f.write(render_universe(universe))

    with open('universe-fog.dot', 'w') as f:
        f.write(render_universe(universe, True))

if __name__ == '__main__':
    main()
