from GUI.label import Label
from GUI.textbox import TextBox
from GUI.frame import Frame


class MainUI(Frame):
    def __init__(self, screen):
        Frame.__init__(self, screen, (300, 110), (20, 20))
        self.l1 = Label(self, "Velocidad inicial", position=(30, 10))
        self.t1 = TextBox(self, (160, 10))
        self.l2 = Label(self, "Ángulo", position=(30, 40))
        self.t2 = TextBox(self, (160, 40))
        self.textboxes = {
            'angle': self.t2,
            'v_0': self.t1
        }
