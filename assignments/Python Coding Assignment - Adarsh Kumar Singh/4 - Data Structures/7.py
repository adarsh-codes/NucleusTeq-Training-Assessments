from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item) 

    def dequeue(self):
        if self.queue:
            return self.queue.popleft()
        return None 

q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())
print(q.dequeue()) 
print(q.dequeue()) 
print(q.dequeue())  
