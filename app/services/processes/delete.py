# -*- coding: utf-8 -*-
# app/services/processes/delete.py


"""
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn
"""


# Python internal imports.
from ...utils.colors import GREEN, RED, RESET


class Delete:
    """Delete NFTs on OpenSea."""

    def __init__() -> None:
        pass
    
    def init(self, structure: object, web: object) -> None:
        """Get the required classes and variables."""
        self.fails = 0  # Counter of sale retries.
        # Get the instance of the needed classes.
        self.structure = structure  # From the Structure class.
        self.web = web  # From the Webdriver class.

    def delete(self) -> None:
        """Delete each NFT one by one."""
        print('Deletion of the NFT.', end=' ')
        try:  # Try to sell the NFT with different types and methods.
            self.web.driver.get(self.structure.nft_url.replace(
                '/edit', ''))  # Go to the NFT page.
            self.web.driver.get(self.web.visible(  # Click on the "Edit" button.
                '//div[contains(@class, "OrderManager")]/div/a'
                ).get_attribute('href'))
            self.web.clickable(  # Click on the "Delete item" button.
                '//div[@class="AssetForm--submit"]/div[@class="'
                'AssetForm--action"][position()=2]')
            # Click on the "Delete item" button a second time.
            self.web.clickable('//footer/div[position()=2]/div/button')
            # "Deleted! Changes will take a minute to reflect." message.
            self.web.visible('//span[contains(@class, "status-done")]')
            print(f'{GREEN}NFT has been deleted.{RESET}')
        except Exception as error:  # Any other error.
            print(f'{RED}NFT cannot be deleted.{RESET}',
                  str(error).replace('Message: ', '') if 'Stacktrace'
                  not in str(error) else '\n', end='')
            self.fails += 1  # Increment the counter.
            if self.fails < 1:  # Retry to delete.
                self.delete()  # Try to re-upload the NFT.
        self.fails = 0  # Reset the counter for next listing.
