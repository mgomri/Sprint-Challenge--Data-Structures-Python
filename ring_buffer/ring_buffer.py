class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.oldest_index = 0
        
    def append(self, value):
          
        if len(self.storage) < self.capacity: 
            self.storage.append(value)
        elif self.oldest_index < self.capacity:
            self.storage[self.oldest_index] = value
            self.oldest_index += 1
        else:
            self.oldest_index = 0
            self.storage[self.oldest_index] = value
            self.oldest_index += 1

    def get(self):
            buffer_list = []
            for el in self.storage:
                if el is None:
                    pass
                else:
                    buffer_list.append(el)
            return buffer_list