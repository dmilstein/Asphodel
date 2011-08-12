from uuid import uuid4

_TEMPLATE = """graph universe {
    node [shape = doublecircle];
%(groups)s
%(bridges)s
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

_SYSTEM_TEMPLATE = """\t"%(name)s (%(population)s)" -- "%(destination_name)s (%(destination_population)s)";"""
# possibly add [ label = "1" ]
_GROUP_TEMPLATE = """\t"%(name)s (%(population)s)" [group="%(group)s"];"""
_BRIDGE_TEMPLATE = """\t"%(name)s (%(population)s)" [shape=circle];"""


def render_universe(universe):
    visited = set()
    systems = []
    groups = []
    bridges = []
    for galaxy in universe.galaxies:
        galaxy_id = uuid4().hex
        for system in galaxy.systems:
            if galaxy.name:
                groups.append(_GROUP_TEMPLATE % {
                    'name': system.full_name(),
                    'population': system.population,
                    'group': galaxy_id,
                })
            else:
                bridges.append(_BRIDGE_TEMPLATE % {
                    'name': system.full_name(),
                    'population': system.population,
                })

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
        'groups': '\n'.join(groups),
        'systems': '\n'.join(systems),
        'bridges': '\n'.join(bridges),
    }
