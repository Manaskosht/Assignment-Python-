#kbc game

score = 0
correct = 0
wrong = 0
skip = 0

start = input("Start Game? (yes/no): ")

if start == "yes":

    # Question 1
    print("\nQ1. Capital of India?")
    print("A. Mumbai")
    print("B. Delhi")
    print("C. Chennai")
    print("D. Kolkata")

    ans = input("Enter answer or type skip: ")

    if ans == "B":
        print("Correct")
        score += 1000
        correct += 1
    elif ans == "skip":
        print("Skipped")
        skip += 1
    else:
        print("Wrong")
        wrong += 1

    # Question 2
    print("\nQ2. 2 + 2 = ?")
    print("A. 3")
    print("B. 4")
    print("C. 5")
    print("D. 6")

    ans = input("Enter answer or type skip: ")

    if ans == "B":
        print("Correct")
        score += 2000
        correct += 1
    elif ans == "skip":
        print("Skipped")
        skip += 1
    else:
        print("Wrong")
        wrong += 1

    # Question 3
    print("\nQ3. Father of Computer?")
    print("A. Newton")
    print("B. Tesla")
    print("C. Charles Babbage")
    print("D. Edison")

    ans = input("Enter answer or type skip: ")

    if ans == "C":
        print("Correct")
        score += 3000
        correct += 1
    elif ans == "skip":
        print("Skipped")
        skip += 1
    else:
        print("Wrong")
        wrong += 1

    # Question 4
    print("\nQ4. Red Planet?")
    print("A. Mars")
    print("B. Earth")
    print("C. Venus")
    print("D. Jupiter")

    ans = input("Enter answer or type skip: ")

    if ans == "A":
        print("Correct")
        score += 5000
        correct += 1
    elif ans == "skip":
        print("Skipped")
        skip += 1
    else:
        print("Wrong")
        wrong += 1

    # Question 5
    print("\nQ5. 5 + 5 = ?")
    print("A. 8")
    print("B. 9")
    print("C. 10")
    print("D. 11")

    ans = input("Enter answer or type skip: ")

    if ans == "C":
        print("Correct")
        score += 10000
        correct += 1
    elif ans == "skip":
        print("Skipped")
        skip += 1
    else:
        print("Wrong")
        wrong += 1

    # Final Result
    print("\n===== RESULT =====")
    print("Total Score:", score)
    print("Correct Answers:", correct)
    print("Wrong Answers:", wrong)
    print("Skipped Questions:", skip)

else:
    print("Game Ended")