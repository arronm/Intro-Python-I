def get_fib(n):
  """Recursive Fibonacci function"""

  if n <= 1:
    return n
  else:
    return (get_fib(n - 1) + get_fib(n - 2))

terms = int(input("How many terms? "))

if terms <= 0:
   print("Please enter a positive integer")
else:
   for i in range(terms):
       print(get_fib(i))
