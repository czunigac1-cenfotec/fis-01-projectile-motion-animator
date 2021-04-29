from GUI.label import Label
from GUI.textbox import TextBox
from GUI.frame import Frame


class MainUI(Frame):
    def __init__(self, screen, motionGame):

        Frame.__init__(self, screen, (330, 110), (10, 10))

        self.l1 = Label(self, "Angulo", position=(135, 10))
        self.t1 = TextBox(self, (295, 10))

        self.l2 = Label(self, "Velocidad inicial", position=(135, 10))
        self.t2 = TextBox(self, (295, 10))

        self.textboxes = {'Angulo': self.t1,
                          'Velocidad inicial': self.t2}
        #ToDO: Create UI elements declaration
        return

    def draw_ui(self):
        raise NotImplementedError
