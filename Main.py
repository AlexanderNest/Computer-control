import os
import tkinter as tk
from tkinter import messagebox


class Graphics:
    def __init__(self):
        self.root = tk.Tk()

        self.is_timermode = tk.IntVar()  # метка checkbutton
        self.timer_text = tk.StringVar()  # значение поля таймера

        # Создание элементов окна


        self.root.title('Управление компьютером')
        self.shutdown_btn = tk.Button(text="Выключить компьютер", command=self.shutdown)
        self.sleep_btn = tk.Button(text="Спящий режим", command=self.sleep)
        self.timer_btn = tk.Button(text="Перезагрузить компьютер", command=self.restart)
        self.timer_mode_btn = tk.Checkbutton(text='Режим таймера', variable=self.is_timermode,
                                             command=self.changetimerstate)
        self.cancel_btn = tk.Button(text='Отмена таймера', command=self.canceltimer)
        self.timer_textbox = tk.Entry(textvariable=self.timer_text)
        self.timer_textbox.config(state='disabled')

        # размещение элементов на окне
        self.cancel_btn.grid(column=0, row=3, ipadx=10, ipady=6, padx=10, pady=10)
        self.timer_mode_btn.grid(column=2, row=0, ipadx=10, ipady=6, padx=10, pady=10)
        self.shutdown_btn.grid(row=0, column=0, ipadx=10, ipady=6, padx=10, pady=10)
        self.sleep_btn.grid(row=1, column=0, ipadx=10, ipady=6, padx=10, pady=10)
        self.timer_btn.grid(row=2, column=0, ipadx=10, ipady=6, padx=10, pady=10)

        self.timer_textbox.grid(row=1, column=2, ipadx=10, ipady=6, padx=10, pady=10)

        self.root.mainloop()

    # изменение состояния флажка таймера
    def changetimerstate(self):
        if self.is_timermode == 1:
            self.is_timermode = 0
            self.timer_textbox.config(state='normal')
        else:
            self.is_timermode = 1
            self.timer_textbox.config(state='disabled')

    # поле ввода времени, из чч:мм в мин
    def __parseTime(self, time):
        h = time[:2]
        min = time[3:]
        if h.isdigit() and min.isdigit():
            h = int(h)
            min = int(min)

            if h >= 0 and 0 <= min < 60:
                return str(h*60 + min)

    # отменить таймер
    def canceltimer(self):
        self.timer_mode_btn.config(bg='#DCDCDC')
        os.system('shutdown -c')
        tk.messagebox.showinfo(title='Отмена таймера', message='Вы отменили таймер')

    # обработка кнопки выключения
    def shutdown(self):
        if self.is_timermode == 1:
            answer = messagebox.askyesno(title='Выключение компьютера', message='Выключить компьютер?')
            if answer:
                os.system('shutdown -h now')

        else:
            time = self.__parseTime(self.timer_text.get())
            os.system('shutdown -h ' + time)
            tk.messagebox.showinfo(title='Таймер', message='Компьютер будет выключен через ' + time + ' мин')
            print(time)
        self.timer_mode_btn.config(bg='#FFA500')

    def restart(self):
            answer = messagebox.askyesno(title='Перезагрузка компьютера', message='Перезагрузить компьютер?')
            if answer:
                os.system('reboot')



    def sleep(self):
        answer = messagebox.askyesno(title='Режим сна', message='Отправить компьютер в режим сна?')
        if answer:
            os.system('sudo pm-suspend')






window = Graphics()
