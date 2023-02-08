if __name__ == "__main__":
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    s = set()

    for i in range(n - 1, -1, -1):
        s.add(array[i])
        array[i] = str(len(s))
    
    print("\n".join(array[int(input()) - 1] for i in range(m)))
