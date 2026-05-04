import config

from cui import start as cui

config.init_from_args()
if config.ui_type == config.TYPE_CUI:
  cui.loop()    # メインループ
if config.ui_type == config.TYPE_GUI:
  print('This is GUI')

