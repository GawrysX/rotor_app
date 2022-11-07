from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

Builder.load_file('mainkv.kv')


class MyLayout(Widget):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        self.show()

    def RotateLeft(self):
        self.degrees = self.degrees-1 if self.degrees > 0 else 359
        self.show()

    def RotateRight(self):
        self.degrees = self.degrees+1 if self.degrees < 359 else 0
        self.show()

    def show(self):
        self.degreeLabel.text = str(self.degrees)


class MyApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    MyApp().run()
