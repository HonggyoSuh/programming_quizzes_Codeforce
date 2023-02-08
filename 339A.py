import sys

def main(summands):
    digits = []
    result = ""
    digits = summands.split("+")

    digits.sort()

    for i in digits:
        result += i
        result += "+"
    
    result = result[:-1]

    print(result)

if __name__ == "__main__":
    summands = sys.stdin.readline()[:-1]

    main(summands)