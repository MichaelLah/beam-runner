from pynput import keyboard
# Press ⌃R to execute it or replace it with your code.
import os
import subprocess

beam_api_dir = '/Users/michaellah/Documents/GitHub/beam-api'
docker_dir = '.docker/web-services.yml'
beam_js_dir = '/Users/michaellah/Documents/GitHub/js-frontend'

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


def open_beam_api():
    subprocess.run(['rubymine', beam_api_dir])


def start_beam_api():
    subprocess.run(['./dev_env', 'run'], cwd=beam_api_dir)


def start_js():
    subprocess.run(['yarn', 'start', 'all'], cwd=beam_js_dir)


def open_js():
    subprocess.run(['rubymine', beam_js_dir])


def docker():
    subprocess.run(['docker-compose', '-f', f'{beam_api_dir}/{docker_dir}', "down"], cwd=beam_api_dir)
    subprocess.run(['docker-compose', '-f', f'{beam_api_dir}/{docker_dir}', "build"], cwd=beam_api_dir)
    subprocess.run(['docker-compose', '-f', f'{beam_api_dir}/{docker_dir}', "up", "-d"], cwd=beam_api_dir)


def kata_options():
    print('1. JS Kata')
    print('2. Ruby Kata')
    print('3. Marketing Kata')
    kata_option = input()
    if option == '1':
        repo_options()
    elif option == '2':
        pass
    elif option == '3':
        pass
    elif option == '4':
        docker()
    elif option == '5':
        pass


def repo_options():
    print('1. beam-api')
    print('2. js-frontend')
    print('3. auth-server')
    print('4. mobile app')
    print('5. Katas')
    print('6. Perks server')
    print('7. PETL')
    print('8. beam-sftp-dev')
    repo_option = input()

    if repo_option == '1':
        pass
    elif repo_option == '2':
        open_js()
    elif repo_option == '3':
        pass
    elif repo_option == '4':
        pass
    elif repo_option == '5':
        kata_options
    elif repo_option == '6':
        pass
    elif repo_option == '7':
        pass
    elif repo_option == '8':
        pass


    # print('5. JS kata')
    # print('6. Ruby kata')
def print_options():
    print('1. open repo')
    print('2. start beam-api ')
    print('3. start js-frontend')
    print('4. start docker')
    print('5. Full environment start')
    print('>> ', end='')


if __name__ == '__main__':
    print_options()
    option = input()
    if option == '1':
        repo_options()
    elif option == '2':
        start_beam_api()
    elif option == '3':
        start_js()
    elif option == '4':
        docker()
    elif option == '5':
        pass

    # with keyboard.Listener(
    #         on_press=on_press,
    #         on_release=on_release) as listener:
    #     listener.join()