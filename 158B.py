if __name__ == "__main__":
    n = int(input())
    group = list(map(int, input().split()))
    count = 0
    num3 = 0
    num2 = 0
    num1 = 0

    for i in group[:]:
        if i == 4:
            count+= 1
        if i == 3:
            count += 1
            num3 += 1
        if i == 2:
            num2 += 1
        if i == 1:
            num1 += 1
    
    num1 = num1 - num3 if num1 >= num3 else 0

    count += num2 // 2
    if num2 % 2 != 0:
        num2 = 1
    
    if num2 == 1 and num1 > 0:
        num1 -= 2 if num1 >= 2 else 1
        count += 1
    elif num2 == 1:
        count += 1
    
    if num1 > 0:
        count += num1 // 4
        if num1 % 4 != 0:
            count += 1
    
    print(count)