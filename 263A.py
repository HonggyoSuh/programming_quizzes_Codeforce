import sys

def main(row):
    rowNum = 0
    colNum = 0

    for i in range(5):
        row[i] = row[i].replace(" ", "")
        for j in range(5):
            if row[i][j] == "1":
                rowNum = i
                colNum = j
        
    print(abs(2 - rowNum) + abs(2 - colNum))

if __name__ == "__main__":
    row = []

    for i in range(5):
        row.append(sys.stdin.readline()[:-1])

    main(row)