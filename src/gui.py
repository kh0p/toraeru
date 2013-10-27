#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.button import Button

kivy.require('1.7.3')
text =""

class ShowLogo(Image):
    def __init__(self,**kwargs):
        super(Image, self).__init__(**kwargs)


class GetInfo(GridLayout):
    def __init__(self,**kwargs):
        super(GetInfo, self).__init__(**kwargs)
        self.cols = 2
        self.text=text

        self.add_widget(Label(text='Gelbooru limit'))
        self.limit = TextInput(text="100",multiline=False)
        self.add_widget(self.limit)

        def on_text(instance,value):
            print('widget: ',instance,' - val: ',value)

        def on_enter(instance,value):
            print('user pressed enter in: ',instance)

        if self.limit.bind(on_text_validate=on_enter):
            a = int(outnumb)

    # self.printbutton = Button(text='Print')
    # self.printbutton.bind(on_press=self.callback)
    # self.add_widget(self.printbutton)

    #def callback(self,evt=None):
    # return self.add_widget(Label(text=self.text_input.text))


class AppMain(App):
    def build(self):
        img = Image(source="res/wikipe-tan.png")
        return GetInfo()


AppMain().run()