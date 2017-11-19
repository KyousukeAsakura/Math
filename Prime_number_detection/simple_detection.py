import math

def isPrime(N):
    if N == 2:
        return True
    elif N < 2 or N % 2 == 0:
        return False
    else:
        i = 3
        while (i <= math.sqrt(N)):
            print(i)
            if N % i == 0:
                return False
            i = i + 2

    return True

if __name__ == '__main__':
    N = int(input())

    PN = isPrime(N)

    print (PN)
