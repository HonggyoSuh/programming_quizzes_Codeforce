import sys

def main(temp, n):
    result = 0

    for i in range(n):
        temp[i] = temp[i][0:-1]
        temp[i] = temp[i].replace(" ", "")
    
    for item in temp:
        count = 0

        for index in range(3):
            if item[index] == "1":
                count += 1
        
        if count > 1:
            count = 0
            result += 1

    print(result)

if __name__ == "__main__":
    temp = []
    n = int(sys.stdin.readline())

    for i in range(n):
        temp.append(sys.stdin.readline())

    main(temp, n)