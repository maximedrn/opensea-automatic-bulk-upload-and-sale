# -*- coding: utf-8 -*-
# app/services/processes/login.py


"""
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn
"""


# Selenium module imports: pip install selenium
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

# Python internal imports.
from ...utils.colors import GREEN, RED, RESET


class Login:
    """Log to OpenSea by signing the contract."""

    def __init__(self, web: object, wallet: object) -> None:
        """Get the password and the recovery_phrase from the text file."""
        self.login_url = 'https://opensea.io/login'
        self.create_url = 'https://opensea.io/asset/create'
        self.fails = 0  # Counter of fails during wallet connection.
        self.success = False  # Boolean returned after login.
        # Get the instance of the needed classes.
        self.web = web  # From the Webdriver class.
        self.wallet = wallet  # From the Wallet class.

    def login(self, signed: bool = False) -> bool:
        """Login to OpenSea using a specific self.wallet."""
        try:  # Try to login to the OpenSea using a specific self.wallet.
            print('Login to OpenSea.', end=' ')
            if not signed:  # The first time on the page.
                self.web.window_handles(1)  # Switch to the main (data:,) tab.
                self.web.driver.get(self.login_url)  # Go to the login URL.
                self.web.clickable(  # Click on the wallet button.
                    '//a[contains(@href, "account")]/../div/button')
                # Click on the "Show more options" button.
                self.web.clickable('//button[contains(@class, "show-more")]')
                self.web.clickable(  # Click on the wallet button in the list.
                    f'//*[contains(text(), "MetaMask")]/../..')
                self.wallet.sign(False)  # Sign the login on OpenSea.
                signed = True  # The wallet is signed.
            self.web.window_handles(1)  # Switch to the main (data:,) tab.
            self.web.driver.get(self.create_url)  # Go to the create URL.
            WDW(self.web.driver, 10).until(lambda _: self.sign_login())
            # Check if the login to OpenSea worked.
            WDW(self.web.driver, 10).until(EC.url_to_be(self.create_url))
            print(f'{GREEN}Logged to OpenSea.{RESET}')
            self.fails = 0  # Reset the counter.
            return True
        except Exception:  # The contract failed.
            self.fails += 1  # Increment the counter of failure.
            if self.fails < (4 if signed else 2):  # Retry to login.
                print(f'{RED}Login to OpenSea failed. Retrying.{RESET}')
                self.web.window_handles(1)  # Switch to the OpenSea tab.
                self.web.driver.get(self.create_url)  # Go to the create URL.
                return self.login(signed)  # Retry to login again.
            print(f'{RED}Login to OpenSea failed. Restarting.{RESET}')
            self.web.quit()  # Stop the webdriver.
            return False

    def sign_login(self) -> bool:
        """Sign the OpenSea contract for NFT creation."""
        try:  # Try until it works for 30 seconds.
            self.web.window_handles(1)  # Switch again to the OpenSea tab.
            self.web.clickable(  # Click on the wallet button in the list.
                f'//*[contains(text(), "MetaMask")]/../../../button')
            WDW(self.web.driver, 5).until(EC.number_of_windows_to_be(3))
            self.wallet.contract()  # Sign the creation on OpenSea.
            self.web.window_handles(1)  # Switch again to the OpenSea tab.
            return True
        except Exception:
            return False