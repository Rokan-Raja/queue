class Queue:

    def __init__(self):
        self.queue = []

    def put(self, item):
        self.queue.append(item)

    def get(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def front(self):
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def empty(self):
        return not (len(self.queue))
def FrontToLast(q, qsize):
    if qsize <= 0:
        return
    q.put(q.get())
    FrontToLast(q, qsize - 1)
def pushInQueue(q, temp, qsize):
    if q.empty() or qsize == 0:
        q.put(temp)
        return
    elif temp <= q.front():
        q.put(temp)
        FrontToLast(q, qsize)
    else:
        q.put(q.get())
        pushInQueue(q, temp, qsize - 1)
def sortQueue(q):
    if q.empty():
        return
    temp = q.get()
    sortQueue(q)
    pushInQueue(q, temp, q.size())
qu = Queue()
qu.put(10)
qu.put(7)
qu.put(16)
qu.put(9)
qu.put(20)
qu.put(5)
sortQueue(qu)
print("\nBefore Sorting:")
while not qu.empty():
    print(qu.get(), end=' ')
