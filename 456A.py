if __name__ == "__main__":
    n = int(input())
    # dic = {}

    for i in range(n):
        price, value = list(map(int, input().split()))
        
        if price == value:
            continue
        else:
            print("Happy Alex")
            exit()
    print("Poor Alex")