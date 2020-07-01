import tkinter as tk
from math import *

root = tk.Tk()
root.option_add('*font', ('', 14))

# 式を格納するオブジェクト
buffer = tk.StringVar()
buffer.set("")

# 計算
def calc(event):
    if buffer.get():
        value = eval(buffer.get())
        buffer.set(str(value))

# エントリー
e = tk.Entry(root, textvariable = buffer)
e.pack()
e.focus_set()

# バインディング
e.bind('<Return>', calc)

root.mainloop()