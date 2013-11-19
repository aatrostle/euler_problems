# considering the terms in the fibonacci sequence
# whos values do not exceed four million
# find the sum of the even-valued terms

fibs = [0,1,1]
fibssum = []
result = 2
val = 4000000
while (result < val):
  if result % 2 == 0:
    fibssum.append(result)
  fibs.append(result)
  result = fibs[-1] + fibs[-2]

print "fibs is %r \n and fibssum is %r" % (fibs, fibssum)

result = fibs[-1] + fibs[-2]
fibs.append(result)

print "sanity check that next fibs is over 4mil: %r" % fibs
print "\nfinal sum is %r" % sum(fibssum)
