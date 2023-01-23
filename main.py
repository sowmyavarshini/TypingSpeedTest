from tkinter import *
import math
timer = None


def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = '00'
    time_text.config(text=f'{count_min}:{count_sec}')
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    if count == 0:
        result()


def result():
    typing_entry.config(state='disabled')
    wpm = 0
    words = sample_text.split()
    text = typing_entry.get(1.0, END).split()
    print(text)
    for i in range(len(text)):
        if i < len(words) and text[i] == words[i]:
            wpm += 1
    wpm_label.config(text=f"You have typed {wpm} words per minute")


def start_timer():
    typing_entry.config(state='normal')
    count_down(1 * 60)


def reset_timer():
    window.after_cancel(timer)
    time_text.config(text='01:00')
    typing_entry.delete(1.0, END)
    wpm_label.config(text='')


window = Tk()
window.title("Typing Speed Test")
window.minsize(width=350, height=550)
window.config(padx=100, pady=50)

start_button = Button(text='Start', command=start_timer)
start_button.grid(row=0, column=0)
start_button.config(padx=10, pady=10)

time_label = Label(text='Time:', font=('Arial', 12, 'bold'))
time_label.place(x=250, y=10)

time_text = Label(text='1:00', font=('Arial', 12, 'bold'))
time_text.place(x=300, y=10)

reset_button = Button(text='Reset', command=reset_timer)
reset_button.grid(row=0, column=3)
reset_button.config(padx=10, pady=10)

sample_label = Label(text='Sample text:', font=('Arial', 12, 'bold'), justify=LEFT)
sample_label.grid(row=1, column=0)
sample_label.config(padx=10, pady=10)

text_label = Label(text='Medical transcription, also known as MT, is an allied health profession '
                        'dealing with the process of transcribing voice-recorded medical reports '
                        'that are dictated by physicians, nurses and other healthcare practitioners. '
                        'Medical reports can be voice files, notes taken during a lecture, or other '
                        'spoken material. These are dictated over the phone or uploaded digitally via '
                        'the Internet or through smart phone apps.', font=('Arial', 12),
                        wraplength=400, justify=LEFT)
text_label.grid(row=2, column=1)
sample_text = 'Medical transcription, also known as MT, is an allied health profession dealing with the ' \
              'process of transcribing voice-recorded medical reports that are dictated by physicians, ' \
              'nurses and other healthcare practitioners.Medical reports can be voice files, notes taken ' \
              'during a lecture, or other spoken material. These are dictated over the phone or uploaded ' \
              'digitally via the Internet or through smart phone apps.'

typing_label = Label(text='Type the words here:', font=('Arial', 12, 'bold'), justify=LEFT)
typing_label.grid(row=3, column=0)

typing_entry = Text(height=10, width=50,  font=('Arial', 12))
typing_entry.place(x=100, y=270)
typing_entry.config(state='disabled')

wpm_label = Label(text='', font=('Arial', 12, 'bold'))
wpm_label.place(x=200, y=460)

window.mainloop()
