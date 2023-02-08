if __name__ == "__main__":
    word = input()

    if "WUB" in word:
        word = word.replace("WUB", " ")
        word = word.strip()
        print(word)
    else:
        print(word)
    