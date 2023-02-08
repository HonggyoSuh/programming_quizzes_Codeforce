import sys

def main(statement, num):
    count = 0
    x = 0

    while count < num:
        if statement[count].startswith("+") or statement[count].endswith("+"):
            x += 1
        else:
            x -= 1

        count += 1
        
    print(x)

if __name__ == "__main__":
    num = int(sys.stdin.readline())
    statement = []
    count = 0

    for i in range(num):
        statement.append(sys.stdin.readline()[:-1])
        count += 1

    main(statement, num)