

class Chat():
    def __init__(self):
        self.texts = []
        self.texts_history = []
        self.print_message("<red>Chat <blue>engine <green>testing...")

    def handle_input(self, text):
        self.print_message(text)

    def render(self):
        pass

    def print_message(self, message):
        print(message)