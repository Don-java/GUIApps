import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

kivy.require("1.10.1")

# Sample Questions
questions = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "What is 2 + 2?": "4"
}

class QuizLayout(GridLayout):
    def __init__(self, **kwargs):
        super(QuizLayout, self).__init__(**kwargs)
        self.cols = 1
        self.question_label = Label(text="Welcome to the Quiz! Press Start to begin.")
        self.add_widget(self.question_label)

        # Create a Start Button
        self.start_button = Button(text="Start Quiz", font_size=24)
        self.start_button.bind(on_press=self.start_quiz)
        self.add_widget(self.start_button)

        # Placeholder for question index
        self.current_question_index = -1
        self.current_question = ""
        self.score = 0

    def start_quiz(self, instance):
        self.current_question_index = 0
        self.ask_question()

    def ask_question(self):
        if self.current_question_index < len(questions):
            self.current_question = list(questions.keys())[self.current_question_index]
            self.question_label.text = self.current_question

            # Create an input box for the answer
            self.answer_input = TextInput(multiline=False, hint_text="Type your answer here")
            self.add_widget(self.answer_input)

            # Create a Submit Button
            self.submit_button = Button(text="Submit", font_size=24)
            self.submit_button.bind(on_press=self.submit_answer)
            self.add_widget(self.submit_button)
        else:
            self.show_result()

    def submit_answer(self, instance):
        answer = self.answer_input.text.strip()
        correct_answer = questions[self.current_question]

        if answer.lower() == correct_answer.lower():
            self.score += 1
            feedback = "Correct!"
        else:
            feedback = f"Wrong! The correct answer is {correct_answer}."

        popup = Popup(title="Answer Feedback", content=Label(text=feedback), size_hint=(0.6, 0.4))
        popup.open()

        # Remove input and button after submission
        self.remove_widget(self.answer_input)
        self.remove_widget(self.submit_button)

        # Move to next question
        self.current_question_index += 1
        self.ask_question()

    def show_result(self):
        self.question_label.text = f"Quiz Finished! Your score is {self.score}/{len(questions)}."

class QuizApp(App):
    def build(self):
        return QuizLayout()

if __name__ == '__main__':
    QuizApp().run()
