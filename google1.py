import sys

def isSmaller(stringA, stringB):
    smallestCharA = stringA[0]
    countA = 0
    for char in stringA:
        if char < smallestCharA:
            smallestCharA=char
            countA+=1
        elif char == smallestCharA:
            countA+=1
    
    smallestCharB = stringB[0]
    countB = 0
    for char in stringB:
        if char < smallestCharB:
            smallestCharB=char
            countB+=1
        elif char == smallestCharB:
            countB+=1

    return True if countA < countB else False



def solution(A, B):
    """Your solution goes here."""
    A = A.split(',')
    B = B.split(',')

    arr = []

    for wordB in B:
        count = 0
        for wordA in A:
            if isSmaller(wordA, wordB):
                count+=1
        arr.append(count)

    return arr



def main():
  """Read from stdin, solve the problem, write answer to stdout."""
  input = sys.stdin.readline().split()
  A = input[0]
  B = input[1]
  sys.stdout.write(",".join([str(i) for i in solution(A, B)]))


if __name__ == "__main__":
  main()
