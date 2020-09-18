'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

    # initialize count value at 0
def count_th(word, count=0):

    # if the word is only one letter it should return false or 0
    if len(word) < 2:
        return 0 
    # slice the word at every second index, and check for the letters th
    if word[:2] == 'th':
        #if the letters are found recursively call count_th, increment the index to check by 1, and add 1 to count
        return count_th(word[1:])+1
    #return the last index of the array
    return count_th(word[1:])
    
