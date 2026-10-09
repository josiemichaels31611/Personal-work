import time
questions = (
    "How many elements are in the perodic table?",
    "Which animal lays the largest egg?", 
    "What is the most abundant gas?",
    "How many bones are in the human body?",
    "Which planet in the solar system is the hottest?"
)
options = (
    ("A. 116", "B. 117", "C. 118", "D. 119"),
    ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
    ("A. Oxygen", "B. Hydrogen", "C. Nitrogen", "D. Carbon Dioxide"),
    ("A. 206", "B. 207", "C. 208", "D. 209"),
    ("A. Mercury", "B. Venus", "C. Earth", "D. Mars")
)
answers = ("C", "D", "C", "A", "B")
guesses = []
score = 0
question_number = 1
def quiz():
    '''This function asks the questions and verifies answers.'''
    global score, question_number, guesses
    for i in range(len(questions)):
        print(f"-----------QUESTION {question_number}-----------")
        print(f"""
    {questions[i]}
    {options[i]}
    """)
        print("----------------------------")
        question_number += 1 
        guess = input("Enter (A, B, C, or D): ").upper()
        guesses.append(guess)
        if guess == answers[i]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
            print(f"The correct answer was {answers[i]}.")

def results():
    '''This function calculates and prints results.'''
    global score
    print("-----RESULTS-----")
    print("Answers:", end= " ")
    for answer in answers:
        print(answer, end= " ")
    print()
    print("Guesses: ", end= " ")
    for guess in guesses:
        print(guess, end= " ")
    print()
    score = int((score/len(questions) * 100))
    print(f"Your score is {score}%.")

def reset():
    '''This function resets all variable to their original state.'''
    global guesses, score, question_number
    guesses = []
    score = 0
    question_number = 1

while True:
    quiz()
    results()
    retry = input("Would you like to try again? (y for yes, other for no): ")
    while retry.lower() == "y":
         reset()
         quiz()
         results()
         retry = input("Would you like to try again? (y for yes, other for no): ")
    else:
        break