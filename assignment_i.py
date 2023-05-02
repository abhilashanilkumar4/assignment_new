class Q:
    def __init__(self):
        self._enqueue_stack = []
        self._dequeue_stack = []
    
    def enqueue(self, value):
        self._enqueue_stack.append(value)
    
    def dequeue(self):
        if not self._dequeue_stack:
            while self._enqueue_stack:
                self._dequeue_stack.append(self._enqueue_stack.pop())
        return self._dequeue_stack.pop()
    
    def is_empty(self):
        return len(self._enqueue_stack) + len(self._dequeue_stack) == 0


q = Q()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())
print(q.dequeue())

q.enqueue(4)
q.enqueue(5)

print(q.dequeue())  
print(q.dequeue())  
print(q.dequeue())  
print(q.is_empty())
