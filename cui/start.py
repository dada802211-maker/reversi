from . import command

# メインループ
def loop():
    while True:
        print('input: x y => "3 2"')
        res = command.get()
        print(' ')

        if res['err']:
            print('Error')
            continue

        print('@', res['x'], res['y'])
