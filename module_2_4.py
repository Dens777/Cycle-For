numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
import math
for i in numbers:
  is_prime = True
  for j in range(2, int(math.sqrt(i)+1)):
    if i % j == 0:
      is_prime = False
  if is_prime:
      primes.insert(i,i)
  else:
      not_primes.insert(i,i)
primes.remove(1)
print("Primes",primes)
print("Not primes",not_primes)