if __name__ == "__main__":
    n, k = [int(i) for i in input().split()]
    num = [int(i) for i in input().split()]
    prev, index = sum(num[:k]), 1
    total = prev

    for i in range(k, n):
        total -= num[i - k]
        total += num[i]

        if total < prev:
            prev = total
            index = i - k + 2
    
    print(index)