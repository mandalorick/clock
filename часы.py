from tkinter import *
from time import strftime


# Constants
WINDOW_WIDTH = 75
WINDOW_HAIGHT = 40
BG_COLOR ='#37474f'
FG_COLOR = 'white'
COLOR_H = '#00897b'
COLOR_M = '#4A8FE7'
COLOR_S = '#8e24aa'

def create_obj():
    s_x, s_y = 100, 100

    for i in range(3):
        label = Label(window, font = ('Futura PT', 50),
                        bg= COLOR_H, fg =FG_COLOR, text = '13')
        label.place(x = s_x, y = s_y, width=150, height=150)
        s_x += 200
        label_clock.append(label)

    label_clock[1].config(bg=COLOR_M)
    label_clock[2].config(bg=COLOR_S)

    s_x, s_y = 100, 275

    for i in range(3):
        label = Label(window, font=('Futura PT', 25),
                      bg=COLOR_H, fg=FG_COLOR, text='часы')
        label.place(x=s_x, y=s_y, width=150, height=150)
        s_x += 200
        label_text.append(label)
    label_text[1].config(bg = COLOR_M, text ='минуты')
    label_text[2].config(bg=COLOR_S, text='секунды')

def update_clock():
    h = strftime('%H')
    m = strftime('%M')
    s = strftime('%S')

    label_clock[0].config(text = '{}'.format(h))
    label_clock[1].config(text = '{}'.format(m))
    label_clock[2].config(text = '{}'.format(s))
    window.after(1000, update_clock)


window = Tk()
window.title('часики')
window.resizable(False, False)

canvas = Canvas(window, bg =BG_COLOR, height=WINDOW_HAIGHT, width=WINDOW_WIDTH)
canvas.place(x = 0, y = 0)

window.geometry('750x400')

label_clock = []
label_text = []

create_obj()
update_clock()
window.mainloop()


