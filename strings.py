# Write a Python program that accepts a 
# string and outputs the words in that string
# in reverse order.

def reverse_words(string):
    words = string.split()
    words.reverse()
    result = " ".join(words)
    return result

input_string = input("Enter a string: ")
output_string = reverse_words(input_string)
print(output_string)

# You can use f-string formatting in Python 
# to print the statement with the given variables:

def print_info(name, age):
    print(f"My name is {name} and I am {age} years old.")
name = "John"
age = 30
print_info(name, age)

#  Given the variable sentence, how can you format a 
# string to print "The quick brown fox jumped over the lazy dog.
# " with the first letter of each word capitalized?

def capitalize_first_letter(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)

sentence = "the quick brown fox jumped over the lazy dog."
capitalized_sentence = capitalize_first_letter(sentence)
print(capitalized_sentence)

# Given the variables num1, num2, and result,
# how can you format a string to print "The result 
# of adding 5 and 10 is 15."?

def print_result(num1, num2, result):
    print("The result of adding {} and {} is {}.".format(num1, num2, result))

num1 = 5
num2 = 10
result = num1 + num2
print_result(num1, num2, result)


