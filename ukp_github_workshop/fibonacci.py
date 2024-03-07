class Fibonacci:
    def __init__(self):
        self.mem = {}

    def fib(self, n: int) -> int:
        ##### YOUR CODE HERE #####
        if n in self.mem:
            return self.mem[n]
        if n == -1:
            raise ValueError("Input must be no-negative")
        if n==1 or n==2:
            result = 1
        else:
            result = self.fib(n-1) + self.fib(n-2)
        self.mem[n] = result
        return result
        ##########################