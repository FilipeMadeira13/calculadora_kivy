from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout


class CalculatorLayout(BoxLayout):
    calc_display = ObjectProperty()

    current_number = None
    current_operator = None
    new_input_mode = False
    expression = ""

    def process_input(self, value):
        if self.calc_display.text == "ERROR":
            return

        if (self.calc_display.text == "0") or self.new_input_mode:
            self.calc_display.text = value
            self.new_input_mode = False
        else:
            self.calc_display.text += value

    def process_operator(self, operator):
        if self.calc_display.text == "ERROR":
            return

        if self.current_operator is not None:
            result = self.calculate_result(
                self.current_number, self.calc_display.text, self.current_operator
            )

            self.calc_display.text = result
            self.current_number = result
        else:
            self.current_number = self.calc_display.text

        self.current_operator = operator
        self.new_input_mode = True

        self.flash_display()

    def flash_display(self, *args):
        self.calc_display.foreground_color = (1, 1, 1, 0)
        Clock.schedule_once(self.restore_display, 0.1)

    def restore_display(self, *args):
        self.calc_display.foreground_color = (0, 0, 0, 1)

    def calculate(self):
        if self.current_operator is not None and self.current_number is not None:
            result = self.calculate_result(
                self.current_number, self.calc_display.text, self.current_operator
            )

            self.calc_display.text = result
            self.current_number = result
            self.current_operator = None
            self.new_input_mode = True

    def calculate_result(self, number_1, number_2, operator):
        try:
            if operator == "+":
                result = str(float(number_1) + float(number_2))
            elif operator == "-":
                result = str(float(number_1) - float(number_2))
            elif operator == "*":
                result = str(float(number_1) * float(number_2))
            elif operator == "/":
                result = str(float(number_1) / float(number_2))

            if float(result) % 1 == 0:
                result = str(int(float(result)))

            return result
        except ZeroDivisionError:
            self.current_number = None
            self.current_operator = None
            self.new_input_mode = True
            return "ERROR"

    def clear_display(self):
        self.calc_display.text = "0"

        self.current_number = None
        self.current_operator = None
        self.new_input_mode = True

    def process_percent(self):
        try:
            if self.calc_display.text == "ERROR":
                return

            if self.current_operator in ["+", "-"]:
                percent = float(self.current_number) * (
                    float(self.calc_display.text) / 100
                )
                if self.current_operator == "+":
                    result = float(self.current_number) + percent
                elif self.current_operator == "-":
                    result = float(self.current_number) - percent
            elif self.current_operator in ["*", "/"]:
                percent = float(self.calc_display.text) / 100
                if self.current_operator == "*":
                    result = float(self.current_number) * percent
                elif self.current_operator == "/":
                    result = float(self.current_number) / percent
            else:
                result = float(self.calc_display.text) / 100

            if float(result) % 1 == 0:
                result = int(float(result))

            self.calc_display.text = str(result)
            self.current_number = None
            self.current_operator = None
            self.new_input_mode = True
        except Exception:
            self.calc_display.text = "ERROR"
            self.current_number = None
            self.current_operator = None
            self.new_input_mode = False


class CalculatorApp(App):
    def build(self):
        return Builder.load_file("calc.kv")


if __name__ == "__main__":
    CalculatorApp().run()
