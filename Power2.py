def is_power_two():
    number =int (input("Enter a number"))
    if number>0 and (number&(number-1))==0:
        print("True")
    else:
        print("False")

is_power_two()