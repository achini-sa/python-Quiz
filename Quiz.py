print("\n\n🌟 Hello, Welcome to the quiz !\n\n")

def quiz():
    score = 0
    
    # Question 1
    print("Question 1: \nWho painted the Mona Lisa?")
    answer1 = input("a) Vincent van Gogh \nb) Pablo Picasso \nc) Leonardo da Vinci \nd) Michelangelo \ne) Claude Monet \n\nYour answer: ")
    if answer1.lower() == "c":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is c) Leonardo da Vinci.")
    
    # Question 2
    print("\n\nQuestion 2: \nWho was the first President of the United States?")
    answer2 = input("a) Thomas Jefferson \nb) John Adams \nc) George Washington \nd) Abraham Lincoln \ne) Benjamin Franklin \n\nYour answer: ")
    if answer2.lower() == "c":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is c) George Washington.")
    
    # Question 3
    print("\n\nQuestion 3: \nWhat is the largest mammal on Earth?")
    answer3 = input("a) Elephant \nb) Blue whale \nc) Giraffe \nd) Polar bear \ne) Dolphin  \n\nYour answer: ")
    if answer3.lower() == "b":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is b) Blue whale.")
    
    
    # Question 4
    print("\n\nQuestion 3: \nWhat is the capital of France?")
    answer3 = input("a) Rome \nb) Paris \nc) Berlin \nd) Madrid \ne) London \n\nYour answer: ")
    if answer3.lower() == "b":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is b) Paris.")
    
    
    # Question 5
    print("\n\nQuestion 3: What is the chemical symbol for gold?")
    answer3 = input("a) Ag \nb) Au \nc) Fe \nd) Hg \ne) Pb \n\nYour answer: ")
    if answer3.lower() == "b":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is b) Au.")
        
        
    #score
    print("\nQuiz complete! Your score is:", score)

# Run the quiz
quiz()
