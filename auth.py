from automata import LoginAutomata

VALID_USER = "admin"
VALID_PASS = "12345"

def login(username, password):
    automata = LoginAutomata()

    if username == VALID_USER:
        automata.transition("username_benar")
    else:
        automata.transition("username_salah")
        return False

    if password == VALID_PASS:
        automata.transition("password_benar")
    else:
        automata.transition("password_salah")
        return False

    return automata.state == "q3"
