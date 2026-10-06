from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from random import randint


class MathGame(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(
            orientation="vertical",
            padding=30,
            spacing=20,
            **kwargs
        )

        self.score = 0
        self.streak = 0
        self.question_number = 0
        self.correct = 0
        self.answer = 0

        self.title = Label(
            text="🧠 PHUNGAN MATHS GAME",
            font_size="28sp",
            bold=True
        )

        self.stats = Label(
            text="⭐ Score: 0     🔥 Streak: 0",
            font_size="20sp"
        )

        self.question = Label(
            text="",
            font_size="40sp",
            bold=True
        )

        self.input_box = TextInput(
            hint_text="Enter your answer",
            input_filter="int",
            multiline=False,
            font_size="25sp",
            halign="center"
        )

        self.answer_button = Button(
            text="ANSWER",
            font_size="22sp",
            size_hint_y=None,
            height=60
        )

        self.restart_button = Button(
            text="RESTART",
            font_size="20sp",
            size_hint_y=None,
            height=55
        )

        self.message = Label(
            text="",
            font_size="20sp"
        )

        self.add_widget(self.title)
        self.add_widget(self.stats)
        self.add_widget(self.question)
        self.add_widget(self.input_box)
        self.add_widget(self.answer_button)
        self.add_widget(self.restart_button)
        self.add_widget(self.message)

        self.answer_button.bind(on_press=self.check_answer)
        self.restart_button.bind(on_press=self.restart)

        self.new_question()

    def new_question(self):

        if self.question_number >= 10:
            self.game_over()
            return

        self.question_number += 1

        a = randint(1, 20)
        b = randint(1, 20)

        operation = randint(1, 4)

        if operation == 1:
            self.question.text = f"{a} + {b} = ?"
            self.answer = a + b

        elif operation == 2:

            if a < b:
                a, b = b, a

            self.question.text = f"{a} - {b} = ?"
            self.answer = a - b

        elif operation == 3:

            a = randint(2, 12)
            b = randint(2, 12)

            self.question.text = f"{a} × {b} = ?"
            self.answer = a * b

        else:

            b = randint(2, 10)
            answer = randint(2, 10)
            a = b * answer

            self.question.text = f"{a} ÷ {b} = ?"
            self.answer = answer

        self.input_box.text = ""
        self.input_box.focus = True

        self.stats.text = (
            f"⭐ Score: {self.score}     "
            f"🔥 Streak: {self.streak}\n"
            f"Question {self.question_number}/10"
        )

    def check_answer(self, instance):

        if not self.input_box.text:
            self.message.text = "⚠️ Enter an answer!"
            return

        user_answer = int(self.input_box.text)

        if user_answer == self.answer:

            self.streak += 1
            self.correct += 1

            points = 10 + (self.streak * 2)
            self.score += points

            self.message.text = "✅ CORRECT! 🎉"

        else:

            self.streak = 0

            self.message.text = (
                f"❌ Wrong! Answer: {self.answer}"
            )

        self.new_question()

    def game_over(self):

        self.question.text = "🎉 GAME OVER!"

        self.message.text = (
            f"You got {self.correct}/10 correct!\n"
            f"⭐ Final Score: {self.score}"
        )

        self.answer_button.disabled = True
        self.input_box.disabled = True

    def restart(self, instance):

        self.score = 0
        self.streak = 0
        self.question_number = 0
        self.correct = 0

        self.answer_button.disabled = False
        self.input_box.disabled = False

        self.message.text = ""

        self.new_question()


class PhunganMathsApp(App):

    def build(self):
        Window.clearcolor = (0.03, 0.03, 0.06, 1)
        return MathGame()


PhunganMathsApp().run()



                                         16 * self.zoom, (0.65, 0.65, 0.65))

            
