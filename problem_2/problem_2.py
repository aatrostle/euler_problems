# considering the terms in the fibonacci sequence
# whos values do not exceed four million
# find the sum of the even-valued terms

sum_of_even_fibs = 0
fibs = [ 0, 1 ]
while True:
  fib = sum(fibs)
  if fib > 4000000:
    break
  if fib % 2 == 0:
    sum_of_even_fibs += fib
  fibs = [fibs[1], fib] 
  print sum_of_even_fibs
