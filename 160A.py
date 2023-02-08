if __name__ == "__main__":
    number, value = int(input()), list(map(int, input().split()))
    half = sum(value) / 2
    number2, value2 = 0, 0

    for i in reversed(sorted(value)):
        value2 += i
        number2 += 1

        if value2 > half:
            break

    print(number2)
