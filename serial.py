class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        self.start = start
        self.serial_code = start-1

    def __repr__(self):
        return f"<SerialGenerator start={self.start}>"

    def reset(self):
        self.serial_code = self.start-1

    def generate(self):
        self.serial_code+=1
        return self.serial_code
