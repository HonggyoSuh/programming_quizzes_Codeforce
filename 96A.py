from itertools import groupby

if __name__ == "__main__":
    string = input()

    if 7 <= max([len(list(g)) for k, g in groupby(string)], default = 0):
        print("YES")
    else: 
        print("NO")