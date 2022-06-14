#!/usr/bin/python
# app/services/processes/upload.py


"""
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn

Copyright © 2022 Maxime Dréan. All rights reserved.
Any distribution, modification or commercial use is strictly prohibited.
"""


# Selenium module imports: pip install selenium
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.common.exceptions import TimeoutException as TE
from selenium.webdriver.common.keys import Keys

# Python internal imports.
from ...utils.colors import GREEN, RED, YELLOW, RESET
from ...utils.const import UPLOAD_FAILS

# Python default imports.
from os.path import abspath, splitext, exists, getsize


class Upload:
    """Transfer the NFTs to OpenSea."""

    def __init__(self, solver: int, key: str, structure: object,
                 save: object, web: object, wallet: object,
                 recaptcha: object) -> None:
        """Get the password and the recovery_phrase from the text file."""
        self.create_url = 'https://opensea.io/{}asset{}/create'
        self.fails = 0  # Counter of upload retries.
        self.solver = solver  # Integer of the specific solver.
        self.key = key  # API key for paid services.
        # Get the instance of the needed classes.
        self.structure = structure  # From the Structure class.
        self.save = save  # From the Save class.
        self.web = web  # From the Webdriver class.
        self.wallet = wallet  # From the Wallet class.
        self.recaptcha = recaptcha  # From the Structure class.

    def get_url(self) -> None:
        """Get the create URL depending on collection."""
        create_url = (self.create_url.format(
            'collection/' + self.structure.collection + '/', 's') if
            self.structure.collection.lower() == self.structure.collection and
            self.structure.collection.replace('-', '').isalpha() and
            self.structure.collection != '' else self.create_url.format('', '')
        ) + '?enable_supply=true'  # Collection URL or default.
        self.web.driver.get(create_url)
        return create_url

    def files(self) -> None:
        """Upload the file and its preview if it exists."""
        if isinstance(self.structure.file_path, list):
            if len(self.structure.file_path) == 2:
                file_path = abspath(self.structure.file_path[0])
                preview = abspath(self.structure.file_path[1])
        else:  # No preview file.
            file_path = abspath(self.structure.file_path)
        if not exists(file_path):  # Upload the NFT file.
            raise TE('File doesn\'t exist or path is incorrect.')
        if getsize(file_path) / (1024 ** 2) > 100:
            raise TE('File size must be less than 100 MegaBytes.')
        if splitext(file_path)[1][1:].lower() not in \
            ('jpg', 'jpeg', 'png', 'gif', 'svg', 'mp4',  # Check the file
             'webm', 'mp3', 'wav', 'ogg', 'glb', 'gltf'):  # extensions.
            raise TE('The file extension is not supported on OpenSea.')
        self.web.is_empty('//*[@id="media"]', file_path)
        if splitext(file_path)[1][1:].lower() in \
                ('mp4', 'webm', 'mp3', 'wav', 'ogg', 'glb', 'gltf'):
            if not exists(preview):  # Upload the NFT file.
                raise TE('File doesn\'t exist or path is incorrect.')
            if getsize(preview) / (1024 ** 2) > 100:
                raise TE('File size must be less than 100 MegaBytes.')
            self.web.is_empty('//input[@name="preview"]', preview)

    def name(self) -> None:
        """Check if the NFT name is not empty and send it."""
        if self.web.is_empty('//*[@id="name"]', self.structure.nft_name):
            raise TE('The NFT name is missing.')

    def external_link(self) -> None:
        """Check if the external link is not empty and send it."""
        self.web.is_empty('//*[@id="external_link"]',
                          self.structure.external_link)

    def description(self) -> None:
        """Check if the description is not empty and send it."""
        # Replace the "\n" by "&#13;&#10;" to make a break line.
        self.web.is_empty('//*[@id="description"]', self.structure
            .description.replace('\\n', Keys.ENTER))

    def collection(self, create_url: str) -> None:
        """Check the collection format and send it."""
        self.web.clear_text('//*[@id="collection"]')
        if self.create_url.format('', '') + '?enable_supply=true' == \
            create_url and not self.web.is_empty(
                '//*[@id="collection"]', self.structure.collection):
            try:  # Try to click on the collection button.
                self.web.clickable(  # Click on the collection span.
                    '//span[contains(text(), "'
                    f'{self.structure.collection}")]/../..')
            except Exception:  # If collection doesn't exist.
                raise TE('Collection doesn\'t exist or can\'t be found.')

    def attributes(self) -> None:
        """Send each properties, levels and stats."""
        datas = [self.structure.properties, self.structure.levels,
                 self.structure.stats]  # List for all attributes.
        for index in range(len(datas)):  # Add properties, levels & stats.
            if not len(datas[index]) > 0:  # Check if data is not empty.
                continue  # Pass this data because it's empty or null.
            # Change element from a list of strings to a list of lists.
            if not isinstance(datas[index][0], list):
                datas[index] = [datas[index]]  # Target maybe useless.
            self.web.clickable(  # Click on "+" button to open the pop up.
                f'//form/section/div[{index + 1}]/div/div[2]/button')
            number_ = 0  # Counter of properties/levels/stats to input.
            for data in datas[index]:
                if number_ > 0:  # If there are more than 1 element.
                    # Click on "Add more" button.
                    self.web.clickable('//div[@role="dialog"]/section/button')
                number_ += 1  # Increase number to add more element.
                self.web.send_keys(  # Input values in the inputs.
                    f'/html/body/div[{index + 2}]/div/div/div/section/table'
                    f'/tbody/tr[{number_}]/td[1]/div/div/input', data[0])
                for rank in [3, 2]:  # Input third and second values.
                    if len(data) == 3 or rank == 2:  # 1 or 2 loops.
                        actual_element = f'/html/body/div[{index + 2}]' + \
                            '/div/div/div/section/table/tbody/' + \
                            f'tr[{number_}]/td[{rank}]/div/div/input'
                        self.web.clear_text(actual_element)  # Default value.
                        self.web.send_keys(actual_element, data[rank - 1])
            # Click on the "Save" button.
            self.web.clickable('//footer/button')

    def unlockable_content(self) -> None:
        """Toggle the switch button and send the unlockable content."""
        if isinstance(self.structure.unlockable_content, list) and \
            len(self.structure.unlockable_content) == 2 and isinstance(
                self.structure.unlockable_content[0], bool) and \
                self.structure.unlockable_content[0] and \
                self.structure.unlockable_content[1] != '':
            self.web.send_keys('//*[@id="unlockable-content-toggle"]',
                               Keys.ENTER)  # Toggle the switch button.
            self.web.send_keys(  # Input the unlockable content.
                '//div[contains(@class, "unlockable")]/textarea',
                self.structure.unlockable_content[1])

    def explicit_and_sensitive_content(self) -> None:
        """Toggle the switch button if true."""
        if isinstance(self.structure.explicit_and_sensitive_content, bool) \
                and self.structure.explicit_and_sensitive_content:
            self.web.send_keys('//*[@id="explicit-content-toggle"]',
                               Keys.ENTER)  # Toggle the switch button.

    def supply_number(self) -> None:
        """Change the supply number if it is greater than 1."""
        if 'supply=' in self.web.driver.current_url and isinstance(
                self.structure.supply, int) and self.structure.supply > 1:
            self.web.send_keys('//*[@id="supply"]',
                               f'{Keys.BACKSPACE}{self.structure.supply}')
        else:  # This is important for the sale part.
            self.structure.supply = 1

    def blockchain(self) -> None:
        """Change the Blockchain if it is different than default."""
        if self.structure.blockchain != '' and self.web.visible(
                '//*[@id="chain"]').get_attribute('value') != \
                self.structure.blockchain:  # Compare to the span text.
            try:  # Try to select the Blockchain.
                self.web.clickable('//*[@id="chain"]/..')  # Open the sheet.
                self.web.clickable('//span[contains(text(), '
                                   f'"{self.structure.blockchain}")]/../..')
            except Exception:  # Blockchain is unknown.
                raise TE('Blockchain is unknown or badly written.')
        elif self.structure.blockchain == '':  # Important for the sale part.
            self.structure.blockchain = 'Ethereum'

    def submit(self) -> None:
        """Click on the submit button."""
        self.web.clickable('(//div[contains(@class, "submit")])[position()=1]'
                           '/div/span/button')  # Click on the "Create" button.

    def solve_recaptcha(self) -> None:
        """Check if reCAPTCHA is displayed and call the solver."""
        try:
            self.web.visible('(//div[@class="g-recaptcha"])[position()=1]')   
            if self.solver in [2, 3, 4]:  # reCAPTCHA solver activated.
                print(f'{YELLOW}Solving the reCAPTCHA.{RESET}', end=' ')
                if not self.recaptcha.solve(self.web):
                    raise TE('Cannot solve the reCAPTCHA.')
                print(f'{GREEN}Solved.{RESET}', end=' ')
            else:  # When solved, webpage changes.
                print(f'{YELLOW}reCAPTCHA displayed.{RESET}', end=' ')
            if self.solver == 4:
                self.submit()  # Submit the form.
        except Exception:
            pass

    def save_sale(self) -> None:
        """Save the file for a future sale."""
        if 2 not in self.structure.action:  # Save the data for future upload.
            self.structure.nft_url = self.web.driver.current_url  # NFT URL.
            self.save.save_sale()  # Save for a future listing.

    def upload(self) -> bool:
        """Upload multiple NFTs automatically on OpenSea."""
        print('Uploading NFT.', end=' ')
        try:  # Go to the OpenSea create URL and input all datas of the NFT.
            create_url = self.get_url()  # Get the create URL.
            self.files()  # Send file and preview.
            self.name()  # Send NFT name.
            self.external_link()  # Send external link.
            self.description()  # Send description.
            self.collection(create_url)  # Send collection.
            self.attributes()  # Send all attributes.
            self.unlockable_content()  # Send unlockable content.
            self.explicit_and_sensitive_content()  # Send explicit content.
            self.supply_number()  # Send supply number.
            self.blockchain()  # Send blockchain.
            self.submit()  # Submit content.
            self.solve_recaptcha()  # Solve the reCAPTCHA.
            # Wait until the page URL changes.
            WDW(self.web.driver, 600 if self.solver == 1 else 20).until(
                lambda _: self.web.driver.current_url != create_url)
            print(f'{GREEN}NFT uploaded.{RESET}')
            if 2 not in self.structure.action:
                self.save_sale()  # Save the file for a future sale.
            self.fails = 0  # Reset the counter for next upload.
            return True  # If it perfectly worked.
        except Exception as error:  # Any other error.
            if self.web.page_error():  # Check if there is a 404
                return self.upload()  # page error.
            print(f'{RED}Upload failed.{RESET}',
                  str(error).replace('Message: ', '').replace('\n', '')
                  if 'Stacktrace' not in str(error) else '')
            self.wallet.close()  # Close the wallet extension popup.
            self.fails += 1  # Increment the counter.
            if self.fails > UPLOAD_FAILS:  # Too much fails.
                self.save.save_upload() if 2 not in self.structure.action \
                    else self.save.save_upload_and_sale()  # Save the details.
                self.fails = 0  # Reset the counter for next upload.
                return False  # It failed.
            return self.upload()  # Try to re-upload the NFT.
