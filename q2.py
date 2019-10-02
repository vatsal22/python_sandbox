import sys


def solution(A):
    """Your solution goes here."""
    A.sort()
    # serverA = []
    sumA = 0
    # serverB = []
    sumB = 0
    for i in range(len(A)):
        if(sumA <= sumB):
            sumA+=A.pop()
        else:
            sumB+=A.pop()
    return sumA-sumB

def main():
    """Read from stdin, solve the problem, write answer to stdout."""
    input = sys.stdin.readline().split()
    A = [int(x) for x in input[0].split(",")]
    sys.stdout.write(str(solution(A)))


if __name__ == "__main__":
    main()
