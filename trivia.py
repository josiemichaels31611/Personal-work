genres = ("World History", "Science", "Pop Culture")
questions =(("How old was Queen Elizabeth II when she became queen of England?", "What year was the Declaration of Independence signed?", "Who fought in the hundred year war?", "Historians believe that the Bubonic plague started in Europe in what year?"),
            ("What is known as the powerhouse of the cell?", "What is the chemical formula for water?", "What is the largest planet in our solar system?", "How many elements are on the perodic table?"),
            ("Which singer is known as the 'King of Pop'?", "What wizarding school does Harry Potter attend?", "What album inspired 'Brat Summer?", "Which 2012 film assembled Earth's mightiest heroes?"))
options = ((("A. 42", "B. 25", "C. 67", "D. 18"), ("A. 1776", "B. 1920", "C. 1888", "D. 1777"), ("A. Canada and USA", "B. Britain and France", "C. Japan and China", "D. Germany and USA"), ("A. 1291", "B. 1782", "C. 1347", "D. 1567" )), 
            (("A. Nucleus", "B. Lithosomes", "C. Ribosomes", "D. Mitochondria"), ("A. HCl", "B. H20", "C. O2", "D. PO3"), ("A. Jupiter", "B. Mars", "C. Neptune", "D. Earth"), ("A. 118", "B. 100", "C. 116", "D. 146")),
            (("A. Harry Styles", "B. Prince", "C. Sombr", "D. Michael Jackson"), ("A. Beaubaxtons", "B. Durmstrang", "C. Hogwarts", "D. Academy of Magic"), ("A. 'Short and Sweet' by Sabrina Carpenter", "B. 'BRAT' by Charli XCX", "C. 'Guts' by Olivia Rodrigo", "D. '1989 T.V.' by Taylor Swift"), ("A. Avengers", "B. Batman VS Superman", "C. Star Wars", "D. Star Trek")))
answers = (("B", "A", "B", "C"), ("D", "B", "A", "A"), ("D", "C", "B", "A"))
guesses = []
question_number = 1
score =0
def quiz(genre):
    '''This function asks the questions and verifies answers.'''
    global score, question_number
    for i in genres[genre]:
        for i in range(len(questions)):
            print(f"-----------{genre.upper()} QUESTION {question_number}-----------")
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
                score += 5
            else:
                print("Incorrect.")
                print(f"The correct answer was {answers[i]}.")
def results():
    '''This function calculates and prints results.'''
    print("-----RESULTS-----")
    print("Answers:", end= " ")
    for answer in answers:
        print(answer, end= " ")
    print()
    print("Guesses: ", end= " ")
    for guess in guesses:
        print(guess, end= " ")
    print()
    print(f"You scored {score} points.")
def reset():
    '''This function resets all variable to their original state.'''
    global guesses, score, question_number
    guesses = []
    score = 0
    question_number = 1
while True:
    genre = input(f"""Enter what genre you'd like to play
     Options:{genres}
 """).title()
    quiz(genre)
    results()
    retry = input("Would you like to try again? (y for yes, other for no): ")
    while retry.lower() == "y":
         reset()
         genre = input(f"""Enter what genre you'd like to play
     Options:{genres}
 """).title()
         quiz(genre)
         results()
         retry = input("Would you like to try again? (y for yes, other for no): ")
    else:
        break