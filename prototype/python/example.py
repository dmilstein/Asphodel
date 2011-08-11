from gen_map import UniverseGenerator, UniverseSpec, GalaxySpec, BridgeSpec

def main():
    homeA = GalaxySpec(4, 1, 24, 10)
    homeB = GalaxySpec(4, 1, 24, 10)
    hub = GalaxySpec(9, 3, 15, 5)
    goldmineA = GalaxySpec(6, 2, 36, 20)
    goldmineB = GalaxySpec(6, 2, 42, 14)
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
    import pdb;  pdb.set_trace()


if __name__ == '__main__':
    main()
