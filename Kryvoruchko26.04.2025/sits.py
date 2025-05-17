from kivy.uix.label import Label
from kivy.clock import clock





class Sits(Label):
    def init(self, total, **kwargs):
        self.current = 0
        self.total = total
        my_text = "Залишилось присідань: " + str(self.total)
        super().init(text=my_text, **kwargs)

    def next(self, *args):
        self.current += 1
        remain = max(0, self.total - self.current)
        my_text = "Залишилось присідань: " + str(remain)
        self.text = my_text
