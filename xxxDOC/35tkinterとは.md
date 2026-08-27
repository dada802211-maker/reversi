35tkinterとは

PythonでGUIをあつかう標準ライブラリ
tkinterをインポートする
ウィンドウやUI部品を作ったあと、mainloop()を実行することで動作する

import tkinter as tk

root = tk.Tk()
root.geometry(F'120x80')

def push():
  print('clicked.')

btn = tk.Button(root, text='Click!', command=push)
btn.place(x=0, y=0, w=100, h=60)

root.mainloop()

python test.py

  ドキュメント
Python 3.13.5
https://docs.python.org/ja/3.13/library/tkinter.html
https://tkdocs.com/tutorial/widgets.html
https://tkdocs.com/tutorial/morewidgets.html
