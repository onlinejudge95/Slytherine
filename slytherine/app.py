from pygame import init as pygame_init
from pygame import display
from pygame import event

from slytherine.utils import Constants


class App:

    def __init__(self):
        self.constants = Constants
        self.running = False
        self.game_display = None
        self.width = 640
        self.height = 400

    def init(self):
        pygame_init()
        self.game_display = display.set_mode((self.width, self.height),
                                             self.constants.SURFACE | self.constants.BUFFERING)
        self.running = True

    def execute(self):
        self.init()
        if not self.running:
            self.running = False

        while self.running:
            for item in event.get():
                self.handle_event(item)
            self.loop()
            self.render()

        self.clean_up()

    def handle_event(self, item):
        if item.type == self.constants.EVENTS.QUIT:
            self.running = False

    def loop(self):
        print('In Loop')

    def render(self):
        print('In Render')

    def clean_up(self):
        print('In Cleanup')
