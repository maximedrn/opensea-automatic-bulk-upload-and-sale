"""
@author: Maxime.

Github: https://github.com/maximedrn
Version: 1.1
"""

# Colorama module: pip install colorama
from colorama import init, Fore, Style

# Selenium module imports: pip install selenium
from selenium import webdriver
from selenium.common.exceptions import TimeoutException as TE
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Python default import.
from time import sleep
from glob import glob
import os


"""Colorama module constants."""
init(convert=True)  # Init colorama module.
red = Fore.RED  # Red color.
green = Fore.GREEN  # Green color.
yellow = Fore.YELLOW  # Yellow color.
reset = Style.RESET_ALL  # Reset color attribute.


class Settings(object):
    """Contains all settings of upload."""

    def __init__(self, file: str, filetype: str) -> None:
        """Open Settings JSON file and read it."""
        self.filetype = filetype[1:]  # Type of data file.
        if self.filetype == 'json':
            from json import loads
            self.file = loads(open(file, encoding='utf-8').read())['nft']
            self.len_file = len(self.file)  # Lenght of file.
        elif self.filetype == 'csv':
            self.file = open(file, encoding='utf-8').read().splitlines()[1:]
            self.len_file = len(self.file)  # Lenght of file.
        elif self.filetype == 'xlsx':
            from pandas import read_excel
            self.file = read_excel(file)  # Read Excel (XLSX) file.
            self.len_file = self.file.shape[0]  # Get number of rows.
            self.file = self.file.to_dict()  # Transform XLSX to dict.
        else:
            import sys
            sys.exit(f'{red}File extension is not support.{reset}')

    def create_parameters(self, parameters: list) -> None:
        """Create parameters."""
        self.file_path = str(parameters[0])
        self.nft_name = str(parameters[1])
        self.external_link = parameters[2]
        self.description = str(parameters[3])
        self.collection = str(parameters[4])
        self.properties: list = self.type_parameters(
            parameters[5], 2)  # [[type, name], ...]
        self.levels: list = self.type_parameters(
            parameters[6], 3)  # [[name, from, to], ...]
        self.stats: list = self.type_parameters(
            parameters[7], 3)  # [[name, from, to], ...]
        self.unlockable_content: list = parameters[8]  # [bool, text]
        self.explicit_and_sensitive_content: bool = parameters[9]
        self.supply: int = parameters[10]
        self.blockchain: str = parameters[11]

    def type_parameters(self, parameters: list, _range: int) -> list:
        """Change element's type of some parameters."""
        if len(parameters) > 0:
            if type(parameters[0]) == list:
                for parameter in range(len(parameters)):
                    for element in range(_range):
                        parameters[parameter][element] = \
                            str(parameters[parameter][element])
            else:
                for element in range(_range):
                    parameters[element] = str(parameters[element])
        return parameters

    def get_nft(self, nft: int) -> None:
        """Get all settings of NFT."""
        self.nft = nft
        if self.filetype == 'json':
            self.json_file()
        elif self.filetype == 'csv':
            self.csv_file()
        elif self.filetype == 'xlsx':
            self.xlsx_file()

    def csv_file(self) -> None:
        """Transform CSV file into a list."""
        self.create_parameters(self.type_checker(self.file[self.nft]))

    def xlsx_file(self) -> None:
        """Transform XLSX file into a list."""
        self.create_parameters(self.type_checker(
            [self.file[element].get(self.nft) for element in self.file]))

    def type_checker(self, nft_settings: list) -> list:
        """Type with correctly string element in list."""
        from ast import literal_eval
        _list = []
        nft_settings = nft_settings.split(';') \
            if self.filetype == 'csv' else nft_settings
        for element in nft_settings:
            element = str(element).strip()  # Remove whitespaces.
            # Check if element is a list like.
            if element != '':
                if element[0] == '[' and element[len(element) - 1] == ']':
                    element = literal_eval(element)
                # Check if element is a boolean like.
                elif element == 'True' or element == 'False':
                    element = bool(element)
                # Check if element is a integer like.
                elif element.isdigit():
                    element = int(element)
            _list.append(element)
        return _list

    def json_file(self) -> None:
        """Transform JSON list/dict to a whole list."""
        nft_settings = self.file[self.nft]
        # Get key's value from the NFT data.
        nft_settings = [nft_settings[settings] for settings in nft_settings]
        _list = []  # Init a new list.
        for element in nft_settings:  # Take each element in list.
            _list.append(self.dict_checker(element))  # Check element.
        # Create parameters from list.
        self.create_parameters(_list)

    def dict_checker(self, element):
        """Check if element is a dict or not."""
        if type(element) == list:  # If element is a list.
            final_list = []  # Final list that will be return.
            for item in element:  # For each item in this list.
                temp_list = []  # Store all key's value.
                if type(item) == dict:  # If element is a dict.
                    for key in item:  # For each key in dict (item).
                        temp_list.append(item.get(key))  # Get key's value.
                else:
                    temp_list = item  # Do nothing.
                final_list.append(temp_list)  # Append each temp list.
            return final_list
        else:
            return element  # Else return the same element.


class Opensea(object):
    """Main class of Opensea automatic uploader."""

    def __init__(self, password: str, recovery_phrase: str) -> None:
        """Get the password and the recovery_phrase from the text file."""
        # Get recovery phrase of MetaMask wallet.
        self.recovery_phrase = recovery_phrase
        self.password = password  # Get new password.
        # Used files path.
        self.webdriver_path = 'assets/chromedriver.exe'
        self.metamask_extension_path = 'assets/MetaMask.crx'
        self.driver = self.webdriver()  # Start new webdriver.
        # Opensea URLs.
        self.login_url = 'https://opensea.io/login?referrer=%2Fasset%2Fcreate'
        self.create_url = 'https://opensea.io/asset/create'

    def webdriver(self):
        """Start webdriver and return state of it."""
        options = webdriver.ChromeOptions()  # Configure options for Chrome.
        options.add_extension(self.metamask_extension_path)  # Add extension.
        # options.add_argument("headless")  # Headless ChromeDriver.
        options.add_argument("log-level=3")  # No logs is printed.
        options.add_argument("--mute-audio")  # Audio is muted.
        driver = webdriver.Chrome(self.webdriver_path, options=options)
        driver.maximize_window()  # Maximize window to reach all elements.
        return driver

    def element_clickable(self, element: str) -> None:
        """Click on element if it's clickable using Selenium."""
        WDW(self.driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, element))).click()

    def element_visible(self, element: str, timer: int = 5):
        """Check if element is visible using Selenium."""
        return WDW(self.driver, timer).until(EC.visibility_of_element_located(
            (By.XPATH, element)))

    def element_send_keys(self, element: str, keys: str) -> None:
        """Send keys to element if it's visible using Selenium."""
        try:
            WDW(self.driver, 5).until(EC.visibility_of_element_located(
                (By.XPATH, element))).send_keys(keys)
        except TE:
            # Some elements are not visible but are still present.
            WDW(self.driver, 5).until(EC.presence_of_element_located(
                (By.XPATH, element))).send_keys(keys)

    def clear_text(self, element) -> None:
        """Clear text from input."""
        self.element_clickable(element)
        webdriver.ActionChains(self.driver).key_down(Keys.CONTROL).perform()
        webdriver.ActionChains(self.driver).send_keys("a").perform()
        webdriver.ActionChains(self.driver).key_up(Keys.CONTROL).perform()

    def window_handles(self, window_number: int) -> None:
        """Check for window handles and wait until a specific tab is opened."""
        wait = 0
        while True:
            # If asked tab is opened.
            sleep(2)
            if len(self.driver.window_handles) == window_number + 1:
                return True
            elif wait == 10:
                return False
            wait += 1

    def metamask(self) -> None:
        """Login to MetaMask extension."""
        print('Login to MetaMask extension.', end=' ')
        # Switch to MetaMask extension's tab.
        self.driver.switch_to.window(self.driver.window_handles[0])
        # Refresh MetaMask extension's tab while extension is not loaded.
        while True:
            # If page is fully loaded.
            if 'initialize' in self.driver.current_url:
                break
            self.driver.refresh()  # Reload page.
            sleep(1)  # Wait 1 second.
        # Click on "Start" button.
        self.element_clickable(
            '//*[@id="app-content"]/div/div[3]/div/div/div/button')
        # Click on "Import wallet" button.
        self.element_clickable('//*[@id="app-content"]/div/div[3]/div/div/'
                               'div[2]/div/div[2]/div[1]/button')
        # Click on "I agree" button.
        self.element_clickable('//*[@id="app-content"]/div/div[3]/div/div/'
                               'div/div[5]/div[1]/footer/button[2]')
        # Input recovery phrase.
        self.element_send_keys('//*[@id="app-content"]/div/div[3]/div/div/'
                               'form/div[4]''/div[1]/div/input',
                               self.recovery_phrase)
        # Input new password.
        self.element_send_keys('//*[@id="password"]', self.password)
        self.element_send_keys('//*[@id="confirm-password"]', self.password)
        # Check "I have read and agree to the..." checkbox.
        self.element_clickable(
            '//*[@id="app-content"]/div/div[3]/div/div/form/div[7]/div')
        # Click on "Import" button.
        self.element_clickable(
            '//*[@id="app-content"]/div/div[3]/div/div/form/button')
        # Click on "All done" button.
        self.element_clickable(
            '//*[@id="app-content"]/div/div[3]/div/div/button')
        print(f'{green}Logged to Metamask extension.{reset}')

    def opensea_login(self) -> None:
        """Login to Opensea using Metamask."""
        print('Login to Opensea.', end=' ')
        self.driver.switch_to.window(self.driver.window_handles[1]) \
            if self.window_handles(1) else self.retry_login(0)
        self.driver.get(self.login_url)  # Go to Opensea login URL.
        # Click on "Metamask" button in list of wallet.
        ul = len(self.element_visible(
            '//*[@id="__next"]/div[1]/main/div/div/div/div[2]/ul'
        ).find_elements_by_tag_name('li'))
        for li in range(ul):
            li += 1  # Add 1 to start li element at li[1].
            # Check if button text contains "MetaMask".
            if self.element_visible(
                    '//*[@id="__next"]/div[1]/main/div/div/div/div[2]/ul/li'
                    f'[{li}]/button/div[2]/span').text == 'MetaMask':
                # Click on Metamask button.
                self.element_clickable('//*[@id="__next"]/div[1]/main/div/div'
                                       f'/div/div[2]/ul/li[{li}]/button')
                break
        # Switch on MetaMask popup tab.
        self.driver.switch_to.window(self.driver.window_handles[2]) \
            if self.window_handles(2) else self.retry_login(0)
        # Click on "Next" button.
        self.element_clickable('//*[@id="app-content"]/div/div[3]/div/'
                               'div[2]/div[4]/div[2]/button[2]')
        # Click on "Connect" button.
        self.element_clickable('//*[@id="app-content"]/div/div[3]/div/'
                               'div[2]/div[2]/div[2]/footer/button[2]')
        self.metamask_sign()
        # Reload page and retry to log in to Opensea if failed.
        try:
            WDW(self.driver, 10).until(EC.url_to_be(self.create_url))
            print(f'{green}Logged to Opensea.{reset}\n')
        except TE:
            self.retry_login()

    def metamask_sign(self) -> None:
        """Metamask confirm connection."""
        # Switch on MetaMask popup tab.
        self.driver.switch_to.window(self.driver.window_handles[2]) \
            if self.window_handles(2) else self.retry_login(0)
        # Click on "Sign" button.
        self.element_clickable(
            '//*[@id="app-content"]/div/div[3]/div/div[3]/button[2]')
        # Switch back to Opensea tab.
        self.driver.switch_to.window(self.driver.window_handles[1]) \
            if self.window_handles(1) else self.retry_login(0)

    def retry_login(self, value: int = 1) -> None:
        """Retry to log in to Opensea after an error occured."""
        print(f'{red}Failed to login to Opensea, Retrying.{reset}')
        if value == 0:
            self.opensea_login()
        else:
            self.driver.get(self.create_url)
            self.metamask_sign()

    def opensea_upload(self, number: int) -> None:
        """Upload multiple NFTs automatically on Opensea."""
        try:
            print(f'Uploading NFT n°{number}/{len(settings.file)}.',
                  end=' ')
            # Go to Opensea login URL.
            self.driver.get(self.create_url + '?enable_supply=true')
            # Upload NFT file.
            if not os.path.exists(settings.file_path) \
                    or settings.file_path == '':
                raise TE('File doesn\'t exist.')
            self.element_send_keys('//*[@id="media"]', settings.file_path)
            # Input NFT name.
            if settings.nft_name == '':
                raise TE('Missing NFT Name.')
            self.element_send_keys('//*[@id="name"]', settings.nft_name)
            # Input external link.
            if settings.external_link != '':
                self.element_send_keys(
                    '//*[@id="external_link"]', settings.external_link)
            # Input description.
            if settings.description != '':
                self.element_send_keys(
                    '//*[@id="description"]', settings.description)
            # Input collection and select it.
            if settings.collection != '':
                self.element_send_keys(
                    '//*[@id="__next"]/div[1]/main/div/div/section/div/form/'
                    'div[5]/div/div[2]/input', settings.collection)
                try:
                    self.element_clickable(
                        '//*[contains(@id, "tippy")]/div/div/div/ul/li/button')
                except Exception:
                    raise TE('Collection doesn\'t exist')
            # Add properties, levels and stats.
            parameters = [settings.properties, settings.levels, settings.stats]
            for index in range(3):
                if len(parameters[index]) > 0:
                    # Change element from list of string to list of list.
                    # https://github.com/maximedrn/opensea_automatic_uploader/issues/1
                    if type(parameters[index][0]) != list:
                        parameters[index] = [parameters[index]]
                    # Click on "+" button for properties, levels and stats.
                    self.element_clickable(
                        '//*[@id="__next"]/div[1]/main/div/div/section/div/'
                        f'form/section/div[{index + 1}]/div/div[2]/button')
                    parameter = 0
                    for element in parameters[index]:
                        # If there are more than 1 element.
                        if parameter > 0:
                            # Click on "Add more" button.
                            self.element_clickable(
                                f'/html/body/div[{index + 2}]/div/div/div/'
                                'section/button')
                        parameter += 1
                        self.element_send_keys(
                            f'/html/body/div[{index + 2}]/div/div/div/section/'
                            f'table/tbody/tr[{parameter}]/td[1]/div/div/input',
                            element[0])
                        if len(element) == 3:
                            actual_element = (
                                f'/html/body/div[{index + 2}]/div/div/div/'
                                f'section/table/tbody/tr[{parameter}]/td[3]'
                                '/div/div/input')
                            self.clear_text(actual_element)
                            self.element_send_keys(actual_element, element[2])
                        actual_element = (
                            f'/html/body/div[{index + 2}]/div/div/div/section/'
                            f'table/tbody/tr[{parameter}]/td[2]/div/div/input')
                        self.clear_text(actual_element)
                        self.element_send_keys(actual_element, element[1])
                    # Click on "Save" button.
                    self.element_clickable(f'/html/body/div[{index + 2}]/div'
                                           '/div/div/footer/button')
            # Click on "Unlockable Content" switch if true.
            if settings.unlockable_content != '':
                if len(settings.unlockable_content) > 0:
                    if settings.unlockable_content[0]:
                        self.element_send_keys(
                            '//*[@id="unlockable-content-toggle"]', Keys.ENTER)
                        # Send text content.
                        self.element_send_keys(
                            '//*[@id="__next"]/div[1]/main/div/div/section/div'
                            '/form/section/div[4]/div[2]/textarea',
                            settings.unlockable_content[1])
            # Click on "Explicit & Sensitive Content" switch if true.
            if settings.explicit_and_sensitive_content != '':
                if settings.explicit_and_sensitive_content:
                    self.element_send_keys(
                        '//*[@id="explicit-content-toggle"]', Keys.ENTER)
            # Set number of supply.
            if settings.supply != '' and type(settings.supply) == int:
                if '?enable_supply=true' in self.driver.current_url \
                        and settings.supply > 1:
                    self.element_send_keys(
                        '//*[@id="supply"]', settings.supply)
            # Set Blockchain.
            if settings.blockchain != '':
                blockchain = self.element_visible('//*[@id="chain"]')
                if blockchain.get_attribute('value') != settings.blockchain:
                    # Click on bottom sheet.
                    self.element_clickable(
                        '//*[@id="__next"]/div[1]/main/div/div'
                        '/section/div/form/div[7]/div/div[2]')
                    # Get lenght of elements list.
                    ul = len(self.element_visible(
                        '//*[@id="tippy-9"]/div/div/div/ul'
                    ).find_elements_by_tag_name('li'))
                    # Find Blockchain in list.
                    for li in range(ul):
                        li += 1  # Add 1 to start li element at li[1].
                        # Check if span text contains Blockchain.
                        if self.element_visible(
                            f'//*[@id="tippy-9"]/div/div/div/ul/li[{li}]'
                            '/button/div[2]/span[1]').text \
                                == settings.blockchain:
                            # Click on specific Blockchain button.
                            self.element_clickable('//*[@id="tippy-9"]/div/div'
                                                   f'/div/ul/li[{li}]/button')
                            break
            # Click on "Create" button.
            self.element_clickable('//*[@id="__next"]/div[1]/main/div/div/'
                                   'section/div/form/div/div[1]/span/button')
            # Check if done.
            self.element_visible('/html/body/div[5]/div/div/div/div[1]', 10)

            # TODO: Sell NFT.
            """
            # Sell NFT.
            self.driver.get(self.driver.current_url + '/sell')
            """

            print(f'{green}Done.{reset}')
        except TE as error:
            print(f'{red}Failed: {error}{reset}')


def cls() -> None:
    """Clear console function."""
    # Clear console for Windows using 'cls' and Linux & Mac using 'clear'.
    os.system('cls' if os.name == 'nt' else 'clear')


def read_file(file_: str, question: str) -> str:
    """Read file or ask for data to write in text file."""
    if not os.path.isfile(f'assets/{file_}.txt'):
        open(f'assets/{file_}.txt', 'a')
    with open(f'assets/{file_}.txt', 'r+', encoding='utf-8') as file:
        text = file.read()
        if text == '':
            text = input(question)
            if input(f'Do you want to save your {file_} in'
                     ' text file? (y/n) ').lower() == 'y':
                file.write(text)
                print(f'{green}Saved.{reset}')
            else:
                print(f'{yellow}Not saved.{reset}')
        return text


def data_file() -> str:
    """Read data folder and extract JSON, CSV and XLSX files."""
    while True:
        folder = [glob(f'data/{extension}')
                  for extension in ['*.json', '*.csv', '*.xlsx']]
        print(f'{yellow}\nChoose your file:{reset}')
        file_number = 0
        files = []
        print('0 - Browse file on PC.')
        for extension in folder:
            for file in extension:
                file_number += 1
                files.append(file)
                print(f'{file_number} - {file}')
        answer = input('File number: ')
        cls()  # Clear console.
        if answer.isdigit():
            if int(answer) == 0:
                # Browse file on PC.
                from tkinter import Tk
                from tkinter.filedialog import askopenfilename
                Tk().withdraw()  # Hide Tkinter tab.
                return askopenfilename(filetypes=[('', '.json .csv .xlsx')])
            elif int(answer) <= len(files):
                return files[int(answer) - 1]
            else:
                print(f'{red}File doesn\'t exist.{reset}')
        else:
            print(f'{red}Answer must be an integer.{reset}')


if __name__ == '__main__':

    cls()  # Clear console.

    print(f'{green}Made by Maxime. '
          f'\n@Github: https://github.com/maximedrn{reset}')

    password = read_file('password', '\nWhat is your MetaMask password? ')
    recovery_phrase = read_file('recovery_phrase',
                                '\nWhat is your MetaMask recovery phrase? ')

    file = data_file()  # Ask for file.
    # Init Settings class.
    settings = Settings(file, os.path.splitext(file)[1])
    # Init Opensea class and send password and recovery phrase.
    opensea = Opensea(password, recovery_phrase)
    opensea.metamask()  # Connect to Metamask.
    opensea.opensea_login()  # Connect to Opensea.

    # Upload each NFT one by one.
    for element in range(settings.len_file):
        settings.get_nft(element)  # Get data of the NFT.
        opensea.opensea_upload(element + 1)  # Upload it.
