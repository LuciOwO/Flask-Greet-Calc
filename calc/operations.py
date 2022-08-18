"""Basic math operations."""
class MathOperations:
    '''Performs basic math operations
    '''

    def __init__(self, a, b):
        """asigns values to the variables"""
        self.a = a
        self.b = b

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    @classmethod

    def wtf(self):
        """Add a and b."""
    
        return self.a + self.b

    def add(self):
        """Calculates a + b"""

        return self.a + self.b

    def sub(self):
        """Substract b from a."""

        return self.a - self.b

    def mult(self):
        """Multiply a and b."""

        return self.a * self.b

    def div(self):
        """Divide a by b."""

        return self.a / self.b
