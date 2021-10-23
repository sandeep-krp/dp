"""
The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N. The method is to take increasingly larger prime numbers, and mark their multiples as composite.

For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two), then [6, 9, 12, ...] (multiples of three), and so on. Once we have done this for all primes less than N, the unmarked numbers that remain will be prime.

Implement this algorithm.

Bonus: Create a generator that produces primes indefinitely (that is, without taking N as an input).


"""

def solve_818(up_to):
    non_primes = set()
    counter = 2
    primes = []
    while(True):
        if(counter not in non_primes):
            non_primes.update(calculate_multiples(counter,up_to))
            primes.append(counter)
        counter+=1
        if counter >= up_to:
            break
    return primes

def calculate_multiples(n,up_to):
    multiples_of_n = set()
    i = 2
    while(True):
        x = n*i
        if x < up_to:
            multiples_of_n.add(x)
        else:
            break
        i +=1
    return multiples_of_n
