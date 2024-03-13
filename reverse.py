#Write a program that takes an integer as input and returns an integer with reversed digit ordering.
def reverse_integer(num):
  reversed_num = 0

  if num < 0:
    is_negative = True
    num = abs(num)

  
  while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
  return reversed_num


  

number =int(input("Enter a number"))
reversed_number = reverse_integer(number)
print(reversed_number)  