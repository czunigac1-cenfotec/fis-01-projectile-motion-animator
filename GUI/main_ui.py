from GUI.label import Label
from GUI.textbox import TextBox
from GUI.frame import Frame


class MainUI(Frame):
    def __init__(self, screen, motionGame):

        Frame.__init__(self, screen, (400, 110), (20, 20))

        self.l1 = Label(self, "Ángulo", position=(90, 40))
        self.t2 = TextBox(self, (250, 40)) #textbox del angulo

        self.l2 = Label(self, "Velocidad inicial", position=(90, 10))
        self.t1 = TextBox(self, (250, 10)) #textbox de sl velocidad incial

        self.textboxes = {'Angulo': self.t1,
                          'Velocidad inicial': self.t2}
        #ToDO: Create UI elements declaration
        return

    def draw_ui(self):
        raise NotImplementedError
