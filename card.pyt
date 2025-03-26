
mode = input("Would you like to enter Teacher or Student Mode?")
#Teacher Mode
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
print(flashcards_data)

""" #Student Mode
if mode == 'Student Mode':
    class Student: """