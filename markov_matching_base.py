import numpy as np
import matplotlib as plt

class person(object):
    def __init__(self, number_of_opposite_sex, index=None, sex=None):
        self.number_of_opposite_sex = number_of_opposite_sex
        self.preferences = self._set_random_preferences()
        # If matched, we will list the match here, if not matched, tha value will be false.
        self.match = None
        self.index = index
        self.sex = sex

    def _set_random_preferences(self):
        # set reandom preferences with a random sorting of a consecutive list
        preferences_list = np.arange(self.number_of_opposite_sex)
        np.random.shuffle(preferences_list)
        return preferences_list

    def set_match(self, match):
        self.match =  int(match)

    def get_rank_of_match(self):
        # Get the current rank of the person they're matched too.
        if self.match is not None:
            return self.preferences.tolist().index(self.match)
        else: 
            return self.number_of_opposite_sex-1



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
        self.verbose = True
    
    def _set_preferences(self):
            # set random preferences
            self.men = [ person( self.number_women, index=ii, sex='male' ) for ii in np.arange(self.number_men)]
            self.women = [ person( self.number_men, index=ii, sex='female' ) for ii in np.arange(self.number_women)]
    
    def set_matching(self, matching):
        # set matchings for each person
        for man_index, woman_index in matching.iteritems():
            self.men[int(man_index)].set_match(woman_index)
            self.women[int(woman_index)].set_match(man_index)

    def check_for_blocking_pair(self, man, woman):
        # check for blocking pairs, by looping over all matched men and checking for a 
        # blocking pair
            mans_rank_of_current_match = man.get_rank_of_match()
            womans_rank_of_current_match = woman.get_rank_of_match()
            rank_of_current_woman_to_man = man.preferences.tolist().index(int(woman.index))
            rank_of_man_to_current_woman = woman.preferences.tolist().index(int(man.index))
            self._print("Man's ranking of current match: {}".format(mans_rank_of_current_match))
            self._print( "Woman position with regard to man is {}".format(rank_of_current_woman_to_man) )
            self._print("Woman's ranking of current match: {}".format(womans_rank_of_current_match))
            self._print( "Man's position with regard to current woman is {}".format(rank_of_man_to_current_woman) )
            if ( rank_of_current_woman_to_man < mans_rank_of_current_match) and (rank_of_man_to_current_woman < womans_rank_of_current_match ):
                self._print("Blocking Pair Formed")
                return True

    def print_matching(self):
        man_matching_vector = [man.match for man in self.men]
        woman_matching_vector = [woman.match for woman in self.women]
        self._print( "The men are matched too: {}".format(man_matching_vector) )
        self._print( "The women are matched too: {}".format(woman_matching_vector) )

    def get_all_single_pairings(self):
        pairings = []
        for man in self.men:
            for woman in self.women:
                pairings.append((man.index, woman.index))
        return pairings


    def _print(self, string):
        if self.verbose:
            print string
            
test = set(3,3,{'0':'1', '1':'0'})
test.print_matching()
a = test.get_all_single_pairings()
print len(a) 
print a


        

