import tkinter as tk

root = tk.Tk()
root.geometry(F'120x80')

def push():
  print('clicked.')

btn = tk.Button(root, text='Click!', command=push)
btn.place(x=0, y=0, w=100, h=60)

root.mainloop()
