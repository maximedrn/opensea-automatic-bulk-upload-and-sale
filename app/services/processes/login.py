#!/usr/bin/python
# app/services/processes/login.py


"""
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn

Copyright © 2022 Maxime Dréan. All rights reserved.
Any distribution, modification or commercial use is strictly prohibited.
"""


# Selenium module imports: pip install selenium
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

# Python internal imports.
from ...utils.colors import GREEN, RED, RESET


class Login:
    """Main class: OpenSea automatic uploader."""

    def __init__(self, web: object, wallet: object) -> None:
        """Get the password and the recovery_phrase from the text file."""
        self.login_url = 'https://opensea.io/login?referrer=%2Fasset%2Fcreate'
        self.create_url = 'https://opensea.io/asset/create'
        self.fails = 0  # Counter of fails during wallet connection.
        self.success = False  # Boolean returned after login.
        # Get the instance of the needed classes.
        self.web = web  # From the Webdriver class.
        self.wallet = wallet  # From the Wallet class.

    def login(self) -> bool:
        """Login to OpenSea using a specific self.wallet."""
        try:  # Try to login to the OpenSea using a specific self.wallet.
            print('Login to OpenSea.', end=' ')
            self.web.window_handles(1)  # Switch to the main (data:,) tab.
            self.web.driver.get(self.login_url)  # Go to the OpenSea login URL.
            # Click on the wallet button.
            self.web.clickable('//i[@value="account_balance_wallet"]/..')
            # Click on the "Show more options" button.
            self.web.clickable('//button[contains(@class, "show-more")]')
            self.web.clickable(  # Click on the wallet button in the list.
                f'//*[contains(text(), "{self.wallet.wallet}")]/../..')
            self.wallet.sign()  # Sign the login on OpenSea.
            # Check if the login to OpenSea worked.
            WDW(self.web.driver, 15).until(EC.url_to_be(self.create_url))
            print(f'{GREEN}Logged to OpenSea.{RESET}')
            return True
        except Exception:  # The contract failed.
            try:  # Using the custom Google Chrome profile.
                if self.web.visible('//img[@alt="Account"]'):
                    print(f'{GREEN}Logged to OpenSea.{RESET}')
                    return True  # Already connected.
            except Exception:
                pass  # Ignore the error.
            try:  # Not a custom Google Chrome profile.
                self.wallet.sign(False, 1) if self.web.window == 1 else \
                    self.wallet.contract()  # Sign the contract.
                self.web.window_handles(1)  # Switch again to the OpenSea tab.
                # Check again if the login to OpenSea worked.
                WDW(self.web.driver, 10).until(EC.url_to_be(self.create_url))
                print(f'{GREEN}Logged to OpenSea.{RESET}')
                return True
            except Exception:
                self.fails += 1  # Increment the counter of failure.
                if self.fails < 2:  # Retry to login to the OpenSea.
                    print(f'{RED}Login to OpenSea failed. Retrying.{RESET}')
                    self.web.window_handles(1)  # Switch to the OpenSea tab.
                    self.web.driver.refresh()  # Reload the page.
                    return self.login()  # Retry to login again.
                else:  # Too many fails.
                    print(f'{RED}Login to OpenSea failed. Restarting.{RESET}')
                    self.web.quit()  # Stop the webdriver.
                    return False
