# find the sum of all multiples of 3 or 5 below 1000

data = range(1,1000)
sum = 0

for number in data:
  if number % 3 == 0 or number % 5 == 0:
    sum += number

print "The sum of all multiples of 3 or 5 below 1000 is: %s" % sum
