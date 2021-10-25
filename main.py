"""
@author: Maxime.

Github: https://github.com/maximedrn
"""

# Colorama module: pip install colorama
from colorama import init, Fore, Style

# Selenium module imports: pip install selenium
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Python default import.
import time
import glob
import sys
import os


"""Colorama module constants."""
init()  # Init colorama module.
red = Fore.RED  # Red color.
green = Fore.GREEN  # Green color.
yellow = Fore.YELLOW  # Yellow color.
reset = Style.RESET_ALL  # Reset color attribute.


class Settings(object):
    """Contains all settings of upload."""

    def __init__(self, file: str, filetype: str) -> None:
        """Open Settings JSON file and read it."""
        self.filetype = filetype[1:]  # Type of data file.
        self.file = open(file, encoding='utf-8').read()  # Read file.
        if self.filetype == 'json':
            import json
            self.file = json.loads(self.file)['nft']
        elif self.filetype == 'csv':
            self.file = self.file.splitlines()[1:]

    def create_parameters(self, parameters: list) -> None:
        """Create parameters."""
        self.file_path = str(parameters[0])
        self.nft_name = str(parameters[1])
        self.external_link = parameters[2]
        self.description = str(parameters[3])
        self.collection = str(parameters[4])
        self.properties: list = parameters[5]  # [[type, name], ...]
        self.type_parameters(self.properties, 2)
        self.levels: list = parameters[6]  # [[name, from, to], ...]
        self.type_parameters(self.levels, 3)
        self.stats: list = parameters[7]  # [[name, from, to], ...]
        self.type_parameters(self.stats, 3)
        self.unlockable_content: list = parameters[8]  # [bool, text]
        self.explicit_and_sensitive_content: bool = parameters[9]
        self.supply: int = parameters[10]
        self.blockchain: str = parameters[11]
        
    def type_parameters(self, parameters: list, _range: int) -> list:
        """Change element's type of some parameters."""
        for parameter in range(len(parameters)):
            for element in range(_range):
                parameters[parameter][element] \
                    = str(parameters[parameter][element])
        return parameters

    def get_nft(self, nft: int) -> None:
        """Get all settings of NFT."""
        self.nft = nft
        if self.filetype == 'json':
            self.json_file()
        elif self.filetype == 'csv':
            self.csv_file()
            
    def csv_file(self) -> None:
        """Transform CSV file into a list."""
        import ast
        nft_settings = self.file[self.nft]
        _list = []
        for element in nft_settings.split(';'):
            element = element.strip()  # Remove whitespaces. 
            # Check if element is a list like.
            if element != '':
                if element[0] == '[' and element[len(element) - 1] == ']':
                    element = ast.literal_eval(element)
                # Check if element is a boolean like.
                elif element == 'True' or element == 'False':
                    element = bool(element)
                # Check if element is an integer like.
                elif element.isdigit():
                    element = int(element)
            _list.append(element)
        self.create_parameters(_list)

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
    """Main class of OpenSea automatic uploader."""

    def __init__(self, password: str, recovery_phrase: str) -> None:
        """Get the password and the recovery_phrase from the text file."""
        # Get recovery phrase of Metamask wallet.
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
        # options.add_argument("headless")  # Headless Chrome driver.
        options.add_argument("log-level=3")  # No logs is printed.
        options.add_argument("--mute-audio")  # Audio is muted.
        driver = webdriver.Chrome(self.webdriver_path, options=options)
        driver.maximize_window()  # Maximize window to reach all elements.
        return driver

    def element_clickable(self, element: str) -> None:
        """Click on element if it's clickable using Selenium."""
        WDW(self.driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, element))).click()

    def element_visible(self, element: str):
        """Check if element is visible using Selenium."""
        return WDW(self.driver, 5).until(EC.visibility_of_element_located(
            (By.XPATH, element)))

    def element_send_keys(self, element: str, keys: str) -> None:
        """Send keys to element if it's visible using Selenium."""
        try:
            WDW(self.driver, 5).until(EC.visibility_of_element_located(
                (By.XPATH, element))).send_keys(keys)
        except TimeoutException:
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
            time.sleep(2)
            if len(self.driver.window_handles) == window_number + 1:
                return True
            elif wait == 10:
                return False
            wait += 1

    def metamask(self) -> None:
        """Login to Metamask extension."""
        print('Login to Metamask extension.', end=' ')
        # Switch to Metamask extension's tab.
        self.driver.switch_to.window(self.driver.window_handles[0])
        # Refresh Metamask extension's tab while extension is not loaded.
        while True:
            # If page is fully loaded.
            if 'initialize' in self.driver.current_url:
                break
            self.driver.refresh()  # Reload page.
            time.sleep(1)  # Wait 1 second.
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
            # Check if button text contains "Metamask".
            if self.element_visible(
                    '//*[@id="__next"]/div[1]/main/div/div/div/div[2]/ul/li'
                    f'[{li}]/button/div[2]/span').text == 'MetaMask':
                # Click on Metamask button.
                self.element_clickable('//*[@id="__next"]/div[1]/main/div/div'
                                       f'/div/div[2]/ul/li[{li}]/button')
                break
        # Switch on Metamask popup tab.
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
        except TimeoutException:
            self.retry_login()

    def metamask_sign(self) -> None:
        """Metamask confirm connection."""
        # Switch on Metamask popup tab.
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
                raise TimeoutException('File doesn\'t exist.')
            self.element_send_keys('//*[@id="media"]', settings.file_path)
            # Input NFT name.
            if settings.nft_name == '':
                raise TimeoutException('Missing NFT Name.')
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
                    raise TimeoutException('Collection doesn\'t exist')
            # Add properties, levels and stats.
            parameters = [settings.properties, settings.levels, settings.stats]
            for index in range(3):
                if len(parameters[index]) > 0:
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
                            '//*[@id="__next"]/div[1]/main/div/div/section/div/'
                            'form/section/div[4]/div[2]/textarea',
                            settings.unlockable_content[1])
            # Click on "Explicit & Sensitive Content" switch if true.
            if settings.explicit_and_sensitive_content != '':
                if settings.explicit_and_sensitive_content:
                    self.element_send_keys(
                        '//*[@id="explicit-content-toggle"]', Keys.ENTER)
            # Set number of supply.
            if settings.supply != '':
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
            self.element_visible('/html/body/div[5]/div/div/div/div[1]')
            
            # TODO: Sell NFT.
            """
            # Sell NFT.
            self.driver.get(self.driver.current_url + '/sell')
            """
            
            print(f'{green}Done.{reset}')
        except TimeoutException as error:
            print(f'{red}Failed: {error}{reset}')


def cls() -> None:
    """Clear console function."""
    # Clear console for Windows using 'cls' and Linux & Mac using 'clear'.
    os.system('cls' if os.name == 'nt' else 'clear')


def read_file(file_: str, question: str) -> str:
    """Read file or ask for data to write in text file."""
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
    while True:
        folder = [glob.glob(f'data/{extension}') 
                  for extension in ['*.json', '*.csv']]
        print(f'{yellow}Choose your file:{reset}')
        file_number = 0
        files = []
        for extension in folder:
            for file in extension:
                file_number += 1
                files.append(file)
                print(f'{file_number} - {file}')
        answer = input('File number: ')
        cls()  # Clear console.
        if answer.isdigit():
            if int(answer) <= len(files):
                return files[int(answer) - 1]
            else:
                print(f'{red}File doesn\'t exist.{reset}')
        else:
            print(f'{red}Answer must be an integer.{reset}')


if __name__ == '__main__':

    cls()  # Clear console.
    password = read_file('password', 'What is your Metamask password? ')
    recovery_phrase = read_file('recovery_phrase',
                                '\nWhat are your Metamask recovery phrase? ')

    cls()  # Clear console.
    file = data_file()  # Ask for file.
    # Init Settings class.
    settings = Settings(file, os.path.splitext(file)[1])
    # Init Opensea class and send password and recovery phrase.
    opensea = Opensea(password, recovery_phrase)
    opensea.metamask()  # Connect to Metamask.
    opensea.opensea_login()  # Connect to Opensea.

    # Upload each NFT one by one.
    for element in range(len(settings.file)):
        settings.get_nft(element)  # Get data of the NFT.
        opensea.opensea_upload(element + 1)  # Upload it.
