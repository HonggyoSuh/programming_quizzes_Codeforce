import sys

def main(row):
    for i in range(len(word[0])):
        if word[0][i] > word[1][i]:
            print(1)
            break
        elif word[0][i] < word[1][i]:
            print(-1)
            break
        elif word[0][i] == word[1][i] and i == len(word[0]) - 1:
            print(0)

if __name__ == "__main__":
    word = []

    for i in range(2):
        word.append(sys.stdin.readline()[:-1].upper())

    main(word)