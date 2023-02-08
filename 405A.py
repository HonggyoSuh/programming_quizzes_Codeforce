if __name__ == "__main__":
    n = int(input())
    box = list(map(int, input().split()))
    box.sort()
    for i in box:
        print(i, end=" ")