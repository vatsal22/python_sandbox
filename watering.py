import sys


def solution(plants, capacity1, capacity2):
    index1 = 0
    index2 = len(plants) - 1
    curCap1 = capacity1
    curCap2 = capacity2
    numOfRefills = 0

    splitPlants = len(plants)/2 if not len(plants) % 2 else len(plants)/2+1

    for _ in range(splitPlants):
        if index1 == index2:
            if curCap1+curCap2 < plants[index1]:
                numOfRefills += 1
                break  # doesn't matter who filled up. We know we're done now
            else:
                break  # they tag teamed the last plant so no more refills

        if plants[index1] > curCap1:
            numOfRefills += 1
            curCap1 = capacity1
        curCap1 -= plants[index1]

        if plants[index2] > curCap2:
            numOfRefills += 1
            curCap2 = capacity2
        curCap2 -= plants[index2]

        index1 += 1
        index2 -= 1
    return numOfRefills


def main():
    """Read from stdin, solve the problem, write answer to stdout."""
    input = sys.stdin.readline().split()
    A = [int(x) for x in input[0].split(',')]
    B = int(input[1], 10)
    C = int(input[2], 10)
    sys.stdout.write(str(solution(A, B, C)))


if __name__ == "__main__":
    main()
