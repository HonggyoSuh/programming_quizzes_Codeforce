import sys

if __name__ == "__main__":
    name = sys.stdin.readline()[:-1]

    if len(set(name)) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")