
# Support a very large number of fine-grained objects
# Requirement: the state information of each object can be retrieved on demand

import weakref


class Card(object):
    """The Flyweight"""

    # Could be a simple dict.
    # With WeakValueDictionary garbage collection can reclaim the object
    # when there are no other references to it.
    _pool = weakref.WeakValueDictionary()
    def __new__(cls, value, suit):
        ids = value+suit
        # If the object exists in the pool - just return it
        obj = cls._pool.get(ids)
        # otherwise - create new one (and add it to the pool)
        if obj is not None:
            return obj

        obj = object.__new__(cls)
        cls._pool[ids] = obj
        # This row does the part we usually see in `__init__`
        #obj.value, obj.suit = value, suit
        return obj

    # If you uncomment `__init__` and comment-out `__new__` -
    #   Card becomes normal (non-flyweight).
    # def __init__(self, value, suit):
    #     self.value, self.suit = value, suit
    

    def __repr__(self):
        return f"<Card: {self.value}{self.suit}>"
