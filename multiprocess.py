# -*- coding: utf-8 -*-
# multiprocess.py

"""
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn
"""


# Utils functions for GUI and CLI.
from app.utils.colors import GREEN, RED, YELLOW, RESET
from app.utils.const import ENTER, FIRST_PAGE, SECOND_PAGE
from app.utils.func import cls, exit

# Common functions for the metadata file.
from app.utils.values import UPLOAD, SALE, UPLOAD_AND_SALE
from app.common.reader import Reader
from app.common.structure import Structure
from app.common.save import Save

# Services functions for Upload/Sale process.
from app.services.webdriver import download_browser

# Main functions.
from main import user

# A Python default import.
from os import getcwd, chdir, system as ossystem
from multiprocessing import Process
from subprocess import Popen
from platform import system
from os.path import abspath
from sys import executable
from requests import post
from json import loads
from time import sleep
from math import ceil


# Mode and details constants.
MODE = {'1': 'upload', '2': 'sale', '1 2': 'upload_and_sale'}
DETAILS = {'1': UPLOAD, '2': SALE, '1 2': UPLOAD_AND_SALE}


def processes_number() -> int:
    """Ask the user for the number of processes."""
    while True:
        processes = input('\nHow many processes do you want to use? ')
        if processes.isdigit() and 0 < int(processes) <= 5:
            return int(processes)
        print(f'{RED}Please enter a number between 1 and 5.{RESET}')


def split_file(file_path: str, part: int, processes: int,
               action: list, action_str: str, starting: int) -> list:
    """Split the file in two files to multiprocess."""
    print(f'\nCreation of part n°{part + 1}/{processes}.')
    action_str = ''.join(action_str)
    reader = Reader(file_path)  # Send the file path.
    structure = Structure(action, reader)  # Send the action.
    save = Save(structure)  # Initialize the Save class.
    # Get odd and even indexes of the file.
    for number in range(part + starting, reader.length_file, processes):
        text = f'Element n°{ceil(number / processes + 1)}/' + \
            f'{ceil(reader.length_file / processes)}.'
        print(text, end='\r')  # Display the number of elements.
        structure.get_data(number)  # Structure metadata.
        # Save it in a temporary file.
        save.save(MODE[action_str], DETAILS[action_str], True)
    print(f'{text} {GREEN}Done.{RESET}')
    return eval(f'save.{MODE[action_str]}_file')


def command_line(wallet_name: str, password: str, recovery_phrase: str,
                 private_key: str, action: str, solver: int, key: str,
                 browser: int, file: str, browser_path: str,
                 system_password: str) -> None:
    """Open a command prompt and then start task.py."""
    python = executable.replace('\\', '/')  # Python path.
    current = abspath(getcwd()).replace('\\', '/')  # Work directory.
    browser_path = browser_path.replace('\\', '/')
    if solver == 4:  # reCAPTCHA Bypasser.
        from pickle import dumps  # Create a copy of the class
        from base64 import b64encode  # and encode it.
        key = str(b64encode(dumps(key)))[2:-1]
    python_command = (
        f'"{python}" task.py --wallet_name="{wallet_name}" '
        f'--password="{password}" --recovery_phrase="{recovery_phrase}" '
        f'--private_key="{private_key}" --action {action} '
        f'--solver={solver if isinstance(solver, int) else 0} '
        f'--key="{key}" --browser={browser} --file="{file}" '
        f'--browser_path="{browser_path}"')
    if system() == 'Darwin':  # MacOS.
        from appscript import app
        python_command = python_command.replace('!', '\!')
        app('Terminal').do_script(
            f'echo "{system_password}" | sudo -i -S ; clear ;'
            f' cd "{current}" ; sudo {python_command}')
    elif system() == 'Windows':  # Windows.
        chdir(current)  # Move to the bot path.
        ossystem(f'start /wait cmd /c "{python_command}"')
    elif system() == 'Linux':  # Linux.
        Popen(f'gnome-terminal  --wait -- /bin/bash -c \'echo "'
              f'{system_password}" | sudo -i -S ; cd "{current}" ; '
              f'sudo {python_command}\'', shell=True)


def install_appscript(python: str) -> None:
    print('\nInstalling the Appscript module.\n')
    for command in (f'"{python}" -m pip', 'pip3'):
        try:
            ossystem(f'{command} install appscript')
            return  # Done.
        except Exception:
            continue  # Retry a second time.
    exit('\nCannot install the AppScript module.')


if __name__ == '__main__':
    try:
        cls()  # Clear console.
        print(FIRST_PAGE)
        input(ENTER)  # Press enter to continue.

        cls()  # Clear console.
        print(SECOND_PAGE)  # License and author.
        # Get user informations and choices.
        wallet_name, password, recovery_phrase, private_key, \
            action, solver, key, browser, file, starting = user()
        processes = processes_number()  # Get the number of processes.
        cls()  # Clear console.
        browser_path = download_browser(browser)  # Download the webdriver.

        if system() == 'Darwin':  # Only for MacOS users.
            try:  # Try to import the Appscript module if it exists.
                from appscript import app
            except ImportError:  # Install the Appscript module.
                install_appscript(executable.replace('\\', '/'))
        system_password = input(
            '\nWhat is your system password to activate the administrator '
            'privileges? ') if system() != 'Windows' else ''

        if solver == 4:  # reCAPTCHA Bypasser.
            from app.services.solvers.solver import Solver
            key = Solver(solver, key)
            key.init_solver()  # Send web instance.

        tasks, action_str = [], ' '.join(str(element) for element in action)
        for number in range(processes):  # Multiprocessing.
            task = Process(target=command_line, args=(
                wallet_name, password, recovery_phrase, private_key,
                action_str, solver, key, browser, split_file(
                    file, number, processes, action, action_str, starting)
                if processes > 1 else file, browser_path, system_password))
            tasks.append(task)  # Add the task the the tasks list.
            task.start()  # Start the task in multiprocess.
            if number != processes - 1:  # Do not wait for the last process.
                print('Waiting 10 seconds before starting the next task.')
                sleep(10)  # Wait 10 seconds before.
        [task.join() for task in tasks]
        print('\nYou can close this tab.')
    except KeyboardInterrupt:
        print(f'\n\n{YELLOW}The program has been '
              f'stopped by the user.{RESET}')
    except Exception as error:
        print(f'{RED}Something went wrong.{RESET} \n{error}')
    exit()  # Exit the program.
