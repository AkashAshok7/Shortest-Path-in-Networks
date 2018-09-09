class PriorityQueue(object):
    def __init__(self):
        self.queue = [0] #initializing heap with 0

    def shiftUp(self):
        i = len(self)
        while i // 2 > 0: # i//2 always gives an integer value and is used to avoid floating point numbers
          if self.queue[i] < self.queue[i // 2]:
            self.queue[i // 2], self.queue[i] = self.queue[i], self.queue[i // 2]
          i = i // 2

    def shiftDown(self, i):
        while i * 2 <= len(self):
            minimum = self.smallestChild(i)
            if self.queue[i] > self.queue[minimum]:
                self.queue[i], self.queue[minimum] = self.queue[minimum], self.queue[i]
            i = minimum

    def insert(self, k):
        #insert into heap
        self.queue.append(k)
        self.shiftUp()
        
    def deleteMinimum(self):
        #delete from heap
        return_value = self.queue[1]
        self.queue[1] = self.queue[len(self)] #the last leaf node is made as the root
        self.queue.pop() #pop the last item
        self.shiftDown(1) #order property
        return return_value

    def smallestChild(self, i):
        if i * 2 + 1 > len(self):
            return i * 2
        if self.queue[i * 2] < self.queue[i * 2 + 1]:
            return i * 2
        return i * 2 + 1   
    
    def buildPQ(self, alist):
        #used to build priority queue
        i = len(alist) // 2
        self.queue = [0] + alist
        while i > 0:
            self.shiftDown(i) #order property
            i = i - 1       

    def __len__(self):
        return len(self.queue) - 1
