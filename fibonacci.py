class fibber:

    def __init__(self):
        self.memo = {}


    def fib(self, n):

        if n < 0:
            raise Exception('Please use a positive integer')

        elif n in [0,1]:
            return n

        
        if n in self.memo:
            return self.memo[n]

        
        result =  self.fib(n-1) + self.fib(n-2)

        self.memo[n] = result

        return result


if __name__ == '__main__':
    nfib = fibber()
    print nfib.fib(6)

