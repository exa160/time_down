import time
from tkinter import Tk, Label


class TimeShow():  # 实现倒计时

    def __init__(self, time_show=5):
        self.timeShowWin = Tk()
        self.timeShowWin.overrideredirect(True)
        self.timeShowWin.attributes('-alpha', 1)
        self.timeShowWin.attributes('-topmost', True)
        self.timeShowWin.attributes('-transparentcolor', 'red')
        self.time_show = time_show
        self.time_label = Label(self.timeShowWin, text='倒计时{}秒'.format(
            self.time_show), font=('楷体', 12), fg='black', bg='red')
        self.time_label.pack(fill='x', anchor='center')
        self.timeShowWin.geometry(
            '+'+str(int(self.timeShowWin.winfo_screenwidth() - 180))+'+'+str(int(self.timeShowWin.winfo_screenheight() - 65)))
        self.timeShowWin.after(1, self.show)

    def show(self):
        while self.time_show >= 0:
            print('time_label={}'.format(self.time_label))
            self.time_label['text'] = '倒计时{}秒'.format(self.time_show)
            self.timeShowWin.update()
            self.time_show -= 1
            time.sleep(1)
        self.timeShowWin.destroy()

    def start(self):
        print('ok')
        self.timeShowWin.mainloop()


if __name__ == '__main__':
    a = TimeShow(10)
    a.start()
