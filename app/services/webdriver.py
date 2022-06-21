#!/usr/bin/python
# app/services/webdriver.py


"""
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn

Copyright © 2022 Maxime Dréan. All rights reserved.
Any distribution, modification or commercial use is strictly prohibited.
"""


# Selenium module imports: pip install selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as SC
from selenium.webdriver.firefox.service import Service as SG
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Webdriver Manager module: pip install webdriver-manager
from webdriver_manager.chrome import ChromeDriverManager as CDM
from webdriver_manager.firefox import GeckoDriverManager as GDM

# Python internal imports.
from ..utils.func import exit
from ..utils.colors import GREEN, RED, YELLOW, RESET

# Python default imports.
from os import name as osname, devnull
from os.path import abspath, exists
from datetime import datetime as dt


class Webdriver:
    """Webdriver class and methods to prevent exceptions."""

    def __init__(self, browser: int, browser_path: str,
                 wallet_name: str, wallet: object, solver: int) -> None:
        """Contains the file paths of the webdriver and the extension."""
        self.metamask_extension_path = abspath(  # MetaMask extension path.
            'assets/MetaMask.xpi' if browser == 1 else 'assets/MetaMask.crx')
        self.coinbase_wallet_extension_path = abspath(
            'assets/CoinbaseWallet.crx')  # Coinbase Wallet extension path.
        self.wallet_name = wallet_name.lower().replace(' ', '_')
        self.browser_path = browser_path  # Get the browser path.
        self.solver = solver  # reCAPTCHA solver number.
        self.wallet = wallet  # Instance of the Wallet class.
        # Start a Chrome (not headless) or Firefox (headless mode) webdriver.
        self.driver = self.firefox() if browser == 1 else self.chrome()
        self.window = browser  # Window handle value.

    def chrome(self) -> webdriver:
        """Start a Chrome webdriver and return its state."""
        options = webdriver.ChromeOptions()  # Configure options for Chrome.
        # Add wallet extension according to user choice
        options.add_extension(eval(f'self.{self.wallet_name}_extension_path'))
        options.add_argument('log-level=3')  # No logs is printed.
        options.add_argument('--mute-audio')  # Audio is muted.
        options.add_argument('--disable-infobars')
        options.add_argument('--disable-popup-blocking')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--lang=en-US')  # Set webdriver language
        options.add_experimental_option(  # to English. - 2 methods.
            'prefs', {'intl.accept_languages': 'en,en_US'})
        options.add_experimental_option('excludeSwitches', [
            'enable-logging', 'enable-automation'])
        if isinstance(self.wallet.recovery_phrase, tuple):
            options.add_argument(  # Set the User Data folder.
                f'--user-data-dir={self.wallet.recovery_phrase[0]}')
            options.add_argument(  # Set the Google Chrome profile.
                f'--profile-directory={self.wallet.recovery_phrase[1]}')
        driver = webdriver.Chrome(service=SC(  # DeprecationWarning using
            self.browser_path), options=options)  # executable_path.
        driver.maximize_window()  # Maximize window to reach all elements.
        return driver

    def firefox(self) -> webdriver:
        """Start a Firefox webdriver and return its state."""
        options = webdriver.FirefoxOptions()  # Configure options for Firefox.
        if self.solver != 1 and self.wallet.recovery_phrase != '' and \
                self.wallet.password != '':  # Not manual solver.
            options.add_argument('--headless')  # Headless mode.
        options.add_argument('--mute-audio')  # Audio is muted.
        options.add_argument('--disable-infobars')
        options.add_argument('--disable-popup-blocking')
        options.add_argument('--disable-dev-shm-usage')
        options.set_preference('intl.accept_languages', 'en,en-US')
        driver = webdriver.Firefox(service=SG(  # DeprecationWarning using
            self.browser_path), options=options,  # executable_path.
            service_log_path=devnull)  # Disable Firefox logs.
        driver.install_addon(self.metamask_extension_path)  # Add extension.
        driver.maximize_window()  # Maximize window to reach all elements.
        return driver

    def quit(self) -> None:
        """Stop the webdriver."""
        try:  # Try to close the webdriver.
            self.driver.quit()
        except Exception:  # The webdriver is closed
            pass  # or no webdriver is started.

    def page_error(self) -> bool:
        """
        Check the actual state of the page and if there is an error.

        Check if the page is correctly displayed (404 page error)
        or if a red message is displayed at the bottom right.
        """
        self.window_handles(1)  # Switch to OpenSea.
        for text in ['This page is lost', 'Something went wrong']:
            if text in self.driver.page_source:
                print(f'{YELLOW}404 page error.{RESET}')
                return True
        try:  # Check if a red message is displayed.
            self.visible('//div[@data-testid="toasts"]', 1)
            print(f'{YELLOW}Red message displayed.{RESET}')
            return True  # It is displayed.
        except Exception:  # No red message is displayed.
            return False

    def clickable(self, element: str) -> None:
        """Click on an element if it's clickable using Selenium."""
        try:
            WDW(self.driver, 5).until(EC.element_to_be_clickable(
                (By.XPATH, element))).click()
        except Exception:  # Some buttons need to be visible to be clickable,
            self.driver.execute_script(  # so JavaScript can bypass this.
                'arguments[0].click();', self.visible(element))

    def visible(self, element: str, timer: int = 5) -> object:
        """Check if an element is visible using Selenium."""
        return WDW(self.driver, timer).until(
            EC.visibility_of_element_located((By.XPATH, element)))

    def send_keys(self, element: str, keys: str) -> None:
        """Send keys to an element if it's visible using Selenium."""
        try:
            self.visible(element).send_keys(keys)
        except Exception:  # Some elements are not visible but are present.
            WDW(self.driver, 5).until(EC.presence_of_element_located(
                (By.XPATH, element))).send_keys(keys)

    def send_date(self, element: str, keys: str, clockface: str = 'A') -> None:
        """Send a date (DD-MM-YYYY HH:MM) to a date input by clicking on it."""
        # From "DD-MM-YYYY" or "hh:mm" to ["DD", "MM", "YYYY"] or ["hh", "mm"].
        keys_ = keys.split('-') if '-' in keys else keys.split(':')
        # From ["DD", "MM", "YYYY"] to ["MM", "DD", "YYYY"].
        if isinstance(keys_, list) and '-' in keys and len(keys_) > 2:
            keys_ = [keys_[1], keys_[0], keys_[2]]  # Switch day and month.
            # ["DD", "MM", "YYYY"] or ["DD", "MM"] according to the year.
            keys_ = keys_ if keys_[-1] == dt.now().year else keys_[:-1]
        if ':' in keys:  # If it is an hour, change AM or PM.
            if int(keys_[0]) > 13:  # Remove 12 hours if it is afternoon.
                keys_[0], clockface = str(int(keys_[0]) - 12), 'P'
            keys_.append(clockface)  # Add "A" or "P".
        for part in range(len(keys_)):  # Add left and rights arrows moves.
            keys_[part] = f'{Keys.ARROW_LEFT}' * len(keys_) + \
                f'{Keys.ARROW_RIGHT}' * part + keys_[part]
        self.clickable(element)  # Click on the date element.
        self.send_keys(element, ''.join(keys_))  # Join and send date or time.


    def clear_text(self, element) -> None:
        """Clear text from an input."""
        self.clickable(element)  # Click on the element then clear its text.
        # Note: change with 'darwin' if it's not working on MacOS.
        control = Keys.COMMAND if osname == 'posix' else Keys.CONTROL
        if self.window == 1:  # GeckoDriver (Mozilla Firefox).
            self.send_keys(element, (control, 'a'))
        else:  # ChromeDriver (Google Chrome).
            webdriver.ActionChains(self.driver).key_down(control).send_keys(
                'a').key_up(control).perform()

    def is_empty(self, element: str, data: str, value: str = '') -> bool:
        """Check if data is empty and input its value."""
        if data != value:  # Check if the data is not an empty string
            self.send_keys(element, data)  # or a default value, and send it.
            return False
        return True

    def window_handles(self, window_number: int) -> None:
        """Check for window handles and wait until a specific tab is opened."""
        window_number = {1: 0, 0: 1, 2: 2}[window_number] \
            if self.window == 1 else window_number
        WDW(self.driver, 10).until(lambda _: len(
            self.driver.window_handles) > window_number)
        self.driver.switch_to.window(  # Switch to the asked tab.
            self.driver.window_handles[window_number])


def download_browser(browser: int) -> str:
    """Try to download the webdriver using the Driver Manager."""
    try:
        # Set the name of the webdriver according to browser choice.
        webdriver = 'ChromeDriver' if browser == 0 else 'GeckoDriver'
        print(f'Downloading the {webdriver}.', end=' ')
        # Download the webdriver using the Driver Manager module.
        browser_path = GDM(log_level=0).install() if browser == 1 \
            else CDM(log_level=0).install()
        print(f'{GREEN}{webdriver} downloaded:{RESET} \n{browser_path}')
        return browser_path  # Return the path of the webdriver.
    except Exception:
        print(f'{RED}Browser download failed.{RESET}')
        # Set the browser path as "assets/" + browser + extension.
        browser_path = abspath('assets/' + ((
            'geckodriver.' + 'exe' if osname == 'nt' else '') if browser == 1
            else ('chromedriver.' + 'exe' if osname == 'nt' else '')))
        # Check if an executable is already in this path, else exit.
        if not exists(browser_path):
            exit('Download the webdriver and place it in the assets/ folder.')
        print(f'Webdriver path set as {browser_path}')
        return browser_path
