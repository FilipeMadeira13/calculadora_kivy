from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout


class CalculatorLayout(BoxLayout):
    calc_display = ObjectProperty()
    new_input_mode = True
    expression = ""

    def process_input(self, value):
        if self.calc_display.text == "ERROR":
            return

        if self.expression and self.expression[-1] == "%":
            return

        if (self.calc_display.text == "0") or self.new_input_mode:
            self.calc_display.text = value
            self.expression = value
            self.new_input_mode = False
        else:
            self.calc_display.text += value
            self.expression += value

    def process_operator(self, operator):
        if self.calc_display.text == "ERROR":
            return

        if not self.expression:
            return

        if self.expression[-1] in "+-*/":
            return

        if self.expression[-1].isdigit() or self.expression[-1] == ")":
            self.expression += operator
            self.calc_display.text = self.expression
            self.new_input_mode = False

    def calculate(self):
        if self.calc_display.text == "ERROR":
            return

        try:
            expr = self.expression

            if expr and expr[-1] == ".":
                expr += "0"

            expr = expr.replace("%", "/100")

            result = eval(expr)

            if float(result) % 1 == 0:
                result = int(float(result))

            self.expression = str(result)
            self.calc_display.text = self.expression
            self.new_input_mode = True

        except Exception:
            self.calc_display.text = "ERROR"
            self.expression = ""
            self.new_input_mode = True

    def clear_display(self):
        self.calc_display.text = "0"
        self.expression = ""
        self.new_input_mode = True

    def process_percent(self):
        if self.calc_display.text == "ERROR":
            return

        try:
            if self.expression and self.expression[-1].isdigit():
                self.expression += "%"
                self.calc_display.text = self.expression
            else:
                return
        except Exception:
            self.calc_display.text = "ERROR"
            self.expression = ""
            self.new_input_mode = True

    def process_parenthesis(self, paren):
        if self.calc_display.text == "ERROR":
            return

        if paren == "(":
            if self.new_input_mode:
                self.expression = paren
                self.calc_display.text = paren
                self.new_input_mode = False
            elif not self.expression:
                self.expression = paren
                self.calc_display.text = paren
                self.new_input_mode = False
            elif self.expression[-1] in "+-*/(":
                self.expression += paren
                self.calc_display.text = self.expression
                self.new_input_mode = False
        elif paren == ")":
            if (
                self.expression.count("(") > self.expression.count(")")
                and self.expression[-1] not in "+-*/("
            ):
                self.expression += ")"
                self.calc_display.text = self.expression
                self.new_input_mode = False

    def process_dot(self):
        if self.calc_display.text == "ERROR":
            return

        if self.expression and self.expression[-1] == "%":
            return

        if not self.expression or self.expression.endswith(("+", "-", "*", "/", "(")):
            self.expression += "0."
            self.calc_display.text = self.expression
            self.new_input_mode = False
            return

        last_number = (
            self.expression.split("+")[-1]
            .split("-")[-1]
            .split("*")[-1]
            .split("/")[-1]
            .split("(")[-1]
        )

        if "." in last_number:
            return

        self.expression += "."
        self.calc_display.text = self.expression
        self.new_input_mode = False


class CalculatorApp(App):
    def build(self):
        return Builder.load_file("calc.kv")


if __name__ == "__main__":
    CalculatorApp().run()
