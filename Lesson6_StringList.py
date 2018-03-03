word = input("Give me a word: ")
word = word.replace(" ","")

if word[::-1] == word:
    print("it's a palindrome!")
else:
    print("it's not a palindrome")