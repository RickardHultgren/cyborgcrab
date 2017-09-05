import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image

class CrabApp(App):
  def build(self):
	return Image(source='crab.png')

CrabApp().run()

