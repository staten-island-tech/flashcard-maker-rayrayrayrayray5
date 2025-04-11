import json
import random
mode = input("Would you like to enter Teacher or Student Mode?")
#Teacher Mode
class Teacher:
    class FlashCard:
        def __init__(self, value, answer):
            self.value = value
            self.answer = answer

        def to_dict(self):
            return{"value": self.value, "answer": self.answer,}
flashcards_data = []

while True:
    if mode == 'Teacher Mode':
        value = input('Input a word/phrase:')
        answer = input('Input the answer:')
        flashcards = Teacher.FlashCard(value, answer)
        new_flashcard = flashcards.to_dict()

        try:      
            with open("FlashCards.json", "r") as file:
                try:
                    existing_data = json.load(file)
                except json.JSONDecodeError:
                    existing_data = []
        except FileNotFoundError:
            existing_data = []

        existing_data.append(new_flashcard)
        with open("FlashCards.json", "w") as file:
            json.dump(existing_data, file, indent=4)
            
        x = input('Do you want to continue?')
        if x.lower() == 'no':
            break

#Clear .json
""" with open("FlashCards.json", "w") as file:
    pass  """

#Student Mode
if mode == 'Student Mode':
    class Student:
        def __init__(self):
                self.points = 0
                self.streak = 0

        def flashcard_question(self, flashcard):
            print(f'Flashcard:{flashcard["value"]}')
            answer = input('Answer:')

            if answer.lower() == flashcard["answer"].lower():
                print("Correct, +1 point!")
                self.streak += 1
                self.points += 1
                base_points = 1

                if self.streak%3 == 0:
                    streak_bonus = 1
                    print("3 correct in a row! +1 point!")
                    self.points = self.points + streak_bonus
                    print('Correct, +1 point!')
            else:
                print(f'Incorrect, the correct answer was {flashcard["value"]}')
                self.streak = 0

    player = Student()

    try:
        with open("Flashcards.json", "r") as file:
            flashcards_list = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        flashcards_list = []

    random.shuffle(flashcards_list)

    for flashcard in flashcards_list:
        player.flashcard_question(flashcard)

    print(f"You finished with {player.points} points!")