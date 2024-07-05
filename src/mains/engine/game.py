from classes.logger import info, error
from mains.engine.chat import Chat
from mains.engine.client import Client
from pyray import init_window, window_should_close, begin_drawing, draw_text, end_drawing, close_window, clear_background, set_target_fps
import pyray


class Main_Engine(): 
    def __init__(self, config, server):
        self.config = config
        self.server = server
        self.chat = Chat()
        self.client = Client(server["ip"], server["port"], Chat())
        self.init_window(self.config.readstr("window","window_title"))
        self.run()

    def updates(self):
        # update all things
        self.client.step()

    def draws(self):
        self.chat.render()

    def init_window(self, title="test"):
        set_target_fps(self.config.readint("window","target_fps"))
        init_window(800, 600, title)

    def run(self):
        while not window_should_close():
            begin_drawing()
            clear_background(pyray.WHITE)
            draw_text("Hello World!", 100, 100, 20, pyray.BLACK)
            end_drawing()

        close_window()
