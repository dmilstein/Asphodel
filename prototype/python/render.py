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

_COLOR_TEMPLATE = """[color="#%s"]"""
_SYSTEM_TEMPLATE = """\t"%(name)s" -- "%(destination_name)s" %(color)s;"""
# possibly add [ label = "1" ]
_GROUP_TEMPLATE = """\t"%(name)s" [group="%(group)s"];"""
_BRIDGE_TEMPLATE = """\t"%(name)s" [shape=circle];"""


def render_universe(universe, fog_of_war=False):
    if fog_of_war: # We want to be able to hide data about the universe
        color = _COLOR_TEMPLATE % "ffffff"
    else:
        color = ""

    visited = set()
    systems = []
    groups = []
    bridges = []
    for galaxy in universe.galaxies:
        galaxy_id = uuid4().hex
        for system in galaxy.systems:
            if galaxy.name:
                groups.append(_GROUP_TEMPLATE % {
                    'name': system.full_name(fog_of_war),
                    'group': galaxy_id,
                })
            else:
                bridges.append(_BRIDGE_TEMPLATE % {
                    'name': system.full_name(fog_of_war),
                    'population': system.population,
                })

            for destination in system.lanes.keys():
                visit = tuple(sorted([system, destination]))
                if visit in visited:
                    continue
                visited.add(visit)

                systems.append(_SYSTEM_TEMPLATE % {
                    'name': system.full_name(fog_of_war),
                    'destination_name': destination.full_name(fog_of_war),
                    'destination_population': destination.population,
                    'color': color,
                })

    return _TEMPLATE % {
        'groups': '\n'.join(groups),
        'systems': '\n'.join(systems),
        'bridges': '\n'.join(bridges),
    }
