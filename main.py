"""
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn

Copyright © 2022 Maxime Dréan. All rights reserved.
Any distribution, modification or commercial use is strictly prohibited.

Version 1.5.10 - 2022, 26 February.

Transfer as many non-fungible tokens as you want to
the OpenSea marketplace. Easy, efficient and fast,
this tool lets you make your life as an Artist of
the digital world much smoother.
"""


# Colorama module: pip install colorama
from colorama import init, Fore, Style

# Selenium module imports: pip install selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as SC
from selenium.webdriver.firefox.service import Service as SG
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.common.exceptions import TimeoutException as TE
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Webdriver Manager module: pip install webdriver-manager
from webdriver_manager.chrome import ChromeDriverManager as CDM
from webdriver_manager.firefox import GeckoDriverManager as GDM

# Python default imports.
from datetime import datetime as dt
from glob import glob
import os


"""Colorama module constants."""
# This module may not work under MacOS.
init(convert=True, autoreset=True)  # Init the Colorama module.
red = Fore.RED  # Red color.
green = Fore.GREEN  # Green color.
yellow = Fore.YELLOW  # Yellow color.
reset = Style.RESET_ALL  # Reset color attribute.


class Reader:
    """Read files and extract NFTs data. Convert all types into a list."""

    def __init__(self, path: str) -> None:
        """Basically open a file and get all NFTs' data."""
        # Get file's extension to lowercase (MacOS support).
        self.path = path  # Instance the file path.
        # Get splitted file name (['text', '.txt']) and then remove the dot.
        self.extension = os.path.splitext(self.path)[1][1:].lower()
        # Check if the extension is supported by the Reader class.
        if self.extension in ('json', 'csv', 'xlsx'):
            # Eval function: self.extract_{FILE_EXTENSION}_file()
            eval(f'self.extract_{self.extension}_file()')
        else:  # Stop running the script.
            exit('The file extension is not supported.')

    def extract_json_file(self) -> None:
        """Transform JSON file format to a list of dictionaries."""
        from json import loads  # A Python default import.
        # Load and read the JSON file and extract "nft" part.
        self.file = loads(open(self.path, encoding='utf-8').read())['nft']
        self.lenght_file = len(self.file)  # Number of NFTs.

    def extract_csv_file(self) -> None:
        """Transform CSV file format to a list of dictionaries."""
        # Open file and splitlines (every "\n") and remove headers.
        # It gets a list of each rows.
        self.file = open(self.path, encoding='utf-8').read().splitlines()[1:]
        self.lenght_file = len(self.file)  # Number of NFTs.

    def extract_xlsx_file(self) -> None:
        """Transform XLSX file format to a dictionnary {key: {value, ...}}."""
        from pandas import read_excel  # Pandas module: pip install pandas
        self.file = read_excel(self.path)  # Read the Excel (XLSX) file.
        self.lenght_file = self.file.shape[0]  # Get number of rows.
        self.file = self.file.to_dict()  # Transform XLSX to a dictionnnary.


class Structure:
    """Structure JSON/CSV/XLSX data lists or dictionnaries."""

    def __init__(self, action: list) -> None:
        """Make a copy of the readed file and its extension."""
        self.file = reader.file.copy()  # File data copy.
        self.extension = reader.extension  # File extension copy.
        self.action = action  # 1, 2 or 1 and 2.
        self.structured = False  # If the file is well structured.
        self.upload_file, self.upload_and_sale_file, \
            self.sale_file = '', '', ''  # Data save files.
        self.upload_details = [  # All the upload details.
            'file_path', 'nft_name', 'link', 'description', 'collection',
            'properties', 'levels', 'stats', 'unlockable_content',
            'explicit_and_sensitive_content', 'supply', 'blockchain']
        self.sale_details = [  # All the sale details.
            'nft_url', 'supply', 'blockchain', 'type', 'price',
            'method', 'duration', 'specific_buyer', 'quantity']
        self.upload_and_sale_details = self.upload_details + \
            self.sale_details[3:]  # All the upload and sale details.

    def get_data(self, nft_number: int) -> None:
        """Get NFT's data."""
        self.nft_number = nft_number
        # Eval function: self.structure_{FILE_EXTENSION}()
        eval(f'self.structure_{self.extension}()')
        return self.structured

    def structure_json(self) -> None:
        """Transform JSON dictionnaries list to a whole list."""
        nft_data = self.file[self.nft_number]  # Get datas of index.
        # Get key's value from the NFT data.
        nft_data = [nft_data[data] for data in nft_data]
        # Take each element in the list and check it.
        self.structure_data([self.dict_to_list(
            element) for element in nft_data])  # Then structure data.

    def structure_csv(self) -> None:
        """Transform CSV file into a list."""
        # Note: each information is split every ";;", you can change the
        self.structure_data(self.change_type(  # characters to others.
            self.file[self.nft_number].split(';;')))

    def structure_xlsx(self) -> None:
        """Transform XLSX file into a list."""
        self.structure_data([
            element.replace('nan', '').strip() if isinstance(element, str) else
            element for element in self.change_type([self.file[element].get(
                self.nft_number) for element in self.file])])

    def dict_to_list(self, element: dict or str) -> list or str:
        """Transform a dictionnary into a list. - JSON file method."""
        if isinstance(element, list):  # If element is a list.
            return [[item.get(key) for key in item] if isinstance(
                item, dict) else item for item in element]
        return element  # Return the same element.

    def change_type(self, nft_data: list) -> list:
        """Change type of element with a literal eval."""
        from ast import literal_eval  # A Python default import.
        list_ = []  # List that contains NFT's data.
        for data in nft_data:  # Get each element of NFT's data.
            element = str(data).strip()  # Remove whitespaces.
            try:  # Change type of element (str to int/float/list/bool).
                # In case of element is an integer, float, list or boolean.
                list_.append(literal_eval(element))
            except Exception:  # SyntaxError or ValueError.
                # In case of element is a real string.
                list_.append(element)
        return list_

    def structure_data(self, nft_data: list) -> bool:
        """Structure each data of the NFT in a variable."""
        # self.nft_data_list = nft_data  # For development.
        index = 9 if 1 not in self.action else 0
        if (1 in self.action and 2 in self.action and len(nft_data) < 18) \
            or (1 in self.action and len(nft_data) < 12) or (2 in self.action
            and len(nft_data) < 9):  # File is badly structured.
            print(f'{red}Your file is poorly structured for this NFT.\nCheck '
                  f'that elements are present and in the right order.{reset}')
            return  # Do not try to structure the file.
        if 1 in self.action:  # Upload part.
            self.file_path: str or list = nft_data[0]
            self.nft_name: str = str(nft_data[1])  # Set string value to
            self.link: str = str(nft_data[2])  # real string to prevent
            self.description: str = str(nft_data[3])  # different types.
            self.collection: str = str(nft_data[4])
            self.properties: list = nft_data[5]  # [[type, name], ...].
            self.levels: list = nft_data[6]  # [[name, from, to], ...].
            self.stats: list = nft_data[7]  # [[name, from, to], ...].
            self.unlockable_content: list or bool = nft_data[8]  # [bool, str].
            self.explicit_and_sensitive_content: bool = nft_data[9]
            self.supply: int = nft_data[10]
            self.blockchain: str = str(nft_data[11]).capitalize()
        if 2 in self.action:  # Sale part.
            self.type: str = str(nft_data[12 - index]).title()
            self.price: float or int = nft_data[13 - index]
            self.method: list = nft_data[14 - index]  # [method, price].
            self.duration: list or str = nft_data[15 - index]
            self.specific_buyer: list or bool = nft_data[16 - index]
            self.quantity: int = nft_data[17 - index]
        if index != 0:  # Sale only!
            self.nft_url: str = str(nft_data[0])
            self.supply: int = nft_data[1]
            self.blockchain: str = str(nft_data[2]).capitalize()
        self.structured = True

    def is_empty(self, element: str, data: str, value: str = '') -> bool:
        """Check if data is empty and input its value."""
        if data != value:  # Check if the data is not an empty string
            web.send_keys(element, data)  # or a default value, and send it.
            return False
        return True

    def create_file(self, mode: str, content: str) -> None:
        """Create a file containing data for all NFTs."""
        from uuid import uuid4  # A Python default import.
        exec(f'self.{mode}_file = "data/{mode}_{str(uuid4())[:8]}.csv"')
        with open(eval(f'self.{mode}_file'), 'a+', encoding='utf-8') as file:
            file.write(content[:-3] if content.endswith(';; ') else content)

    def save(self, mode: str, details: list) -> None:
        """Save in the file all details of the NFT."""
        if not os.path.isfile(os.path.abspath(eval(f'self.{mode}_file'))):
            self.create_file(  # Create the upload file.
                mode, ''.join(f'{detail};; ' for detail in details))
        with open(eval(f'self.{mode}_file'), 'a+', encoding='utf-8') as file:
            file.write('\n' + ''.join(  # Create the upload file.
                f'{eval(f"self.{detail}", {"self": self})};; '
                .replace("\\", "/") for detail in details)[:-3])
        print(f'{green}Data saved in {eval(f"self.{mode}_file")}')

    def save_upload(self) -> None:
        """Save all the details of the NFT for a new upload."""
        self.save('upload', self.upload_details)

    def save_upload_and_sale(self) -> None:
        """Save all the details of the NFT for a new upload and sale."""
        self.save('upload_and_sale', self.upload_and_sale_details)

    def save_sale(self, future: bool = False) -> None:
        """Save all the details of the NFT for a (failed) sale."""
        [exec(f'self.{detail} = ""' if future else '', {'self': self})
         for detail in self.sale_details[3:]]  # Set an empty value to the
        self.save('sale', self.sale_details)  # missing sale details.


class Webdriver:
    """Webdriver class and methods to prevent exceptions."""

    def __init__(self, browser: int, browser_path: str) -> None:
        """Contains the file paths of the webdriver and the extension."""
        self.metamask_extension_path = os.path.abspath(  # Extension path.
            'assets/MetaMask.crx' if browser == 0 else 'assets/MetaMask.xpi')
        self.browser_path = browser_path  # Get the browser path.
        # Start a Chrome (not headless) or Firefox (headless mode) webdriver.
        self.driver = self.chrome() if browser == 0 else self.firefox()
        self.window = browser  # Window handle value.

    def chrome(self) -> webdriver:
        """Start a Chrome webdriver and return its state."""
        options = webdriver.ChromeOptions()  # Configure options for Chrome.
        options.add_extension(self.metamask_extension_path)  # Add extension.
        options.add_argument('log-level=3')  # No logs is printed.
        options.add_argument('--mute-audio')  # Audio is muted.
        options.add_argument('--lang=en-US')  # Set webdriver language
        options.add_experimental_option(  # to English. - 2 methods.
            'prefs', {'intl.accept_languages': 'en,en_US'})
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(service=SC(  # DeprecationWarning using
            self.browser_path), options=options)  # executable_path.
        driver.maximize_window()  # Maximize window to reach all elements.
        return driver

    def firefox(self) -> webdriver:
        """Start a Firefox webdriver and return its state."""
        options = webdriver.FirefoxOptions()  # Configure options for Firefox.
        options.add_argument('--headless')  # Headless mode.
        options.add_argument('--log-level=3')  # No logs is printed.
        options.add_argument('--mute-audio')  # Audio is muted.
        options.set_preference('intl.accept_languages', 'en,en-US')
        driver = webdriver.Firefox(service=SG(  # DeprecationWarning using
            self.browser_path), options=options)  # executable_path.
        driver.install_addon(self.metamask_extension_path)  # Add extension.
        driver.maximize_window()  # Maximize window to reach all elements.
        return driver

    def quit(self) -> None:
        """Stop the webdriver."""
        try:  # Try to close the webdriver.
            self.driver.quit()
        except Exception:  # The webdriver is closed
            pass  # or no webdriver is started.

    def clickable(self, element: str) -> None:
        """Click on an element if it's clickable using Selenium."""
        try:
            WDW(self.driver, 5).until(EC.element_to_be_clickable(
                (By.XPATH, element))).click()
        except Exception:  # Some buttons need to be visible to be clickable,
            self.driver.execute_script(  # so JavaScript can bypass this.
                'arguments[0].click();', self.visible(element))

    def visible(self, element: str):
        """Check if an element is visible using Selenium."""
        return WDW(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, element)))

    def send_keys(self, element: str, keys: str) -> None:
        """Send keys to an element if it's visible using Selenium."""
        try:
            self.visible(element).send_keys(keys)
        except Exception:  # Some elements are not visible but are present.
            WDW(self.driver, 5).until(EC.presence_of_element_located(
                (By.XPATH, element))).send_keys(keys)

    def send_date(self, element: str, keys: str) -> None:
        """Send a date (DD-MM-YYYY HH:MM) to a date input by clicking on it."""
        if self.window == 1:  # GeckoDriver (Mozilla Firefox).
            self.send_keys(element, '-'.join(
                reversed(keys.split('-'))) if '-' in keys else keys)
            return  # Quit the method.
        keys = keys.split('-') if '-' in keys else [keys]
        keys = [keys[1], keys[0], keys[2]] if len(keys) > 1 else keys
        for part in range(len(keys) - 1 if keys[len(keys) - 1] == str(
                          dt.now().year) else len(keys)):  # Number of clicks.
            self.clickable(element)  # Click first on the element.
            self.send_keys(element, keys[part])  # Then send it the date.

    def clear_text(self, element) -> None:
        """Clear text from an input."""
        self.clickable(element)  # Click on the element then clear its text.
        # Note: change with 'darwin' if it's not working on MacOS.
        control = Keys.COMMAND if os.name == 'posix' else Keys.CONTROL
        if self.window == 0:  # ChromeDriver (Google Chrome).
            webdriver.ActionChains(self.driver).key_down(control).send_keys(
                'a').key_up(control).perform()
        elif self.window == 1:  # GeckoDriver (Mozilla Firefox).
            self.send_keys(element, (control, 'a'))

    def window_handles(self, window_number: int) -> None:
        """Check for window handles and wait until a specific tab is opened."""
        window_number = {1: 0, 0: 1, 2: 2}[window_number] \
            if self.window == 1 else window_number
        WDW(self.driver, 10).until(lambda _: len(
            self.driver.window_handles) > window_number)
        self.driver.switch_to.window(  # Switch to the asked tab.
            self.driver.window_handles[window_number])


class Wallets:
    """Allows connection to OpenSea with different wallets."""

    def __init__(self, wallet: int, password: int,
                 recovery_phrase: str) -> None:
        """Get the wallet and connect to the extension/etc."""
        self.recovery_phrase = recovery_phrase  # Get the phrase.
        self.password = password  # Get the new/same password.
        self.wallet = wallet  # Wallet user choice.
        self.wallet_function = wallet.lower().replace(' ', '_')
        self.fails = 0  # Counter of fails during wallet connection.
        self.success = False

    def login(self) -> bool:
        """Connect to OpenSea using a specific wallet."""
        eval(f'self.{self.wallet_function}_login()')
        return self.success

    def sign(self) -> None:
        """Use the method of the wallet to sign the login."""
        eval(f'self.{self.wallet_function}_sign()')

    def contract(self) -> None:
        """Use the method of the wallet to sign the contract."""
        eval(f'self.{self.wallet_function}_contract()')

    def close(self) -> None:
        """Close any popup or page opened by an extension."""
        eval(f'self.{self.wallet_function}_close()')

    def metamask_login(self) -> bool or None:
        """Login to the MetaMask extension."""
        try:  # Try to login to the MetaMask extension.
            print('Login to MetaMask.', end=' ')
            web.window_handles(0)  # Switch to the MetaMask extension tab.
            web.driver.refresh()  # Reload the page to prevent a blank page.
            # Click on the "Start" button.
            web.clickable('//*[@class="welcome-page"]/button')
            # Click on the "Import wallet" button.
            web.clickable('//*[contains(@class, "btn-primary")][position()=1]')
            # Click on the "I agree" button.
            web.clickable('//footer/button[2]')
            # Input the recovery phrase.
            web.send_keys('//input[position()=1]', self.recovery_phrase)
            # Input a new password or the same password of your account.
            web.send_keys('//*[@id="password"]', self.password)
            web.send_keys('//*[@id="confirm-password"]', self.password)
            # Click on the "I have read and agree to the..." checkbox.
            web.clickable('(//*[@role="checkbox"])[2]')
            # Click on the "Import" button.
            web.clickable('//*[contains(@class, "btn-primary")][position()=1]')
            # Wait until the login worked and click on the "All done" button".
            web.visible('//*[contains(@class, "emoji")][position()=1]')
            web.clickable('//*[contains(@class, "btn-primary")][position()=1]')
            print(f'{green}Logged to MetaMask.{reset}')
            self.success = True
        except Exception:  # Failed - a web element is not accessible.
            self.fails += 1  # Increment the counter.
            if self.fails < 2:  # Retry login to the wallet.
                print(f'{red}Login to MetaMask failed. Retrying.{reset}')
                self.metamask_login()
            else:  # Too many fails.
                self.fails = 0  # Reset the counter.
                print(f'{red}Login to MetaMask failed. Restarting.{reset}')
                web.quit()  # Stop the webdriver.

    def metamask_sign(self) -> None:
        web.window_handles(2)  # Switch to the MetaMask pop up tab.
        # Click on the "Next" button.
        web.clickable('//*[contains(@class, "btn-primary")]')
        # Click on the "Connect" button.
        web.clickable('//*[contains(@class, "btn-primary")]')
        web.window_handles(2)  # Switch to the MetaMask pop up tab.
        self.metamask_contract()  # Sign the contract.

    def metamask_contract(self) -> None:
        """Sign a MetaMask contract to login to OpenSea."""
        web.window_handles(2)  # Switch to the MetaMask pop up tab.
        # Click on the "Sign" button - Make a contract link.
        web.clickable('(//*[contains(@class, "signature") and conta'
                      'ins(@class, "footer")])[position()=1]/button[2]')
        try:  # Wait until the MetaMask pop up is closed.
            WDW(web.driver, 10).until(EC.number_of_windows_to_be(2))
        except TE:
            self.metamask_contract()  # Sign the contract a second time.
        web.window_handles(1)  # Switch back to the OpenSea tab.

    def metamask_close(self) -> None:
        """Close the MetaMask popup."""
        if len(web.driver.window_handles) > 2:
            try:
                web.window_handles(2)  # Switch to the MetaMask popup.
                web.driver.close()  # Close the popup extension.
                web.window_handles(1)  # Switch back to OpenSea.
            except Exception:
                pass  # Ignore the exception.


class OpenSea:
    """Main class: OpenSea automatic uploader."""

    def __init__(self) -> None:
        """Get the password and the recovery_phrase from the text file."""
        self.login_url = 'https://opensea.io/login?referrer=%2Fasset%2Fcreate'
        self.create_url = 'https://opensea.io/asset/create'  # OpenSea URLs.
        self.fails = 0  # Counter of fails during wallet connection.
        self.retries_upload = 0  # Counter of upload retries.
        self.retries_sale = 0  # Counter of sale retries.
        self.success = False  # Boolean returned after login.

    def login(self) -> bool or None:
        """Login to OpenSea using MetaMask."""
        try:  # Try to login to the OpenSea using MetaMask.
            print('Login to OpenSea.', end=' ')
            web.window_handles(1)  # Switch to the main (data:,) tab.
            web.driver.get(self.login_url)  # Go to the OpenSea login URL.
            # Click on the "Show more options" button.
            web.clickable('//button[contains(@class, "show-more")]')
            # Click on the wallet button in list of wallets.
            web.clickable(f'//*[contains(text(), "{wallet.wallet}")]/../..')
            wallet.sign()  # Sign the login on OpenSea.
            # Check if the login worked.
            WDW(web.driver, 15).until(EC.url_to_be(self.create_url))
            print(f'{green}Logged to OpenSea.{reset}')
            self.success = True
        except Exception:  # The contract failed.
            try:
                web.window_handles(1)  # Switch back to the OpenSea tab.
                wallet.contract()  # Sign the contract.
                # Check if the login worked.
                WDW(web.driver, 10).until(EC.url_to_be(self.create_url))
                print(f'{green}Logged to OpenSea.{reset}')
                self.success = True
            except Exception:
                self.fails += 1  # Increment the counter.
                if self.fails < 2:  # Retry login to the wallet.
                    print(f'{red}Login to OpenSea failed. Retrying.{reset}')
                    web.driver.refresh()  # Reload the page (login failed?).
                    self.login()  # Retry everything.
                else:  # Too many fails.
                    self.fails = 0  # Reset the counter.
                    print(f'{red}Login to OpenSea failed. Restarting.{reset}')
                    web.quit()  # Stop the webdriver.
        return self.success

    def upload(self) -> bool:
        """Upload multiple NFTs automatically on OpenSea."""
        print(f'Uploading NFT.', end=' ')
        try:  # Go to the OpenSea create URL and input all datas of the NFT.
            web.driver.get(self.create_url + '?enable_supply=true')
            if isinstance(structure.file_path, list):
                if len(structure.file_path) == 2:
                    file_path = os.path.abspath(structure.file_path[0])
                    preview = os.path.abspath(structure.file_path[1])
            else:  # No preview file.
                file_path = os.path.abspath(structure.file_path)
            if not os.path.exists(file_path):  # Upload the NFT file.
                raise TE('File doesn\'t exist or path is incorrect.')
            if os.path.getsize(file_path) / (1024 ** 2) > 100:
                raise TE('File size must be less than 100 MegaBytes.')
            if os.path.splitext(file_path)[1][1:].lower() not in \
                ('jpg', 'jpeg', 'png', 'gif', 'svg', 'mp4',  # Check the file
                 'webm', 'mp3', 'wav', 'ogg', 'glb', 'gltf'):  # extensions.
                raise TE('The file extension is not supported on OpenSea.')
            structure.is_empty('//*[@id="media"]', file_path)
            if os.path.splitext(file_path)[1][1:].lower() in \
                    ('mp4', 'webm', 'mp3', 'wav', 'ogg', 'glb', 'gltf'):
                if not os.path.exists(preview):  # Upload the NFT file.
                    raise TE('File doesn\'t exist or path is incorrect.')
                if os.path.getsize(preview) / (1024 ** 2) > 100:
                    raise TE('File size must be less than 100 MegaBytes.')
                structure.is_empty('//input[@name="preview"]', preview)
            # Input NFT name.
            if structure.is_empty('//*[@id="name"]', structure.nft_name):
                raise TE('The NFT name is missing.')
            # Input external link.
            structure.is_empty('//*[@id="external_link"]', structure.link)
            # Input description.
            structure.is_empty('//*[@id="description"]', structure.description)
            if not structure.is_empty(  # Input collection and select it.
                    '//*[@id="collection"]', structure.collection):
                try:  # Try to click on the collection button.
                    collection = ('//span[contains(text(), "'
                                  f'{structure.collection}")]/../..')
                    web.visible(collection)  # Check that the collection span
                    web.clickable(collection)  # is visible and click on it.
                except Exception:  # If collection doesn't exist.
                    raise TE('Collection doesn\'t exist or can\'t be found.')
            datas = [structure.properties, structure.levels, structure.stats]
            for index in range(len(datas)):  # Add properties, levels & stats.
                if not len(datas[index]) > 0:  # Check if data is not empty.
                    continue  # Pass this data because it's empty or null.
                # Change element from a list of strings to a list of lists.
                if not isinstance(datas[index][0], list):
                    datas[index] = [datas[index]]  # Target maybe useless.
                web.clickable(  # Click on "+" button to open the pop up.
                    f'//form/section/div[{index + 1}]/div/div[2]/button')
                number_ = 0  # Counter of properties/levels/stats to input.
                for data in datas[index]:
                    if number_ > 0:  # If there are more than 1 element.
                        # Click on "Add more" button.
                        web.clickable('//div[@role="dialog"]/section/button')
                    number_ += 1  # Increase number to add more element.
                    web.send_keys(  # Input values in the inputs.
                        f'/html/body/div[{index + 2}]/div/div/div/section/tabl'
                        f'e/tbody/tr[{number_}]/td[1]/div/div/input', data[0])
                    for rank in [3, 2]:  # Input third and second values.
                        if len(data) == 3 or rank == 2:  # 1 or 2 loops.
                            actual_element = f'/html/body/div[{index + 2}]' + \
                                '/div/div/div/section/table/tbody/' + \
                                f'tr[{number_}]/td[{rank}]/div/div/input'
                            web.clear_text(actual_element)  # Default value.
                            web.send_keys(actual_element, data[rank - 1])
                web.clickable('//footer/button')  # Click on the "Save" button.
            # Click on the "Unlockable Content" switch if it's true.
            if isinstance(structure.unlockable_content, list):  # If not False.
                if len(structure.unlockable_content) > 0:  # Not an empty list.
                    if isinstance(structure.unlockable_content[0], bool):
                        if structure.unlockable_content[0]:  # If True.
                            web.send_keys('//*[@id="unlockable-content-toggle'
                                          '"]', Keys.ENTER)  # Toggle button.
                            web.send_keys(  # Input the unlockable content.
                                '//div[contains(@class, "unlockable")]/'
                                'textarea', structure.unlockable_content[1])
            # Click on the "Explicit & Sensitive Content" switch if it's true.
            if structure.explicit_and_sensitive_content != '':  # Not empty.
                if isinstance(structure.explicit_and_sensitive_content, bool):
                    if structure.explicit_and_sensitive_content:  # True.
                        web.send_keys('//*[@id="explicit-content-toggle"]',
                                      Keys.ENTER)  # Toggle button.
            # Set number of supplies if it's not an empty string.
            if structure.supply != '' and 'supply=' in web.driver.current_url:
                if isinstance(structure.supply, int):  # Integer.
                    if structure.supply > 1:  # Set supplies deleting default
                        web.send_keys('//*[@id="supply"]',  # supply (= 1).
                                      f'{Keys.BACKSPACE}{structure.supply}')
            else:  # This is important for the sale part.
                structure.supply = 1
            # Set Blockchain if it's different from "Ethereum".
            if structure.blockchain != '':  # If it's not an empty string.
                if web.visible('//*[@id="chain"]').get_attribute('value') \
                        != structure.blockchain:  # Compare to the span text.
                    try:  # Try to select the Blockchain.
                        web.clickable('//*[@id="chain"]/..')  # Open the sheet.
                        web.clickable('//span[contains(text(), '
                                      f'"{structure.blockchain}")]/../..')
                    except Exception:  # Blockchain is unknown.
                        raise TE('Blockchain is unknown or badly written.')
            else:  # This is important for the sale part.
                structure.blockchain = 'Ethereum'
            web.clickable('(//div[contains(@class, "submit")])'  # Click on the
                          '[position()=1]/div/span/button')  # "Create" button.
            WDW(web.driver, 30).until(lambda _: web.driver.current_url !=
                                      self.create_url + '?enable_supply=true')
            print(f'{green}NFT uploaded.{reset}')
            if 2 not in structure.action:  # Save the data for future upload.
                structure.nft_url = web.driver.current_url  # Edit the NFT URL.
                structure.save_sale(True)  # Save for a future listing.
            return True  # If it perfectly worked.
        except Exception as error:  # Any other error.
            print(f'{red}Upload failed.{reset}',
                  error if not 'Stacktrace' in str(error) else "\n", end='')
            wallet.close()  # Close the MetaMask popup.
            self.retries_upload += 1  # Increment the counter.
            if self.retries_upload > 0:  # Too much fails.
                structure.save_upload() if 2 not in structure.action else \
                    structure.save_upload_and_sale()  # Save the details.
                return False  # It failed.
            self.upload()  # Try to re-upload the NFT.

    def sale(self, date: str = '%d-%m-%Y %H:%M') -> None:
        """Set a price for the NFT and sell it."""
        print(f'Sale of the NFT.', end=' ')
        try:  # Try to sell the NFT with different types and methods.
            if 2 in structure.action and 1 not in structure.action:
                web.driver.get(structure.nft_url + '/sell')  # NFT sale page.
            else:  # The NFT has just been uploaded.
                structure.nft_url = web.driver.current_url
                web.driver.get(structure.nft_url + '/sell')  # Sale page.
            if not isinstance(structure.supply, int):
                raise TE('The supply number must be an integer.')
            elif structure.supply == 1 and structure.blockchain == 'Ethereum':
                if not isinstance(structure.price, int) and not \
                        isinstance(structure.price, float):
                    raise TE('The price must be an integer or a float.')
                if 'Timed' in str(structure.type):  # Timed Auction.
                    # Click on the "Timed Auction" button.
                    web.clickable('//i[@value="timelapse"]/../..')
                    if isinstance(structure.method, list):  # If it's a list.
                        if len(structure.method) == 2:  # [method, price]
                            if not isinstance(structure.method[1], int) and \
                                    not isinstance(structure.method[1], float):
                                raise TE('Prices must be integer or float.')
                            if 'declining' in str(structure.method[0]):
                                web.clickable(  # Click on the method button.
                                    '//*[@id="main"]/div/div/div[3]/div/div[2]'
                                    '/div/div[1]/form/div[2]/div/div[2]')
                                # Click on the "Sell with declining price"
                                web.clickable('//*[@role="tooltip"]'  # button.
                                              '/div/div/ul/li/button')
                                if structure.method[1] < structure.price:
                                    web.send_keys(  # Input the ending price.
                                        '//*[@name="endingPrice"]', format(
                                            structure.method[1], '.8f'))
                                else:  # Ending price is higher than the price.
                                    raise TE('The ending price must be higher'
                                             ' than the starting price.')
                            elif 'highest' in str(structure.method[0]):
                                if structure.method[1] > 0:  # Reserve price.
                                    if structure.method[1] <= 1 or structure \
                                            .method[1] < structure.price:
                                        raise TE('Reserve price must be higher'
                                                 ' than 1 WETH and the price.')
                                    # Click on the "More option" button.
                                    web.clickable('//button[contains(@class, '
                                                  '"more-options")]')
                                    # Click on the "Include reserve price"
                                    web.send_keys(  # toggle switch button.
                                        '//*[@role="switch"]', Keys.ENTER)
                                    web.send_keys(  # Input the reserve price.
                                        '//*[@name="reservePrice"]',
                                        format(structure.method[1], '.8f'))
                            else:  # Not a Declining price or a Highest bidder.
                                raise TE('Unknown method for Timed Auction.')
            elif structure.supply > 1:  # Set a quantity of supply.
                if isinstance(structure.quantity, int):  # Quantity is int.
                    if structure.quantity <= structure.supply:
                        web.send_keys('//*[@id="quantity"]',  # Supply to sell.
                                      f'{Keys.BACKSPACE}{structure.quantity}')
                    else:  # Quantity number is higher that supply number.
                        raise TE('Quantity must be less or equal to supplies.')
            elif structure.blockchain not in ('Ethereum', 'Polygon'):
                raise TE('Blockchain is unknown or badly written.')
            if 'Timed' not in str(structure.type):  # Set a specific buyer.
                if isinstance(structure.specific_buyer, list):
                    if len(structure.specific_buyer) == 2:
                        if isinstance(structure.specific_buyer[0], bool):
                            if structure.specific_buyer[0]:
                                # Click on the "More option" button.
                                web.clickable('//button[contains(@cla'
                                              'ss, "more-options")]')
                                # Click on "Reserve for specific buyer".
                                web.send_keys('(//*[@role="switch"])[last()]',
                                              Keys.ENTER)
                                web.send_keys(  # Input a specific buyer.
                                    '//*[@id="reservedBuyerAddressOrEns'
                                    'Name"]', structure.specific_buyer[1])
            web.send_keys('//*[@name="price"]', format(structure.price, '.8f'))
            if isinstance(structure.duration, str):  # Transform to a list.
                structure.duration = [structure.duration]
            if isinstance(structure.duration, list):  # List of 1 or 2 values.
                if len(structure.duration) == 2:  # From {date} to {date}.
                    from datetime import datetime as dt  # Default import.
                    # Check if duration is less than 6 months.
                    if (dt.strptime(structure.duration[1], date) -
                            dt.strptime(structure.duration[0], date
                                        )).total_seconds() / 60 > 262146:
                        raise TE('Duration must be less than 6 months.')
                    # Check if starting date has passed.
                    if dt.strptime(dt.strftime(dt.now(), date), date) \
                            > dt.strptime(structure.duration[0], date):
                        raise TE('Starting date has passed.')
                    # Split the date and the time.
                    start_date, start_time = structure.duration[0].split(' ')
                    end_date, end_time = structure.duration[1].split(' ')
                    web.clickable('//*[@id="duration"]')  # Date button.
                    web.visible(  # Scroll to the pop up frame of the date.
                        '//*[@role="dialog"]').location_once_scrolled_into_view
                    web.send_date('//*[@role="dialog"]'  # Ending date.
                                  '/div[2]/div[2]/div/div[2]/input', end_date)
                    web.send_date('//*[@role="dialog"]/'  # Starting date.
                                  'div[2]/div[1]/div/div[2]/input', start_date)
                    web.send_date('//*[@id="end-time"]', end_time)  # End date.
                    web.send_date(  # Starting date + close tab for Chrome.
                        '//*[@id="start-time"]', start_time if web.window == 1
                        else f'{start_time}{Keys.ENTER}')
                    web.send_keys('//html', Keys.ENTER)  # Close the frame.
                elif len(structure.duration) == 1:  # In {n} days/week/months.
                    if structure.duration[0] == '':  # Duration not specified.
                        raise TE('Duration must be specified.')
                    if web.visible('//*[@id="duration"]/div[2]').text \
                            != structure.duration[0]:  # Not default.
                        web.clickable('//*[@id="duration"]')  # Date button.
                        web.clickable('//*[@role="dialog"]'  # Duration Range
                                      '/div[1]/div/div[2]/input')  # sheet.
                        web.clickable('//span[contains(text(), '   # Date span.
                                      f'"{structure.duration[0]}")]/../..')
                        web.send_keys('//*[@role="dialog"]', Keys.ENTER)
            try:  # Click on the "Complete listing" (submit) button.
                web.clickable('//button[@type="submit"]')
            except Exception:  # An unknown error has occured.
                raise TE('The submit button cannot be clicked.')
            try:  # Polygon blockchain requires a click on a button.
                if structure.blockchain == 'Polygon':
                    web.clickable(  # Click on the "Sign" button.
                        '//div[@class="ActionPanel--content"]/button')  
                wallet.contract()  # Sign the contract.
            except Exception:  # An error occured while listing the NFT.
                raise TE('Cannot sign the MetaMask contract.')
            try:  # Check if the NFT is listed.
                web.window_handles(1)  # Switch back to the OpenSea tab.
                web.visible('//header/h4[contains(text(), "listed")]')
            except Exception:  # Sometimes popup is do not detected.
                try:  # Reload and check if listed.
                    web.window_handles(1)  # Switch back to the OpenSea tab.
                    web.driver.get(structure.nft_url)
                    if 'listing' not in web.visible(  # "Cancel listings".
                        '//button[contains(@class, "second-button")]').text:
                        raise Exception()  # Probably not listed.
                except Exception:  # Not able to tell if the NFT is listed.
                    raise TE('Something went wrong.')
            print(f'{green}NFT put up for sale.{reset}')
        except Exception as error:  # Any other error.
            print(f'{red}NFT sale cancelled.{reset}',
                  error if not 'Stacktrace' in str(error) else "\n", end='')
            wallet.close()  # Close the MetaMask popup.
            self.retries_sale += 1  # Increment the counter.
            if self.retries_sale > 1:  # Too much fails.
                structure.save_sale()  # Save the NFT details for a sale.
                return False  # It failed.
            web.driver.get(structure.nft_url)
            self.sale()  # Try to re-upload the NFT.


def choose_wallet() -> int:
    """Ask the user for a wallet to connect to OpenSea."""
    wallets = ['MetaMask']  # New wallets will be added.
    while True:
        print(f'{yellow}\nChoose a wallet:')
        [print(f'{wallets.index(wallet) + 1} - {wallet}'
               ) for wallet in wallets]  # Print wallets.
        answer = input('Wallet: ')  # Get the user answer.
        if not answer.isdigit():  # Check if answer is a number.
            print(f'{red}Answer must be an integer.')
        elif int(answer) > len(wallets) or int(answer) <= 0:
            print(f'{red}Wallet doesn\'t exist.')
        else:  # Return the name of wallet with a function format.
            return wallets[int(answer) - 1]


def read_file(file_: str, question: str) -> str:
    """Read file or ask for data to write in text file."""
    if not os.path.isfile(f'assets/{file_}.txt'):
        open(f'assets/{file_}.txt', 'a')  # Create a file if it doesn't exist.
    with open(f'assets/{file_}.txt', 'r+', encoding='utf-8') as file:
        text = file.read()  # Read the file.
        if text == '':  # If the file is empty.
            text = input(question)  # Ask the question.
            if input(f'Do you want to save your {file_} in '
                     'a text file? (y/n) ').lower() != 'y':
                print(f'{yellow}Not saved.{reset}')
            else:
                file.write(text)  # Write the text in file.
                print(f'{green}Saved.{reset}')
        return text


def perform_action() -> list:
    """Suggest multiple actions to the user."""
    while True:
        [print(string) for string in [
            f'{yellow}\nChoose an action to perform:{reset}',
            '1 - Upload and sell NFTs (18 details/NFT).',
            '2 - Upload NFTs (12 details/NFT).', '3 - Sell '
            'NFTs (9 details/NFT including 3 autogenerated).']]
        number = input('Action number: ')
        if number.isdigit():  # Check if answer is a number.
            if int(number) > 0:
                return [[1, 2], [1], [2]][int(number) - 1]
        print(f'{red}Answer must be a strictly positive integer.{reset}')


def choose_browser() -> int:
    """Ask the user for a browser."""
    browsers = ['ChromeDriver (Google Chrome) - No headless mode.\n    '
                'Must used in foreground, you see what\'s happening.',
                'GeckoDriver (Mozilla Firefox) - Headless mode.\n    '
                'Can be used in background while doing something else.']
    while True:
        print(f'{yellow}\nChoose a browser:')
        [print(f'{browsers.index(browser) + 1} - {browser}'
               ) for browser in browsers]  # Print browsers.
        answer = input('Browser: ')  # Get the user answer.
        if not answer.isdigit():  # Check if answer is a number.
            print(f'{red}Answer must be an integer.')
        elif int(answer) > len(browsers) or int(answer) <= 0:
            print(f'{red}Browser doesn\'t exist.')
        else:  # Return the index of browser.
            return int(answer) - 1


def data_file() -> str:
    """Read the data folder and extract JSON, CSV and XLSX files."""
    while True:
        file_number, files_list = 0, []
        print(f'{yellow}\nChoose your file:{reset}\n0 - Browse a file on PC.')
        for files in [glob(f'data/{extension}')  # Files of the data folder.
                      for extension in ['*.json', '*.csv', '*.xlsx']]:
            for file in files:
                file_number += 1
                files_list.append(file)
                print(f'{file_number} - {os.path.abspath(file)}')
        answer = input('File number: ')
        if not answer.isdigit():  # Check if answer is a number.
            print(f'{red}Answer must be an integer.{reset}')
        elif int(answer) == 0:  # Browse a file on PC.
            print(f'{yellow}Browsing on your computer...{reset}')
            from tkinter import Tk  # Tkinter module: pip install tk
            from tkinter.filedialog import askopenfilename
            Tk().withdraw()  # Hide Tkinter tab.
            return askopenfilename(filetypes=[('', '.json .csv .xlsx')])
        elif int(answer) <= len(files_list):
            return files_list[int(answer) - 1]  # Return path of file.


def worker_sale() -> None:
    """Sale the NFTs after uploading or not."""
    if not (isinstance(structure.price, int) or
            isinstance(structure.price, float)):
        print(f'{yellow}Sale aborted: price must be a number.{reset}')
    elif (structure.price <= 0 and 'Poly' in structure.blockchain) \
            or (structure.price < 0 and 'Eth' in structure.blockchain):
        print(f'{yellow}Sale aborted: price not defined or null.{reset}')
    else:  # If price has been defined.
        opensea.sale()  # Sell NFT.


def cls() -> None:
    """Clear console function."""
    # Clear console for Windows using 'cls' and Linux & Mac using 'clear'.
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':

    cls()  # Clear console.
    print(f'{green}Created by Maxime Dréan.'
          '\nGithub: https://github.com/maximedrn'
          '\nTelegram: https://t.me/maximedrn'
          '\n\nCopyright © 2022 Maxime Dréan. All rights reserved.'
          '\nAny distribution, modification or commercial use is strictly'
          ' prohibited.'
          f'\n\nVersion 1.5.10 - 2022, 26 February.\n{reset}'
          '\nIf you face any problem, please open an issue.')

    input('\nPRESS [ENTER] TO CONTINUE. ')
    cls()  # Clear console.

    print(f'{green}Created by Maxime Dréan.'
          '\n\nCopyright © 2022 Maxime Dréan. All rights reserved.'
          '\nAny distribution, modification or commercial use is strictly'
          f' prohibited.{reset}')

    wallet = Wallets(choose_wallet(), read_file(  # Send credentials.
        'password', '\nWhat is your MetaMask password? '), read_file(
        'recovery_phrase', '\nWhat is your MetaMask recovery phrase? '))
    action = perform_action()  # What the user wants to do.
    browser = choose_browser()  # Get the browser.
    reader = Reader(data_file())  # Ask for a file and read it.
    structure = Structure(action)  # Structure the file.
    cls()  # Clear console.

    download_failed = 0
    while True:
        try:
            webdriver_ = 'ChromeDriver' if browser == 0 else 'GeckoDriver'
            print(f'Downloading the {webdriver_}.', end=' ')
            browser_path = CDM(log_level=0).install() if browser == 0 else \
                GDM(log_level=0).install()  # Download the webdriver.
            print(f'{green}{webdriver_} downloaded:{reset} \n{browser_path}')
            break  # Stop the while loop.
        except Exception:
            print(f'{red}Browser download failed.{reset}', end=' ')
            download_failed += 1  # Increment the fails counter.
            if download_failed > 4:
                browser_path = input(f'\nDownload and extract the {webdriver_}.'
                                     '\nThen paste its path here: ')
                break  # Stop the while loop.
            print(f'{red}Retrying.{reset}')
            pass  # Ignore the exception.

    if 1 in action:  # Upload the NFT and sale it (if user chooses it).
        for nft_number in range(reader.lenght_file):
            while True:  # While loop to retry to connect for the NFT.
                print(f'\nNFT n°{nft_number + 1}/{reader.lenght_file}:')
                try:  # To prevent Selenium HTTPConnectionPool.
                    if not structure.get_data(nft_number): # Structure data.
                        break  # Break the while loop.
                    web = Webdriver(browser, browser_path)  # Start webdriver.
                    opensea = OpenSea()  # Init the OpenSea class.
                    if wallet.login() is False:  # Connect to MetaMask.
                        continue  # Restart the while loop.
                    if opensea.login() is False:  # Connect to OpenSea.
                        continue  # Restart the while loop.
                    if opensea.upload() and 2 in action:
                        worker_sale()  # Sale of the NFTs.
                    web.quit()  # Stop the webdriver.
                    break  # Stop the while loop and continue the for loop.
                except Exception as error:  # Selenium HTTPConnectionPool.
                    print(f'{red}Launch error.{reset} {error}')
                    try:
                        web.quit()  # Close the webdriver.
                    except Exception:
                        pass  # No webdriver opened.

    elif 2 in action and 1 not in action:  # "not 1" to be sure - Sale only.
        web = Webdriver(browser, browser_path)  # Start a new webdriver.
        opensea = OpenSea()  # Init the OpenSea class.
        print('')  # Separate outputs.
        wallet.login()  # Connect to MetaMask.
        opensea.login()  # Connect to OpenSea.
        for nft_number in range(reader.lenght_file):
            print(f'\nNFT n°{nft_number + 1}/{reader.lenght_file}:')
            if structure.get_data(nft_number):  # Structure the data.
                worker_sale()  # Sale of the NFTs.
        web.quit()  # Stop the webdriver.

    print(f'\n{green}All done!{reset}\nIn order to support me,'
          ' you can make donations at this address:\n'
          '0xDD135d5be0a23f6daAAE7D2d0580828c9e09402E (Ethereum).')
