import threading
import time
from tkinter import Tk, Label, Menu
from datetime import datetime, timedelta


def get_hours(weekday):
    if weekday in (0, 1, 3):
        return 20
    else:
        return 17


def start_time():
    now = datetime.now()
    set_datetime = datetime(now.year, now.month, now.day, get_hours(now.weekday()), 30, 0)
    if now > set_datetime:
        set_datetime = datetime(now.year, now.month, now.day, get_hours(now.weekday() + 1 if now.weekday() < 4 else 0),
                                30, 0) + timedelta(days=1 if now.weekday() < 4 else 7 - now.weekday())
    return set_datetime


def diff_time_cal(set_datetime):
    now = datetime.now()
    diff = set_datetime - now
    day = diff.days
    hour = diff.seconds // 3600 + day * 3600 * 24
    minute = (diff.seconds % 3600) // 60
    second = (diff.seconds % 3600) % 60
    return now, hour, minute, second


class TimeShow:  # 实现倒计时

    def __init__(self):
        self._offset_x = 0
        self._offset_y = 0
        self.timeShowWin = Tk()
        self.timeShowWin.overrideredirect(True)
        self.timeShowWin.attributes('-alpha', 1)
        self.timeShowWin.attributes('-topmost', True)
        self.timeShowWin.attributes('-transparentcolor', 'red')
        self.time_label = Label(self.timeShowWin, text='倒计时', font=('楷体', 8), fg='black', bg='red')
        self.time_label.pack(fill='x', anchor='center')
        self.timeShowWin.bind('<Button-1>', self.click_win)
        self.timeShowWin.bind('<B1-Motion>', self.drag_win)
        menu = Menu(self.time_label, tearoff='off')
        menu.add_cascade(label='设置')
        menu.add_command(label='退出', command=self.timeShowWin.destroy)
        self.show_menu(menu)
        self.timeShowWin.geometry(
            '+' + str(int(self.timeShowWin.winfo_screenwidth() - 130)) + '+' + str(
                int(self.timeShowWin.winfo_screenheight() - 63)))

        t = threading.Thread(target=self.show)
        t.setDaemon(True)
        t.start()

    def show(self):
        act_index = ['-', '\\', '|', '/']
        temp_index = 0
        last_start_datetime = start_time()
        next_start_datetime = last_start_datetime
        while True:
            if next_start_datetime != last_start_datetime:
                last_start_datetime = next_start_datetime
            now, hour, minute, second = diff_time_cal(next_start_datetime)
            if now.hour <= get_hours(now.weekday()):
                index = int(f'{now.microsecond:06d}'[:2]) // 25
                if temp_index != index:
                    temp_index = index
                    self.time_label[
                        'text'] = f'{hour:02d}: {minute:02d}{":" if index > 1 else " "} {second:02d} {act_index[index]}'
                    self.timeShowWin.update()
                time.sleep(0.01)
            else:
                if next_start_datetime == last_start_datetime:
                    next_start_datetime = start_time()
                    now, hour, minute, second = diff_time_cal(next_start_datetime)

                index = now.second % 20 // 5
                #     start_datetime = start_time()
                if temp_index != index:
                    temp_index = index
                    self.time_label['text'] = f'--: --{":" if now.second // 2 == 0 else " "} -- {act_index[index]}\n' \
                                              f'{hour:02d}: {minute:02d}-nextD'
                    # self.time_label['text'] = f'{hour:02d}: {minute:02d}{":" if index > 1 else " "} {second:02d} {act_index[index]}'
                    self.timeShowWin.update()
                time.sleep(0.05)

    def start(self):
        self.timeShowWin.mainloop()

    def show_menu(self, menu):
        def set_menu(event):
            menu.post(event.x + self.timeShowWin.winfo_rootx(), event.y + self.timeShowWin.winfo_rooty())
            self.timeShowWin.update()

        self.time_label.bind('<Button-3>', set_menu)

    def drag_win(self, event):
        x = self.timeShowWin.winfo_pointerx() - self._offset_x
        y = self.timeShowWin.winfo_pointery() - self._offset_y
        self.timeShowWin.geometry('+{x}+{y}'.format(x=x, y=y))

    def click_win(self, event):
        self._offset_x = event.x
        self._offset_y = event.y


if __name__ == '__main__':
    print(start_time())
    a = TimeShow()
    a.start()
