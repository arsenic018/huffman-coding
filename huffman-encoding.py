import heapq


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