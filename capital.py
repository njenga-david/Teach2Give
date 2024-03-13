#Write a program that accepts a string, capitalizes the first letter of each word in the string and then returns the result string

def capitalize_first_letter(sentence):
    return sentence.title()
def main():
    myString = input("Enter a string: ")
    capitalized_string = capitalize_first_letter( myString )
    print(" The final Capitalized String is:", capitalized_string)


main()
