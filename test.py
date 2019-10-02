import sys


def solution(A):
    """Your solution goes here."""
    row_smallest_height = [A[0]]
    num_of_rows = 1
    for i in range(1, len(A)-1):
        smallest_row = -1
        smallest_height = -1
        iterator = 0
        for x in row_smallest_height:
            if A[i] < x and x > smallest_height:
                smallest_height = x
                smallest_row=iterator
            iterator+=1
        if smallest_row == -1:
            row_smallest_height.append(A[i])
            num_of_rows+=1
        else:
            row_smallest_height[smallest_row] = A[i]
    return num_of_rows






def main():
    """Read from stdin, solve the problem, write answer to stdout."""
    input = sys.stdin.readline().split()
    A = [int(x) for x in input[0].split(",")]
    sys.stdout.write(str(solution(A)))


if __name__ == "__main__":
    main()
