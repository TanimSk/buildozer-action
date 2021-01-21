from kivy.clock import Clock
from kivy.animation import Animation
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.app import App
from kivy.uix.screenmanager import Screen

global label, label1, button, btn1, btn2, btn3, laps, i, j, k, t, num, clock_ss

i = 0
j = 0
k = 0
t = 0
num = 0
clock_ss = None
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
    global i, j, k, t, laps, num, clock_ss
    Clock.unschedule(clock_ss)
    laps = []
    num = 0
    t = 0
    i = 0
    j = 0
    k = 0
    button.text = "start"
    label1.text = "00"
    label.text = "00:00"


def playclock(x):

    global t
    global clock_ss
    Animation(color=(50 / 255, 168 / 255, 82 / 255, 1)).start(label)

    Animation(opacity=1).start(btn1)
    btn1.disabled = False

    Animation(opacity=1).start(btn2)
    btn2.disabled = False

    label1.color = "399964"

    if t == 1:
        button.text = "Renew"
        Clock.unschedule(clock_ss)
        t = 0

    else:
        clock_ss = Clock.schedule_interval(tic, .01)
        button.text = "stop"
        t = 1


def tic(arg):
    global i, j, k, t

    i = i + 1
    label1.text = str(i).zfill(2)
    label.text = str(k).zfill(2) + ':' + str(j).zfill(2)

    if i == 100:
        j = j + 1
        i = 0
        if j == 60:
            k += 1
            j = 0


class MainApp(App):

    def build(self):
        global label, label1, button, btn1, btn2, btn3

        layout = Screen()
        label = Label(text='00:00', halign="center", center_y=150, color='d1d1d1', font_size='70sp')

        label1 = Label(text='00', halign="center", center_y=80, color='d1d1d1', font_size='45sp')

        label2 = Label(text='© By Tanim Sk \n tanimsk@outlook.com', halign="center", center_y=250, color='d1d1d1',
                       font_size='10sp')

        button = Button(text='GO!', pos_hint={"center_x": .5, "center_y": .3},
                        size_hint=(None, None),
                        size=(35, 35))
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

        btn3 = Button(text='See recorded laps', pos_hint={"center_x": .5, "center_y": .1},
                      size_hint=(None, None),
                      size=(55, 35))

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

        return layout


if __name__ == "__main__":
    MainApp().run()
