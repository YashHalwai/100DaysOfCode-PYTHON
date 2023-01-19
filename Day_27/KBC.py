# Exercise 3: Kaun Banega Crorepati (KBC) | Python Tutorial - Day #27

# https://www.youtube.com/watch?v=Vs1Z7K70Mvw&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=27

# Create a program capable of displaying questions to the user like KBC.
# Use list data type to store the questions and their correct answers.
# Display the final amount the person is taking home after playing the game.

questions = [
    "What is the capital of India?",
    "What is the currency of Japan?",
    "Who is the current President of the United States?",
    "What is the highest mountain in the world?",
    "Which of the following is a prime number? a) 4 b) 9 c) 11 d) 15"
]

answers = [
    "New Delhi",
    "Yen",
    "Joe Biden",
    "Mount Everest",
    "c"
]

prizes = [
    1000,
    2000,
    5000,
    10000,
    20000
]

# function to check if the answer is correct
def check_answer(question_number, answer):
    if answer.lower() == answers[question_number].lower():
        return True
    else:
        return False

# function to play the game
def play_game():
    total_prize = 0
    for i in range(len(questions)):
        print(f"Question {i+1}: {questions[i]}")
        answer = input("Enter your answer: ")
        if check_answer(i, answer):
            total_prize += prizes[i]
            print(f"Correct! You won ${prizes[i]}")
        else:
            print("Incorrect. Better luck next time.")
            break
    return total_prize

# function to ask the player if they want to play again
def play_again():
    play_more = input("Do you want to play again? (y/n) ")
    if play_more.lower() == "y":
        return True
    else:
        return False

# main game loop
while True:
    total_prize = play_game()
    print(f"You won a total of ${total_prize}")
    if not play_again():
        break

print("Thank you for playing!")