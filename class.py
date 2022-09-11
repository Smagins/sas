from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class MyApp(App):
    def build(self):

        btn = Button(text='Ввести', on_press = self.vv)
        bxl = BoxLayout(orientation='vertical')
        self.lbl = Label(text=' ')
        self.txtIn = TextInput()

        bxl.add_widget(self.txtIn)
        bxl.add_widget(self.lbl)
        bxl.add_widget(btn)
        
        return bxl

    def vv(self, instance):
        self.lbl.text=self.txtIn.text

        

if __name__ == '__main__':
    MyApp().run()
