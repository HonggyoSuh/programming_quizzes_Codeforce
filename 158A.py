import sys

def main(k, score):
    count = 0
    hurdle = int(score[k])

    for i in score:
        if int(i) >= hurdle and int(i) > 0:
            count += 1
    
    print(count)

if __name__ == "__main__":
    nk = sys.stdin.readline()[0:-1].split(" ")
    k = int(nk[1]) - 1
    score = sys.stdin.readline()[0:-1].split(" ")

    main(k, score)