import json
mode = input("Would you like to enter Teacher or Student Mode?")
#Teacher Mode
while True:
    if mode == 'Teacher Mode':
        class Teacher:
            class FlashCard:
                def __init__(self, value, answer):
                    self.value = value
                    self.answer = answer
                def to_dict(self):
                    return{"value": self.value, "answer": self.answer,}
        value = input('Input a word/phrase:')
        answer = input('Input the answer:')
        flashcards = [
            Teacher.FlashCard(value, answer)
        ]
        flashcards_data = [i.to_dict() for i in flashcards]
        try:
            with open("FlashCards.json", "r") as file:
                flashcards_data = json.load(file)
        except FileNotFoundError:
            new_data = []
            flashcards_data.append(new_data.to_dict())
        x = input('Do you want to continue?')
        if x == 'No' or x == 'no':
            break
            

""" #Student Mode
if mode == 'Student Mode':
    class Student: """