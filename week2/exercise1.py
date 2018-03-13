"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

#I think this will create a list with those words for variable "some_words".
some_words = ['what', 'does', 'this', 'line', 'do', '?'] #it set the variable "some_words"

#I think this will print one word in the variable "some_words"
for word in some_words:
    print(word) #it printed all words contained in "some_words" one by one.

#I think this will print all words contained in "some_words" one by one like one above.
for x in some_words:
    print(x) #It printed all words in "some_words" one by one like one above.


#I think this will print all words in "some_words".
print(some_words) #it printed all words as expected.

#I think this sets a condition to print the phrase in the brackets below , only when "some_words" contains more than 3 words.
if len(some_words) > 3:
    print('some_words contains more than 3 words') #it printed the phrase in the brackets.

#I think it defines the funciton called "usefulFunction" as function print(platform.uname()).
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname()) 

#I think this will print the rusult of "platform.uname"
usefulFunction() #It returned the result of function "platform.uname". 
