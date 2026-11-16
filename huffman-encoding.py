import heapq
import itertools

class Node:
    _counter = intertools.count() # gives each node a creation order for tie breaking
    
    def __innit__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
        self.order = next(node._counter)
        
    def is_leaf(self):
        return self.left is None and self.right is None
    
    def __It__(self, other):
        
        # lower freq comes first, on tie, node earlier comes first
        if self.freq != other.freq:
            return self.freq < other.freq
        else:
            return self.order < other.order
        
    def count_frequencies(text): #returns a dict with mapping for each character for the amount of times it appears
        freq = {}
        for c in text:
            if c in freq:
                freq[c] = freq[c] + 1
            else:
                freq[c] = 1
        return freq


    def build_priority_queue(freq): # Will make one leaf node per character and returns them as a min-heap ordered by frequency
        heap = []
        order = 0
        for c in sorted(freq):
            heap.append((freq[c], order, c))
            order = order + 1
        heapq.heapify(heap)
        return heap