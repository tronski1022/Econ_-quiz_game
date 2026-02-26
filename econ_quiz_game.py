print("Welcome to the Econ Quiz Game!")

playing = input("Do you want to test your knowledge? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does GDP stand for? ")
if answer.lower() == "gross domestic product":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is it called when wage is adjusted for inflation? ")
if answer.lower() == "real wage":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does CPI stand for? ")
if answer.lower() == "consumer price index":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is it called when the levels of prices are rising and purchasing power is reduced? ")
if answer.lower() == "inflation":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the type of inflation that pulls up prices with too many dollars chasing too few goods? ")
if answer.lower() == "demand pull inflation":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the type of inflation where higher production costs push up the prices? ")
if answer.lower() == "cost push inflation":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is all the goods and services that buyers are willing and "
               "able to purchase at different price levels? ")
if answer.lower() == "aggregate demand":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What are rent, insurance, manager salaries...etc ")
if answer.lower() == "fixed costs":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What are raw materials, labor, electricity...etc ")
if answer.lower() == "variable costs":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is Variable costs + Fixed costs ")
if answer.lower() == "costs of production":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 10) * 100) + "%.")

if score >= 7 :
    print("Great job!")
else:
    print("Better luck next time!")

