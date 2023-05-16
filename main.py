from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
Screen:
    MDLabel:
        text: "Привет ШЕФ"
        halign: "center"
        font_style: "H2"
'''

class ChefApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

ChefApp().run()
