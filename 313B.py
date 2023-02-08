if __name__ == "__main__":
    string = input()
    n = len(string)
    checker = [0] * n

    for i in range(1, n):
        checker[i] = checker[i - 1] + (string[i - 1] == string[i])

    m = int(input())
    print(checker)
    for j in range(m):
        low, up = map(int, input().split())

        if j == 0: print("", end = "")

        print(checker[up - 1] - checker[low - 1])