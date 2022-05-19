#!/usr/bin/python
# app/services/processes/sale.py


"""
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn

Copyright © 2022 Maxime Dréan. All rights reserved.
Any distribution, modification or commercial use is strictly prohibited.
"""


# Selenium module imports: pip install selenium
from selenium.common.exceptions import TimeoutException as TE
from selenium.webdriver.common.keys import Keys

# Python internal imports.
from ...utils.colors import GREEN, RED, YELLOW, RESET


class Sale:
    """List the NFTs to OpenSea."""

    def __init__(self, structure: object, save: object,
                 web: object, wallet: object) -> None:
        """Get the password and the recovery_phrase from the text file."""
        self.fails = 0  # Counter of sale retries.
        self.actual_blockchain = 'Ethereum'  # Default blockchain.
        # Get the instance of the needed classes.
        self.structure = structure  # From the Structure class.
        self.save = save  # From the Save class.
        self.web = web  # From the Webdriver class.
        self.wallet = wallet  # From the Wallet class.

    def switch_ethereum(self) -> None:
        """Switch to Ethereum blockchain if wallet is on Polygon."""
        if self.structure.blockchain == 'Ethereum' and self.\
                actual_blockchain != 'Ethereum':  # Different blockchain.
            if 1 not in self.structure.action:
                self.web.driver.get(self.structure.nft_url)
            self.web.clickable('//a[contains(@href, "/sell")]')
            self.web.clickable('//button[contains(text(), "Switch")]')
            self.wallet.sign(False, 1)  # Approve.
            self.web.window_handles(1)  # Switch back to the OpenSea tab.
            self.actual_blockchain == 'Ethereum'
        elif 1 in self.structure.action:  # If it's already set to Ethereum.
            self.structure.nft_url = self.web.driver.current_url\
                .replace('/sell', '')  # Remove the "/sell" part.
            self.web.driver.get(self.structure.nft_url + '/sell')  # Sale page.
        else:  # Sale only, go to the URL page.
            self.web.driver.get(self.structure.nft_url.replace(
                '/sell', '') + '/sell')

    def switch_polygon(self) -> bool:
        """Switch to Polygon blockchain if wallet is on Ethereum."""
        try:  # Switch blockchain.
            if self.web.visible(
                    '//*[contains(@id, "dy react-aria")]/div/div/button'
            ).get_attribute('innerHTML') == 'Switch':
                self.web.clickable(  # Click on the "Switch" button.
                    '//*[contains(@id, "Body react-aria")]/div/div/button')
                self.wallet.sign(False)  # Approve.
                self.web.window_handles(1)  # Switch back to the OpenSea tab.
                self.web.driver.refresh()  # Reload the page.
                self.actual_blockchain = 'Polygon'  # Change blockchain.
                print(f'{YELLOW}Blockchain switched.{RESET}')
                return True  # Done, blockchain switched.
            return False  # Not a "Switch" button.
        except Exception:
            return False

    def check_price(self) -> None:
        """Check the price and the quantity number."""
        if not isinstance(self.structure.supply, int):
            raise TE('The supply number must be an integer.')
        if not isinstance(self.structure.price, int) and not \
                isinstance(self.structure.price, float):
            raise TE('The price must be an integer or a float.')

    def timed_auction(self) -> None:
        """Select Timed Auction and change method."""
        if 'Timed' in str(self.structure.sale_type):  # Timed Auction.
            # Click on the "Timed Auction" button.
            self.web.clickable('//i[@value="timelapse"]/../..')
            if isinstance(self.structure.method, list) and len(
                    self.structure.method) == 2:  # [method, price]
                if not isinstance(self.structure.method[1], int) and \
                        not isinstance(self.structure.method[1], float):
                    raise TE('Prices must be integer or float.')
                if 'declining' in str(self.structure.method[0]):
                    self.declining_price()
                elif 'highest' in str(self.structure.method[0]):
                    self.highest_bidder()
                else:  # Not a Declining price or a Highest bidder.
                    raise TE('Unknown method for Timed Auction.')

    def declining_price(self) -> None:
        """Sell with declining price (Timed Auction)."""
        self.web.clickable('//*[@id="main"]/div/div/div[3]/div/div[2]'
                           '/div/div[1]/form/div[2]/div/div[2]')
        # Click on the "Sell with declining price"
        self.web.clickable('//*[@role="tooltip"]/div/div/ul/li/button')
        if self.structure.method[1] < self.structure.price:
            self.web.send_keys('//*[@name="endingPrice"]',
                               format(self.structure.method[1], '.8f'))
        else:  # Ending price is higher than the price.
            raise TE('The ending price must be higher'
                     ' than the starting price.')

    def highest_bidder(self) -> None:
        """Sell with highest bidder (Timed Auction)."""
        if self.structure.method[1] > 0 and (self.structure.method[
                1] <= 1 or self.structure.method[1] < self.structure.price):
            raise TE('Reserve price must be higher than 1 WETH and the price.')
        # Click on the "More option" button.
        self.web.clickable('//button[contains(@class, "more-options")]')
        # Click on the "Include reserve price"
        self.web.send_keys('//*[@role="switch"]', Keys.ENTER)
        self.web.send_keys('//*[@name="reservePrice"]',
                           format(self.structure.method[1], '.8f'))

    def quantity(self) -> None:
        """Send the quantity number of NFT to list."""
        if isinstance(self.structure.quantity, int):
            if self.structure.quantity <= self.structure.supply:
                self.web.send_keys('//*[@id="quantity"]', f'{Keys.BACKSPACE}'
                                   f'{self.structure.quantity}')
            else:  # Quantity number is higher that supply number.
                raise TE('Quantity must be less or equal to supplies.')

    def specific_buyer(self) -> None:
        """Set a specific buyer."""
        if 'Timed' not in str(self.structure.sale_type) and isinstance(
                self.structure.specific_buyer, list) and len(
                    self.structure.specific_buyer) == 2 and isinstance(
                        self.structure.specific_buyer[0], bool) and \
                self.structure.specific_buyer[0]:
            # Click on the "More option" button.
            self.web.clickable('//button[contains(@class, "more-options")]')
            # Click on "Reserve for specific buyer".
            self.web.send_keys('(//*[@role="switch"])[last()]', Keys.ENTER)
            self.web.send_keys('//*[@id="reservedBuyerAddressOrEns'
                               'Name"]', self.structure.specific_buyer[1])

    def price(self) -> None:
        """Set the price."""
        self.web.send_keys('//*[@name="price"]',
                           format(self.structure.price, '.8f'))

    def duration(self, date: str = '%d-%m-%Y %H:%M') -> None:
        """Select the duration according to its format."""
        if isinstance(self.structure.duration, str):  # Transform to a list.
            self.structure.duration = [self.structure.duration]
        if isinstance(self.structure.duration, list):  # List of 1 or 2 values.
            if len(self.structure.duration) == 2:  # From {date} to {date}.
                from datetime import datetime as dt  # Default import.
                # Check if duration is less than 6 months.
                if (dt.strptime(self.structure.duration[1], date) -
                        dt.strptime(self.structure.duration[0], date
                                    )).total_seconds() / 60 > 262146:
                    raise TE('Duration must be less than 6 months.')
                # Check if starting date has passed.
                if dt.strptime(dt.strftime(dt.now(), date), date) \
                        > dt.strptime(self.structure.duration[0], date):
                    raise TE('Starting date has passed.')
                # Split the date and the time.
                start_date, start_time = self.structure.duration[0].split(' ')
                end_date, end_time = self.structure.duration[1].split(' ')
                self.web.clickable('//*[@id="duration"]')  # Date button.
                self.web.visible(  # Scroll to the pop up frame of the date.
                    '//*[@role="dialog"]').location_once_scrolled_into_view
                self.web.send_date('//*[@role="dialog"]'  # Ending date.
                                   '/div[2]/div[2]/div/div[2]/input', end_date)
                self.web.send_date('//*[@role="dialog"]/div'  # Starting date.
                                   '[2]/div[1]/div/div[2]/input', start_date)
                self.web.send_date('//*[@id="end-time"]', end_time)
                self.web.send_date(  # Starting date + close tab for Chrome.
                    '//*[@id="start-time"]', start_time if self.web.window == 1
                    else f'{start_time}{Keys.ENTER}')
                self.web.send_keys('//html', Keys.ENTER)  # Close the frame.
            elif len(self.structure.duration) == 1:  # In {n} days/week/months.
                if self.structure.duration[0] == '':  # Duration not specified.
                    raise TE('Duration must be specified.')
                if self.web.visible('//*[@id="duration"]/div[2]').text \
                        != self.structure.duration[0]:  # Not default.
                    self.web.clickable('//*[@id="duration"]')  # Date button.
                    self.web.clickable('//*[@role="dialog"]'  # Duration Range
                                       '/div[1]/div/div[2]/input')  # sheet.
                    self.web.clickable(  # Select the duration.
                        '//span[contains(text(), '
                        f'"{self.structure.duration[0]}")]/../..')
                    self.web.send_keys('//*[@role="dialog"]', Keys.ENTER)

    def complete_listing(self) -> None:
        """Complete the listing by clicking on the button."""
        try:  # Click on the "Complete listing" (submit) button.
            self.web.clickable('//button[@type="submit"]')
        except Exception:  # An unknown error has occured.
            raise TE('The submit button cannot be clicked.')

    def sign_contract(self) -> None:
        """Sign the Polygon or Ethereum contract."""
        try:  # Polygon blockchain requires a click on a button.
            if self.structure.blockchain == 'Polygon':  # "Sign" button.
                self.web.clickable(  # Click on the "Sign" button.
                    '//*[contains(@id, "Body react-aria")]/div/div/button')
            self.wallet.contract(True)  # Sign the Wyvern 2.3 contract.
        except Exception:  # An error occured while listing the NFT.
            raise TE('Cannot sign the wallet contract.')

    def check_listed(self) -> None:
        """Check if the NFT is listed."""
        try:
            self.web.window_handles(1)  # Switch back to the OpenSea tab.
            self.web.visible('//header/h4')
        except Exception:  # Sometimes popup is do not detected.
            if self.structure.blockchain == 'Polygon':
                print(f'{YELLOW}NFT seems to not be listed.{RESET}')

    def sale(self) -> None:
        """Set a price for the NFT and sell it."""
        print('Sale of the NFT.', end=' ')
        try:  # Try to sell the NFT with different types and methods.
            self.switch_ethereum()  # Switch to Ethereum blockchain.
            self.check_price()  # Check the type of the price.
            if self.structure.supply == 1 and \
                    self.structure.blockchain == 'Ethereum':
                self.timed_auction()  # Switch to Timed Auction.
            elif self.structure.supply > 1:
                self.quantity()  # Set a quantity of supply.
            elif self.structure.blockchain not in ('Ethereum', 'Polygon'):
                raise TE('Blockchain is unknown or badly written.')
            self.specific_buyer()  # Set a specific buyer.
            self.price()  # Send the price.
            self.duration()  # Set the duration.
            self.complete_listing()  # Complete listing.
            if self.switch_polygon():  # Switch to Polygon blockchain.
                return self.sale()  # Re list the NFT.
            self.sign_contract()  # Sign the contract.
            self.check_listed()  # Check if the NFT is listed.
            print(f'{GREEN}NFT put up for sale.{RESET}')
        except Exception as error:  # Any other error.
            print(f'{RED}NFT sale cancelled.{RESET}',
                  str(error).replace('Message: ', '').replace('\n', '')
                  if 'Stacktrace' not in str(error) else '')
            self.wallet.close()  # Close the wallet extension popup.
            self.fails += 1  # Increment the counter.
            if self.fails > 1:  # Too much fails.
                self.save.save_sale()  # Save the NFT details for a sale.
            else:  # Retry to list.
                self.sale()  # Try to re-upload the NFT.
        self.fails = 0  # Reset the counter for next listing.


def check_price(price: int, blockchain: str) -> bool:
    """
    Check the price detail in the metadata.

    Return if it is valid or not according to its type
    or if it is positive of strictly positive.
    """
    # In case of the price is not a valid number.
    if not (isinstance(price, int) or isinstance(price, float)):
        print(f'{YELLOW}Sale aborted: price must be a number.{RESET}')
        return False
    # In case of the price is not a (strictly) positive number.
    if (price <= 0 and 'Poly' in blockchain) or \
            (price < 0 and 'Eth' in blockchain):
        print(f'{YELLOW}Sale aborted: price not defined or null.{RESET}')
        return False
    return True
