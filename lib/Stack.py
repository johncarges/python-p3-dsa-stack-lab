class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limt = limit
        

    def isEmpty(self):
        return len(self.items) == 0 
        pass

    def push(self, item):
        if not self.full():
            self.items.append(item)
        else:
            return None
        

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None
        pass

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limt
            
        

    def search(self, target):
        for i in reversed(range(self.size())):
            if self.items[i] == target:
                return self.size() - 1 - i
        return -1
        
