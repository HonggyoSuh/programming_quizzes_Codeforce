if __name__ == "__main__":
    # string = input().split()
    # n = int(string[0])
    # k = int(string[1])
    # odd = []
    # even = []

    # for i in range(1, n + 1):
    #     if i % 2 == 0:
    #         even.append(i)
    #     else:
    #         odd.append(i)
    
    # total = odd + even

    # print(total[k - 1])

    n, k = list(map(int, input().split()))
    print((k - (n + 1) // 2) * 2 if k > (n + 1) // 2 else k * 2 - 1)