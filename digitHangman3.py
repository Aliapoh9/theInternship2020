answer = input().replace(" ", "")

wrongGuess = []
correctGuess = []
finalScore = 0

for i in range(5):
    guess = input()

    if answer.find(guess) != -1:
        correctGuess.append(guess)
    else:
        wrongGuess.append(guess)

    for c in answer:
        if c in correctGuess:
            print(c, end=" ")
            if i == 4:
                finalScore += 1
        else:
            print("_", end=" ")

    for g in wrongGuess:
        print(g, end=" ")
    print()

print(finalScore)
