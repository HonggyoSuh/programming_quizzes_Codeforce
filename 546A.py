if __name__ == "__main__":
    string = input().split(" ")
    initial_price = int(string[0])
    budget = int(string[1])
    tobuy = int(string[2])
    topay = 0

    for i in range(1, tobuy + 1):
        topay += (i * initial_price)
    
    if budget >= topay:
        print(0)
    else:
        print(topay - budget)
