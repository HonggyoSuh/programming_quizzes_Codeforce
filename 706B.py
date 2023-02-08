import bisect

if __name__ == "__main__":
    n = int(input())
    price = sorted(list(map(int, input().split())))

    for i in range(int(input())):
        value = int(input())
        print(bisect(price, value))
            