# from queue import Queue


# def reverseNElementQueue(q,n):
#     stack = []
#     for i in range(n):
#         stack.append(q.get())
#     for i in range(n):
#         q.put(stack.pop())
#     for i in range(q.qsize()-n):
#         q.put(q.get())
#     return q
# q = Queue()
# q.put(1)
# q.put(2)
# q.put(3)
# q.put(4)
# q.put(5)
# reverseNElementQueue(q,3)
# while not q.empty():
#     print(q.get())
from collections import deque

def reverseNElementQueue(q,n):
    stack = []
    for i in range(n):
        stack.append(q.popleft())
    for i in range(n):
        q.append(stack.pop())
    for i in range(len(q)-n):
        q.append(q.popleft())
    return q
q = deque([1,2,3,4,5])
q = reverseNElementQueue(q,3)
while not q:
    print(q.popleft())