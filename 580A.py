if __name__ == "__main__":
    n = int(input())
    num = list(map(int, input().split()))
    count, max = 0, 0

    for i in range(n - 1):
        if num[i] <= num[i + 1]:
            count += 1
        else:
            count = 0
        if count > max:
            max = count
    
    if n == 1:
        print(1)
    else:
        print(max + 1)