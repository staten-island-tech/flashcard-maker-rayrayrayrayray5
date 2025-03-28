import json
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
        flashcards_data = [flashcards.to_dict()]
        try:      
            with open("FlashCards.json", "r") as file:
                existing_data = json.load(file)
                existing_data.extend(flashcards_data)
        except FileNotFoundError:
            existing_data = flashcards_data
        with open("FlashCards.json", "w") as file:
            json.dump(existing_data, file, indent=4)
        x = input('Do you want to continue?')
        if x.lower() == 'no':
            break

#Clear .json
""" with open("FlashCards.json", "w") as file:
    pass  """

#Student Mode
""" if mode == 'Student Mode':
    class Student: """