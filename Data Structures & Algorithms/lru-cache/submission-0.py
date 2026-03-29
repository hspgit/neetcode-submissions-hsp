class LRUCache:

    def __init__(self, capacity: int):
        self.store = {}
        self.cap = capacity
        

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        
        val = self.store.pop(key);
        self.store[key] = val
        return val
        

    def put(self, key: int, value: int) -> None:
        # If capacity is 0, we cannot store anything.
        if self.cap == 0:
            return

        if key in self.store:
            # Key already exists. Remove it first.
            # It will be re-added later, making it the most recently used.
            self.store.pop(key)
        elif len(self.store) >= self.cap:
            # Cache is full and the key is new.
            # Evict the least recently used item (the first item in iteration order).
            # next(iter(self.store)) gets the first key (oldest/LRU).
            lru_key = next(iter(self.store))
            self.store.pop(lru_key)
        
        # Add the new key-value pair or update the existing one (now at the end).
        # This makes it the most recently used item.
        self.store[key] = value

        
