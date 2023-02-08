import sys

def abbreviation(word):
    if len(word[0:-1]) > 10:
        print(word[0] + str(len(word[0:-1]) - 2) + word[-2])
    else:
        print(word[0:-1])

def main(list_words, words):
    state = True
    count = 0
    
    while count < words:
        abbreviation(list_words[count])

        count += 1

if __name__ == "__main__":
    temp = []
    n = int(sys.stdin.readline())
    for i in range(n):
        temp.append(sys.stdin.readline())
    main(temp, n)