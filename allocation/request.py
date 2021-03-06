#!/usr/bin/env python3

UNSHARABLE_WAVES = [1, 2]

from person import Person

class Request:

    def __init__(self, person, rank):
        assert rank in [0, 1, 2]
        self.person = person
        self.rank = rank
        
    def __repr__(self):
        return ("Request(%s, rank=%d)" % (self.person, self.rank))
    
    def wish(self):
        return self.person.wish(self.rank)
    
    def key(self):
        return (self.person.wave, self.rank, -self.person.pts, self.wish())
    
    def is_conflicted_with(self, person, allocated_number):
        """ Assume that `person` owns `allocated_number` already """
        wish = self.wish()
        assert wish >= 1 and wish <= 99
        if allocated_number in [-1, -2]:
            return False
        if wish == allocated_number:
            if person.wave != self.person.wave:
                if person.gender == self.person.gender:
                    return True
            if person.wave in UNSHARABLE_WAVES:
                if person.gender == self.person.gender:
                    return True
            if bool(set(self.person.sports) & set(person.sports)):
                return True
        return False

if __name__ == '__main__':
    r = Request(Person.random(), 2)
    print(r)
