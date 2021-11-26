def is_palindrome(string):
    backwards=string[::-1]
    return backwards==string

word=input("Please enter a word to check:")
if is_palindrome(word):
    print("{} is a palindrome".format(word))
else:
   print("{} is not a palindrome".format(word))

print( )
odd=[1,3,5,7,9]
even=[2,4,6,8]
odd.extend(even)
print(odd)
odd.sort()
print(odd)