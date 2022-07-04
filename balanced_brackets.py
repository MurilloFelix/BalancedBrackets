#!/bin/python3

# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING brackets as parameter.
from ast import Break


openBracket = ["{","[","("]
closeBracket = ["}","]",")"]
def isBalanced(brackets):
    openedBracketsList = []
    result = 'YES'
    for bracket in brackets:
        if bracket in openBracket:
            openedBracketsList.append(bracket)
        elif bracket in closeBracket:
            if not openedBracketsList:
                result = 'NO'
                break
            lastOpenBracket = openedBracketsList.pop(len(openedBracketsList)-1)
            if openBracket.index(lastOpenBracket) != closeBracket.index(bracket):
                result = 'NO'
                break
    return result

if __name__ == '__main__':

    t = int(input().strip())

    results = []
    for t_itr in range(t):
        brackets = input()

        results.append(isBalanced(brackets))

    print(*results, sep='\n')
