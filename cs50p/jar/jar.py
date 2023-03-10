class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity not valid")
        self._capacity = capacity
        self._cookies = 0

    def __str__(self):
        return '🍪' * self._cookies

    def deposit(self, n):
        if self._cookies + n > self._capacity:
            raise ValueError("Jar is full!")
        self._cookies += n

    def withdraw(self, n):
        if self._cookies - n < 0:
            raise ValueError("Too much cookies to withdraw!")
        self._cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies