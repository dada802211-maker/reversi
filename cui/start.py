from . import command
from rev import info
from ui import proc

# メインループ
def loop():
    proc.start()    # 開始

    while True:
        if info.info['is_end']:
            break

        print('input: x y => "3 2"')
        res = command.get()
        print(' ')

        if res['err']:
            print('Error')
            continue

        proc.put(res['x'], res['y'])
