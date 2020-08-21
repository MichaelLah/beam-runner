from pynput import keyboard
# Press ⌃R to execute it or replace it with your code.
import os
import subprocess

beam_api_dir = '/Users/michaellah/Documents/GitHub/beam-api'
docker_dir = '.docker/web-services.yml'
beam_js_dir = ''

def on_press(key):
    # os.system('clear')
    print(key)
    print("Key pressed")


def on_release(key):
    print("Key released")
    print('\r')
    print()
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def docker():
    print("DOWN!")
    # subprocess.run(f'docker-compose -f {beam_api_dir}{docker_dir} down')
    # TODO replace the rest with subprocess!
    subprocess.run(['docker-compose', '-f', f'{beam_api_dir}/{docker_dir}', "down"], cwd=beam_api_dir)
    print("BUILD!!!")
    subprocess.run(['docker-compose', '-f', f'{beam_api_dir}/{docker_dir}', "build"], cwd=beam_api_dir)
    print("UP!")
    subprocess.run(['docker-compose', '-f', f'{beam_api_dir}/{docker_dir}', "up", "-d"], cwd=beam_api_dir)

    # cd
    # ~ / Documents / GitHub / beam - api /
    # docker - compose - f.docker / web - services.yml down
    # docker - compose - f.docker / web - services.yml
    # build
    # docker - compose - f.docker / web - services.yml
    # up - d

def print_options():
    os.system('ls')
    print('1. Full environment start')
    print('2. start beam-api ')
    print('3. start js-frontend')
    print('4. start docker')
    print('5. open repo')
    print('>> ', end='')


if __name__ == '__main__':
    print_options()
    print(beam_api_dir)
    option = input()
    if option == '4':
        docker()

    # with keyboard.Listener(
    #         on_press=on_press,
    #         on_release=on_release) as listener:
    #     listener.join()