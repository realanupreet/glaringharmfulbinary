class pqele:
    def __init__(self, value):
        self.val=value
    def __repr__(self):
        return self.val

class pqelemax(pqele):
    def __lt__(self,other):
        return self.val>other.val

class pqelemin(pqele):
    def __lt__(self,other):
        return self.val<other.val


# Usage-
pq = PriorityQueue()
pq.put(PqElement(3))  # Add Item      - O(Log(n))
pq.put(PqElement(5))  # Add Item      - O(Log(n))
pq.put(PqElement(6))  # Add Item      - O(Log(n))
pq.put(PqElement(32))  # Add Item      - O(Log(n))
pq.put(PqElement(2))  # Add Item      - O(Log(n))
pq.put(PqElement(53))  # Add Item      - O(Log(n))
pq.put(PqElement(6))  # Add Item      - O(Log(n))
pq.put(PqElement(23))  # Add Item      - O(Log(n))
pq.put(PqElement(233))  # Add Item      - O(Log(n))
pq.put(PqElement(56))  # Add Item      - O(Log(n))
# topValue = pq.get()        #Pop top item  - O(1)
# topValue = pq.queue[0].val #Get top value - O(1)
print(pq.get())

