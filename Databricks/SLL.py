class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class SLLIerator:
    def __init__(self,start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next

class SLL:
    def __init__(self, start=None):
        self.start = start
    def is_empty(self):
        return self.start is None
    def insert_at_start(self, data):
        node = Node(data, self.start)
        self.start = node
    def insert_at_end(self, data):
        node = Node(data)
        current = self.start
        while current.next:
            current = current.next
        current.next = node
    def insert_after(self, data, after):
        current = self.start
        while current.next:
            if current.data ==after:
                break;
            current = current.next
        current.next = Node(data, current.next)
    def delete_at_start(self):
        self.start = self.start.next
    def delete_at_end(self):
        current = self.start
        while current.next.next:
            # print(current.data, end=' ')
            current = current.next
        current.next = None
    def delete(self, data):
        current = self.start
        while current.next.next:
            if current.next.data == data:
                break
            current = current.next
        current.next = current.next.next
    def printsll(self):
        current = self.start
        while current:
            print(current.data, end=' ')
            current = current.next
    def __iter__(self):
        return SLLIerator(self.start)


