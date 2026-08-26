import config

from cui import start as cui
# from gui import start as gui

# from rev import data, board_group
# data.board = board_group.get(['win', 'lose', 'skip_e', 'skip_m'][0])    # 盤面の選択

config.init_from_args()

#---
from rev import info
from ui import render

info.update() # 情報更新
render.print_info(info.info)   # 情報出力
#---

if config.ui_type == config.TYPE_CUI:
  cui.loop()    # メインループ
if config.ui_type == config.TYPE_GUI:
  print('This is GUI')

