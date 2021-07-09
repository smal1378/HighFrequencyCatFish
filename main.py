import threading
import time
import tkinter


def event_loop():
    while True:
        time.sleep(sleep_time)
        clock_callback()


def speed_checker():
    def calculate_speed():
        s = 0
        for i in range(current_d, current_d+len(d)-1):
            s += d[(i+1) % len(d)] - d[i % len(d)]
        if s != 0:
            s = s / 10 ** 9  # change from ns to s
            clock_speed = f"{round(1 / (s / (len(d) - 1)), 2)}Hz"
        else:
            clock_speed = "N/A"
        lab.config(text=clock_speed)
        win.after(500, calculate_speed)  # rerun the func in 50ms
    win = tkinter.Tk()
    lab = tkinter.Label(win, text="N/A")
    lab.pack()
    calculate_speed()
    win.mainloop()


def clock_callback():
    global current_d
    d[current_d % len(d)] = time.time_ns()
    current_d = (current_d + 1) % len(d)


sleep_time = 0
d = [0] * 500
current_d = 0
thread1 = threading.Thread(target=event_loop)
thread2 = threading.Thread(target=speed_checker)
thread1.start()
thread2.start()
