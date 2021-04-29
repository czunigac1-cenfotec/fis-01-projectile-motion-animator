from GUI.label import Label
from GUI.textbox import TextBox
from GUI.frame import Frame


class MainUI:
    def __init__(self, screen):
        Frame.__init__(self, screen, (330, 110), (10, 10))

        self.l1 = Label(self, "Angulo", position=(135, 10))
        self.t1 = TextBox(self, (295, 10))
        self.l2 = Label(self, "Velocidad inicial", position=(135, 10))
        self.t2 = TextBox(self, (295, 10))

        self.textboxes = {'size': self.tb1,
                          'density': self.tb2,
                          'speed': self.tb3}
        #ToDO: Create UI elements declaration
        return

    def draw_ui(self):
        raise NotImplementedError
