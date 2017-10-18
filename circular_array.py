"""Implement a Circular Array

A circular array is defined by having a start and indexes (be
sure to think about optimizing runtime for indexing)::

    >>> circ = CircularArray()
    >>> circ.add_item('harry')
    >>> circ.add_item('hermione')
    >>> circ.add_item('ginny')
    >>> circ.add_item('ron')
    >>> circ.print_array()
    harry
    hermione
    ginny
    ron
    >>> circ.get_by_index(2)
    'ginny'
    >>> print circ.get_by_index(15)
    None

However, the last item circles back around to the first item,
so you can also rotate the list and shift the indexes. Positive
numbers rotate the list start to the right (or higher indexes)::

    >>> circ = CircularArray()
    >>> circ.add_item('harry')
    >>> circ.add_item('hermione')
    >>> circ.add_item('ginny')
    >>> circ.add_item('ron')
    >>> circ.rotate(1)
    >>> circ.print_array()
    hermione
    ginny
    ron
    harry
    >>> circ.get_by_index(2)
    'ron'

And negative numbers rotate the list start to the left (or lower
indexes)::

    >>> circ = CircularArray()
    >>> circ.add_item('harry')
    >>> circ.add_item('hermione')
    >>> circ.add_item('ginny')
    >>> circ.add_item('ron')
    >>> circ.rotate(-1)
    >>> circ.print_array()
    ron
    harry
    hermione
    ginny
    >>> circ.get_by_index(2)
    'hermione'

And you can also rotate more than once around the ring::

    >>> circ = CircularArray()
    >>> circ.add_item('harry')
    >>> circ.add_item('hermione')
    >>> circ.add_item('ginny')
    >>> circ.add_item('ron')
    >>> circ.rotate(-17)
    >>> circ.get_by_index(1)
    'harry'

If you add a new item after rotating, it should go at the end of
the list in its current rotation::

    >>> circ = CircularArray()
    >>> circ.add_item('harry')
    >>> circ.add_item('hermione')
    >>> circ.add_item('ginny')
    >>> circ.add_item('ron')
    >>> circ.rotate(-2)
    >>> circ.add_item('dobby')
    >>> circ.print_array()
    ginny
    ron
    harry
    hermione
    dobby

"""

# BRAINSTORM:
    # instinct: linked_list r/t last node's .next to .head
        # however, O(n) runtime search. need another way.
        # can do reg. list to keep O(1) search runtime but implement head ([0])
        # to implement rotation (but keep lst the SAME); just abstract out
        # indices


class CircularArray(object):
    """An array that may be rotated, and items retrieved by index"""

    def __init__(self):
        """Instantiate CircularArray."""

        # initialize array. track index 0 via ".head" (for rotation)
        self.array = []
        self.head = None

    def add_item(self, item):
        """Add item to array, at the end of the current rotation.

        if head @ A, insert E.
        [A B C] --> [E A B C] (E now head) --> +=1 head --> [E A B C] (A back to head)

        if rotated 1 & head now @ B, insert E.
        [A B C] --> [A E B C] (E now head) --> +=1 head --> [A E B C] (B back to head)"""

        # if initially empty
        if self.head is None:
            self.head = 0
            self.array = [item]

        # if not empty, insert item before .head + reassign head (since shifted)
        else:
            self.array.insert(self.head, item)
            self.head += 1

    def get_by_index(self, index):
        """Return the data at a particular index.

        No circling (get @2):
        [A B C D] where head @B, target is D
        --> array[1 + 2] --> array[3] --> D

        Circling (get @2)
        [A B C D] where head @D, target is B
        --> new index is 2 + 3 - 4 --> 1 --> array[1] --> B"""

        # Consideration: use head as starting index + add on; don't use
        # regular indexing of list!

        # Edge case: if index doesn't exist
        if index >= len(self.array):
            return None

        # If head positioned where target index doesn't circle around
        if index + self.head < len(self.array):
            return self.array[index + self.head]

        # If circling needed
        adjusted_idx = index + self.head - len(self.array)
        return self.array[adjusted_idx]

    def rotate(self, increment):
        """Rotate array, positive for right, negative for left.

        If increment is greater than list length, keep going around.
        """

        # Consideration: just change .head, not actual array.

        # Edge: empty array
        if not self.head:
            return

        # Circular rotation
        adjusted_idx = (increment + self.head) % len(self.array)
        self.head = adjusted_idx

    def print_array(self):
        """Print the circular array items in order, one per line"""

        # use get_by_index for .head indexing vs. original list index
        for i in range(len(self.array)):
            print self.get_by_index(i)


if __name__ == "__main__":
    print
    import doctest

    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED; YOU MUST BE DIZZY WITH JOY! ***"
    print
