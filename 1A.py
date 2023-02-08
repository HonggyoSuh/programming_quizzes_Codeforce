if __name__ == "__main__":
    spec = list(map(int, input().split()))
    n, m, a = spec[0], spec[1], spec[2]
    print(((n + a - 1) // a) * ((m + a - 1) // a))