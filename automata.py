class LoginAutomata:
    def __init__(self):
        self.state = "q0"

    def transition(self, input_symbol):
        if self.state == "q0":
            if input_symbol == "username_benar":
                self.state = "q1"
            else:
                self.state = "q2"

        elif self.state == "q1":
            if input_symbol == "password_benar":
                self.state = "q3"
            else:
                self.state = "q2"

        return self.state
