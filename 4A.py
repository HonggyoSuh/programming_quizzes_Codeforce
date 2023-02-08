
def main():
    state = True

    while state:
        weightStr = input()
        weightInt = 0

        try:
            weightInt = int(weightStr)
        except ValueError:
            #print("Please put an integer")
            continue

        if weightInt < 1 or weightInt > 100:
            #print("Please put value between 1 and 100")
            continue

        if weightInt % 2 == 0 and weightInt != 2:
            print("YES")
            state = False
        else:
            print("NO")
            state = False

if __name__ == "__main__":
    main()