# Multiples of 3 and 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.="random"
multiples = []

(1...1000).each do |value|
  if value % 3 == 0 || value % 5 == 0
    puts value
    multiples << value
  end
end

puts multiples.inject(:+) # try out reduce, inject is ruby specific
