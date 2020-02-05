acroList = []

n = int(input())

for i in range(n):
    word = input()
    acro = ""
    for w in word.split():
        if w[0].isupper():
            acro += w[0]

    acroList.append(acro)

acroList.sort()
acroList.sort(key=len, reverse=True)

for a in acroList:
    print(a + "\n")