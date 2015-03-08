import numpy as np
import matplotlib as plt

class person(object):
    def __init__(self, number_of_opposite_sex):
        self.number_of_opposite_sex = number_of_opposite_sex
        self.preferences = self._set_random_preferences()
        # If matched, we will list the match here, if not matched, tha value will be false.
        self.match = None

    def _set_random_preferences(self):
        self.preferences = np.random.shuffle(np.arange(self.number_of_opposite_sex)) 

    def set_match(self, match):
        self.match =  match
        
class set(object):
    def __init__(self, number_men, number_women, matching={}):
        self.number_men = number_men
        self.number_women = number_women
        self._set_preferences()
        assert(self.number_men == len(self.men))
        assert(self.number_women == len(self.women))
        # the matching is a dictionary where the key is the man being matched, and the value is
        # who he is matched too. Yes, we are mancentric.
        assert(isinstance(matching, dict)), "Matching Must be a python dictionary"
        self.matching = matching
        self.set_matching(matching)
    
    def _set_preferences(self):
            # set random preferences
            self.men = [ person( self.number_women ) for ii in np.arange(self.number_men)]
            self.women = [ person( self.number_men ) for ii in np.arange(self.number_women)]
    
    def set_matching(self, matching):
        # set matchings for each person
        for man_index, woman_index in matching.iteritems():
            self.men[int(man_index)].set_match(woman_index)
            self.women[int(woman_index)].set_match(man_index)

    def check_for_blocking_pairs(self):
        # check for blocking pairs, by looping over all matched men and checking for a 
        # blocking pair
        for int(man_index), int(match) in matching.iteritems():

    def print_matching(self):
        man_matching_vector = [man.match for man in self.men]
        woman_matching_vector = [woman.match for woman in self.women]
        print "The men are matched too: {}".format(man_matching_vector)
        print "The women are matched too: {}".format(woman_matching_vector)

            
test = set(3,3,{'0':'1', '1':'0'})
test.print_matching()
        

