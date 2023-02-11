from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from moviepy.editor import *
import pytube
 
class YourSpotipy(App):
    def build(self):
         self.window = GridLayout()
         self.window.cols = 1
         self.window.size_hint =(.8, .9)
         self.window.pos_hint = {"center_x":0.5,"center_y":0.5}
         self.icon="icon.png"
         
         self.window.add_widget(Image(source="icon.png"))
         self.window.add_widget(Label(text="Inserisci il link di Youtube",size_hint =(.8, .2)))
         
         self.textinput = TextInput(
             size_hint = (1,.2),
             font_size = "20sp",
             padding_y = "12sp",
             halign = "center"
         )
         
         self.window.add_widget(self.textinput)

         button=Button(
             text="Premi per bestemmiare",
             font_size ="20sp",
             bold = True,
             background_color ="#FF0000",
             size_hint =(.8, .2)
         )

         button.bind(on_press=self.download)
         self.window.add_widget(button)
         

         return self.window

    def download(self,instance):
         link=self.textinput.text
         yt = pytube.YouTube(link)
         #stream = yt.streams.get_highest_resolution()
         stream = yt.streams.filter(only_audio=True).first()
         stream.download()

if __name__ ==" __main__":
    YourSpotipy().run()
