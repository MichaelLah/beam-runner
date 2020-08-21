from pynput import keyboard
# Press ⌃R to execute it or replace it with your code.
import os
import subprocess

KATA_OPTIONS = {
    1: 'JS Kata',
    2: 'Ruby Kata',
    3: 'Marketing Kata'
}

MENU_OPTIONS = {
    1: 'open repo',
    2: 'start beam-api',
    3: 'start js-frontend',
    4: 'start docker',
    5: 'start auth server',
    6: 'Full environment start'
}

REPO_OPTIONS = {
    1: "beam-api",
    2: "js-frontend",
    3: 'auth-server',
    4: 'mobile app',
    5: 'Katas',
    6: 'Perks server',
    7: 'PETL',
    8: 'beam-sftp-dev'
}

beam_api_dir = '/Users/michaellah/Documents/GitHub/beam-api'
docker_dir = '.docker/web-services.yml'
beam_js_dir = '/Users/michaellah/Documents/GitHub/js-frontend'
beam_auth_dir = '/Users/michaellah/Documents/GitHub/authentication-server'


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


def start_auth_server():
    subprocess.run(['rubymine', beam_api_dir])


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
    print_options(KATA_OPTIONS)
    kata_option = input()
    if kata_option == KATA_OPTIONS['JS_KATA']:
        subprocess.run(['rubymine', beam_js_dir])
    elif kata_option == '2':
        pass
    elif kata_option == '3':
        pass
    elif kata_option == '4':
        docker()
    elif kata_option == '5':
        pass


def repo_options():
    print_options(REPO_OPTIONS)
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
        kata_options()
    elif repo_option == '6':
        pass
    elif repo_option == '7':
        pass
    elif repo_option == '8':
        pass


def print_options(options_hash):
    for x in options_hash:
        print(f'{x}. {options_hash[x]}')
    print('>> ', end='')


if __name__ == '__main__':
    print_options(MENU_OPTIONS)
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
        start_auth_server()
    elif option == '6':
        pass

    # with keyboard.Listener(
    #         on_press=on_press,
    #         on_release=on_release) as listener:
    #     listener.join()