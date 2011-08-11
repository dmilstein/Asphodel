

_TEMPLATE = """graph universe {
    node [shape = circle];
%(systems)s
}
"""


# and makes an extra effort to avoid edge crossings. For example, the graph

#digraph G {
#        /*
#          a [group=X, foo=bar];
#            b [group=X, foo=xxx];
#            */
#              c [foo=bar];
#                a -> b;
#                  c -> b;
#                    d -> b;
#                    }

_SYSTEM_TEMPLATE = """"%(name)s (%(population)s)" -- "%(destination_name)s (%(destination_population)s)";"""
# possibly add [ label = "1" ]


def render_universe(universe):
    visited = set()
    systems = []
    for galaxy in universe.galaxies:
        for system in galaxy.systems:
            for destination in system.lanes.keys():
                visit = tuple(sorted([system, destination]))
                if visit in visited:
                    continue
                visited.add(visit)

                systems.append(_SYSTEM_TEMPLATE % {
                    'name': system.full_name(),
                    'population': system.population,
                    'destination_name': destination.full_name(),
                    'destination_population': destination.population,
                })

    return _TEMPLATE % {
        'systems': '\n'.join(systems),
    }
