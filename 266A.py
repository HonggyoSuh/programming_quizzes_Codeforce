if __name__ == "__main__":
    num = int(input())
    color = input()
    count = 0

    if num == 1:
        print(0)
    else:
        for i in range(0, num - 1):
            if color[i] == color[i+1]:
                count += 1
            else:
                continue

        print(count)