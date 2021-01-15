import os
import threading
import time

from kivy.animation import Animation
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.screen import Screen
from pysinewave import SineWave

Window.size = (320, 568)

global label, label1, button, btn1, btn2, btn3, laps, i, j, k, t, num

i = 0
j = 0
k = 0
t = 0
num = 0
laps = []


def lap(x):
    Animation(opacity=1).start(btn3)
    btn3.disabled = False
    global laps, num
    num += 1
    laps.append(label.text + ':' + label1.text + " -- " + str(num) + '\n')


def seelap(x):
    layout2 = GridLayout(cols=1, size_hint_y=None)
    layout2.bind(minimum_height=layout2.setter('height'))

    for l in laps:
        lab = Label(text=l, color='f5e042', font_size='18sp', size_hint_y=None)
        layout2.add_widget(lab)

    root = ScrollView(size_hint=(1, .85))
    root.add_widget(layout2)

    popup = Popup(title='Recorded Laps', content=root, size_hint=(1, .85))
    popup.open()


def res(x):
    time.sleep(0.1)
    global i, j, k, t, laps, num
    laps = []
    num = 0
    t = 2
    i = 0
    j = 0
    k = 0
    button.text = "start"
    label1.text = "00"
    label.text = "00:00"


def playclock(x):
    def plays():
        sinewave = SineWave(pitch=18)
        sinewave.play()
        time.sleep(.12)
        sinewave.stop()
        time.sleep(.12)        

    tr = threading.Thread(target=plays)
    tr.start()

    global t
    Animation(color=(50 / 255, 168 / 255, 82 / 255, 1)).start(label)

    Animation(opacity=1).start(btn1)
    btn1.disabled = False

    Animation(opacity=1).start(btn2)
    btn2.disabled = False

    label1.color = "399964"

    def clockfun():
        global i, j, k, t
        while True:
            i = i + 1
            label1.text = str(i).zfill(2)
            label.text = str(k).zfill(2) + ':' + str(j).zfill(2)
            time.sleep(0.01)

            if i == 100:
                j = j + 1
                i = 0
                if j == 60:
                    k += 1
                    j = 0

            if t == 2:
                t = 0
                break

    if t == 1:
        button.text = "Renew"
        t = 2

    else:
        th = threading.Thread(target=clockfun)
        th.start()
        button.text = "stop"
        t = 1


def on_close(arg):
    os._exit(0)


class TimeMechaApp(MDApp):

    def build(self):
        self.icon = 'icon.jpg'
        self.theme_cls.theme_style = "Dark"
        global label, label1, button, btn1, btn2, btn3

        layout = Screen()
        label = Label(text='00:00', halign="center", center_y=150, color='d1d1d1', font_size='70sp')

        label1 = Label(text='00', halign="center", center_y=80, color='d1d1d1', font_size='45sp')

        label2 = Label(text='© By Tanim Sk \n tanimsk@outlook.com', halign="center", center_y=250, color='d1d1d1',
                       font_size='10sp')

        button = MDRoundFlatButton(text='GO!', pos_hint={"center_x": .5, "center_y": .3},
                                   text_color=(97 / 255, 218 / 255, 1, 1))
        btn1 = Button(text="Lap",
                      background_normal='nor.png',
                      background_down='dow.png',
                      border=(0, 0, 0, 0),
                      size_hint=(None, None),
                      size=(35, 35),
                      pos_hint={"x": 0.68, "y": 0.3},
                      color=(245 / 255, 235 / 255, 223 / 255, 1)
                      )

        btn2 = Button(text="Res",
                      background_normal='nor.png',
                      background_down='dow.png',
                      border=(0, 0, 0, 0),
                      size_hint=(None, None),
                      size=(35, 35),
                      pos_hint={"x": 0.215, "y": 0.3},
                      color=(245 / 255, 235 / 255, 223 / 255, 1)
                      )

        btn3 = MDRoundFlatButton(text='See recorded laps', pos_hint={"center_x": .5, "center_y": .1},
                                 text_color=(97 / 255, 218 / 255, 1, 1))

        btn1.disabled = 1
        btn1.opacity = 0
        btn2.disabled = 1
        btn2.opacity = 0
        btn3.disabled = 1
        btn3.opacity = 0

        layout.add_widget(button)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(label)
        layout.add_widget(label1)
        layout.add_widget(label2)

        button.bind(on_press=playclock)
        btn1.bind(on_press=lap)
        btn2.bind(on_press=res)
        btn3.bind(on_press=seelap)

        Window.bind(on_request_close=on_close)

        return layout


TimeMechaApp().run()

