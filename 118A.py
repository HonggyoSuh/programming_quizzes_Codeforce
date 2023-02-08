if __name__ == "__main__":
    origin = list(input())
    vowel = ["A", "E", "I", "O", "U", "Y", "a", "e", "i", "o", "u", "y"]

    for i in origin[:]:
        if i in vowel:
            origin.remove(i)

    result = ""

    for i in origin:
        result += "." + i.lower()

    print(result)
    