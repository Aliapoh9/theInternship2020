def isPrime(n):

    for i in range(2, int(n**0.5 + 1)):
        if n % i == 0:
            return False
    return True


num = input()

while num != "0.0":

    Prime = False
    spNum = num.split(".")

    for i in range(1, 4):
        fullNum = int(spNum[0] + spNum[1][:i])
        if isPrime(fullNum):
            Prime = True
            print("TRUE")
            break

    if not Prime:
        print("FALSE")

    num = input()