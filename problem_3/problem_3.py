# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

number = 600851475143
prime = 2

def is_prime(n):
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

def get_next_prime(n):
  n += 1
  while is_prime(n) == False:
    n += 1
  return n

def get_next_factor(n):
  prime = 2
  while n % prime != 0:
    prime = get_next_prime(prime)
  return prime

big_factor = 0

while True:
  next_factor = get_next_factor(number)
  number = number / next_factor
  if next_factor > big_factor:
    big_factor = next_factor
  if number == 1:
    break

print "YOLO SWAG %r" % (big_factor)

#while is_prime(this_shit_aint_a_prime) == False:
  
#while number % prime != 0:
# prime = get_next_prime(prime)
 
#print "LOL PRIME!!!! %r" % (prime)
#print "IS PRIME? %r" % (is_prime(49))
