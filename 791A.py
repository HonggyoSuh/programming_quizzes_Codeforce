if __name__ == "__main__":
    weight = input().split(" ")
    Limak = int(weight[0])
    Bob = int(weight[1])

    result = True
    count = 0

    while (result):
        Limak = Limak * 3
        Bob = Bob * 2
        count += 1

        if Limak > Bob:
            print(count)
            exit()
    
    print(count)