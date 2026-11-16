import heapq

class Node: #Class to define Node
    def __init__(self, freq, left, right):
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other): #To be used to compare Node with other Nodes
        return self.freq < other.freq
        
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

def extract-min(heap): #Simple definition for extract-min using heapq.
    return heapq.heappop(heap)

def build_huffman_tree(heap): # Will create and return the huffman tree using the nodes created
    if(len(heap) == 0):
        return None
    iteration = 1
    while(len(heap) > 1):
        x = extract-min(heap)
        y = extract-min(heap)
        z = Node(x.freq + y.freq, left = x, right = y)
        insert(heap, z)
        print(heap, iteration)
        iteration = iteration + 1
    return extract-min(heap);

def generate_codes(root): #Will generate the 0 and 1 code to a specific node for the entire huffman tree
    codes = {}
    if(root == heap)

def encode_text(text, codes): #Will encode the text based on the huffman tree arrangement when trying to spell something
    parts = []
    for c in text:
        parts.append(codes[c])
    return join(parts)
    
