'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    th_count = 0

    # if the word is only one letter it should return false or 0
    if len(word) <= 2:
        return 0 
    
    #iterate through the word by using slice, and check for the letters th
    if word[:2] == 'th':
        th_count += 1
        return count_th(word)
        
    return th_count
