if __name__ == "__main__":
    input()
    a, b, c = [sum(map(int,input().split())) for i in range(3)]
    
    print(a - b)
    print(b - c)
