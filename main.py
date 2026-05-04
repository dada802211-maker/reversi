import config

config.init_from_args()
if config.ui_type == config.TYPE_CUI:
  print('This is CUI')
if config.ui_type == config.TYPE_GUI:
  print('This is GUI')

