


def palindrome_checker():

    word=input("enter the word to check : \n")

    l=len(word)

    for i in range(l):
        if word[i] != word[l-i-1]:
            palindrome_flag=False
            break
        else:
            palindrome_flag=True

    if palindrome_flag:
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")


palindrome_checker()
