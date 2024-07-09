def new_game():
    
    guesses = []
    correct_answers = 0
    questionNum = 1

    for key, value in questions.items():
        print("------------------------------------------")
        print(key)
        for i in options[questionNum - 1]:
            print(i)
        ans = input("Enter A, B , C , or D: ")
        ans = ans.upper()
        ans = ans[0]
        guesses.append(ans)

        correct_answers += check_answer(questions.get(key), ans)
        questionNum += 1

    display_score(guesses, correct_answers)


def check_answer(answer, userGuess):
    if answer == userGuess:
        print("Correct answer!")
        return 1
    else:
        print("Wrong answer!")
        return 0

def display_score(guesses, correctAnswers):
    print("--------------------")
    print("Your answers  : ", end ="")
    for i in guesses:
        print(i, end=" ")
    print("")

    print("--------------------")
    print("The answer key: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print("")

    print("---------------")
    print("Score: "+str(int((correctAnswers / len(questions)) * 100))+"%")
    print("")

    

def play_again():
    again = input("Do you want to play again? (yes to play again): ")
    again = again.lower()
    if again == "yes":
        return True
    return False
    

questions = {
    "Who is the author of 'One Hundred Years of Solitude? '":"B",
    "Where does 'Babel' (by R. F. Kuang) take place? ":"A",
    "Who is not a main character from 'Cloud Atlas' (by David Mitchell)? ":"C",
    "What is found in the desert of Dune (book by Frank Herbert)? ":"C",
    "How does the circus from 'The Night Circus' (by Erin Morgenstern) travel to other places? ": "A",
    "Which of these is not a book written by Malcolm Gladwell? ": "D",
    "Which of the following is correct? " : "C",
    "Which of these is not a stop in the Ankara metro line? ": "D"
}

options = [
    ["A. Agatha Christie", "B. Gabriel Garcia Marquez", "C. Zendaya", "D. Frank Herbert"],
    ["A. Oxford", "B. Cambridge", "C. Dublin", "D. Paris"],
    ["A. Luisa Rey", "B. Sonmi-451", "C. Aureliano Buendia", "D. Adam Ewing"],
    ["A. Diamonds", "B. Hamburgers", "C. Spice", "D. Apples"],
    ["A. Train", "B. Teleportation", "C. Sandworms", "D. Helicopter"],
    ["A. Outliers", "B. The Tipping Point", "C. Blink", "D. Human Compatible"],
    ["A. The earth is flat", "B. La La Land is set in New York", "C. Zeynep still cannot solve a leetcode question using python", "D. Python was invenetd in 1752"],
    ["A. Istanbul yolu", "B. Koru", "C. Bilkent", "D. Kartal"]
]

#begins a game after questions and options have been written down
new_game()

while play_again():
    new_game()

print("Thanks for playing Zeynep's game")