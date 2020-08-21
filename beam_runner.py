from pynput import keyboard
# Press ⌃R to execute it or replace it with your code.
import os

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def on_press(key):
    # os.system('clear')
    print("Key pressed")

def on_release(key):
    print("Key released")
    print('\r')
    print()
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def print_options():
    print('1. Full environment start')
    print('2. start beam-api ')
    print('3. start js-frontend')
    print('4. ')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('start')
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
    print(1)
    # print_hi('PyCharm')
    # print (2)
    # keyboard.wait('esc')
    # print (3)
    # keyboard.add_hotkey('up', up)
    # # keyboard.wait()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



