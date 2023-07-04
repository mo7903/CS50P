class Jar:

    # Initializes a jar object with capacity given and no cookies
    def __init__(self, capacity=12):
        self.n = 0
        self.capacity = capacity

    # Returns a number of cookie emojis equal to the n of cookies in jar object
    def __str__(self):
        return "🍪"*self.n

    # Checks that the cookies number doesn't exceed capacity and deposits
    def deposit(self, n):
        if self.n + n > self.capacity:
            raise ValueError
        else:
            self.n += n

    # Checks that there are cookies to withdraw before withdrawing
    def withdraw(self, n):
        if self.n - n < 0:
            raise ValueError
        else:
            self.n -= n

    # Getter
    @property
    def capacity(self):
        return self._capacity

    # Setter
    @capacity.setter
    def capacity(self, capacity=12):
        if int(capacity) < 0:
            raise ValueError
        self._capacity = capacity

    # Returns the number of cookies currently in the jar
    @property
    def size(self):
        return self.n