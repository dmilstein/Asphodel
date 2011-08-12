#!/usr/bin/python
"""
Simulate a battle between two fleets of ships

Expects two lists of ships, as combat points + ship type, one ship per line,
space separated, with a player name at the start of each list, e.g.:

Alice
5 Ship of the Line
5 Ship of the Line
2 Frigate

Bob
6 Ship of the Line
1 Frigate
1 Frigate
1 Frigate

The defender is listed first, and goes first.

Run python battle.py ships_test.txt for an example
"""

import random
import sys
import time
import itertools

class Player(object):
    def __init__(self, name, ship_strs):
        self.name = name

        # Stored with most powerful ships first
        self.ships = list(reversed(sorted(map(Ship, ship_strs),
                                          key=lambda s: s.combat)))

    def is_dead(self):
        return not self.ships

    def attack(self, opponent):
        """
        Run an attack against an opponent, reporting damage.
        """
        print "Player %s attacking" % self.name
        print
        time.sleep(1)
        for s in self.ships:
            points_damage = s.attack()
            print "%s (%s/%s) does %s points of damage" % (
                s.ship_type,
                s.combat,
                s.health,
                points_damage)
            time.sleep(2)
            opponent.receive_damage(points_damage)
            print
            if opponent.is_dead():
                return
        print "Player %s's turn is overt" % self.name
        time.sleep(1)

    def receive_damage(self, points_damage):
        points_remaining = points_damage
        while points_remaining > 0:
            if not self.ships:
                print "Player %s has no ships left!" % self.name
                time.sleep(2)
                return
        
            weakest_ship = self.ships[-1]
            if weakest_ship.health > points_remaining:
                weakest_ship.health -= points_remaining
                print "%s's %s takes %s points damage, has %s left" % (
                    self.name,
                    weakest_ship.ship_type,
                    points_remaining,
                    weakest_ship.health)
                time.sleep(2)
                return
            
            else:
                points_remaining -= weakest_ship.health
                self.ships.pop()
                print "%s's %s takes %s points damage, evaporates into a cloud of dust" % (
                    self.name,
                    weakest_ship.ship_type,
                    weakest_ship.health)
                time.sleep(1.5)
                
    def __str__(self):
        return "Player: %s\nShips:\n%s" % (self.name, self.describe_ships())

    def describe_ships(self):
        return "\n".join(map(str,self.ships))

    def __repr__(self):
        return str(self)

class Ship(object):
    def __init__(self, ship_str):
        combat, ship_type = ship_str.split(' ', 1)
        self.combat = int(combat)
        self.health = int(combat)
        self.ship_type = ship_type

    def attack(self):
        # Iterative binomial ftw!  If only there was some kind of closed
        # form for this...  When will mathematicians figure that out?
        points_damage = 0
        for i in range(self.combat):
            if random.random() >= 0.5:
                points_damage += 1
        return points_damage

    def __str__(self):
        return "%s (%s)" % (self.ship_type, self.combat)

def run_battle(file_obj):
    defender, attacker = parse_players(file_obj)
    pairs = itertools.cycle([(defender, attacker), (attacker, defender)])
    for a, d in pairs:
        a.attack(d)
        if d.is_dead():
            print "Player %s's fleet is defeated!\n" % d.name
            print "Player %s's remaining fleet:\n%s" % (a.name,
                                                        a.describe_ships())
            return
        else:
            print
            print
        
    
def parse_players(file_obj):
    "Return the defender and attacker Player objects from a file obj"
    lines = file_obj.readlines()
    num_lines = len(lines)
    defender_name = lines[0].rstrip()
    defender_ships = []
    idx = 1
    while lines[idx].strip():
        defender_ships.append(lines[idx].strip())
        idx += 1

    # idx points at blank line
    idx += 1
    attacker_name = lines[idx].rstrip()
    idx += 1
    attacker_ships = []
    while idx < num_lines:
        attacker_ships.append(lines[idx].strip())
        idx += 1

    return (Player(defender_name, defender_ships),
            Player(attacker_name, attacker_ships))



if __name__=='__main__':
    if len(sys.argv) > 1:
        input_file_obj = open(sys.argv[1], 'r')
    else:
        input_file_obj = sys.stdin

    run_battle(input_file_obj)
