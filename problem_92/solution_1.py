'''
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
'''
def square_digits(n):
    ### Return the sum of squares of the base-10 digits of n.
    total = 0
    while n:
        total += (n % 10) ** 2
        n //= 10
    return total


def problem92(limit):
    sum_limit = len(str(limit - 1)) * 9 ** 2 + 1
    arrive = [None] * sum_limit
    arrive[1], arrive[89] = 1, 89
    for n in range(2, sum_limit):
        chain = []
        while not arrive[n]:
            chain.append(n)
            n = square_digits(n)
        dest = arrive[n]
        for term in chain:
            arrive[term] = dest
    c = arrive.count(89)
    for n in range(sum_limit, limit):
        c += arrive[square_digits(n)] == 89
    return c


print(problem92(10000000))
