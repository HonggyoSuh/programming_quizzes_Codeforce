import sys

if __name__ == "__main__":
    word = sys.stdin.readline()[:-1]
    newWord = ""

    if not word[0].isupper():
        newWord = word[0].upper() + word[1:]
    else:
        newWord = word
    
    print(newWord)