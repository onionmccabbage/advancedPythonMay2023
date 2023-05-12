# deque is a double ended queue

from collections import deque

def checkPalindrome(word):
    '''check to see if the word is a palindrome (reads the same both ways)'''
    dq = deque(word)
    while len(dq)>1:
        if dq.popleft() != dq.pop(): # deque also has appendleft and append
            return False
        return True

if __name__ == '__main__':
    print( checkPalindrome('madam') ) # True
    print( checkPalindrome('tenet') ) # True
    print( checkPalindrome('done') )  # False