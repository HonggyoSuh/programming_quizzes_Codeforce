if __name__ == "__main__":
    n = int(input())

    for x in range(n):
        print("YNEOS"[360 % (180 - int(input())) > 0::2])
