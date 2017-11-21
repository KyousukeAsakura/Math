
if __name__ == '__main__':
    N1 = int(input())
    N2 = int(input())

    while True:
        if (N1 == 0 or N2 == 0):
            if(N1 > N2):
                print(N1)
                break
            else:
                print(N2)
                break
        elif(N1 < N2):
            N2 = N2 % N1
        else:
            N1 = N1 % N2
