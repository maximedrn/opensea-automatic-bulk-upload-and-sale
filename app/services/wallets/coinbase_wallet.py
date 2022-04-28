#!/usr/bin/python
# app/services/wallets/coinbase_self.wallet.py


"""
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn

Copyright © 2022 Maxime Dréan. All rights reserved.
Any distribution, modification or commercial use is strictly prohibited.

Version 1.7.0 - 2022, 24 April.

Transfer as many non-fungible tokens as you want to
the OpenSea marketplace. Easy, efficient and fast,
this tool lets you make your life as an Artist of
the digital world much smoother.
"""


# Selenium module imports: pip install selenium
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.common.exceptions import TimeoutException as TE

# A Python internal import.
from ...utils.colors import GREEN, RED, RESET


class CoinbaseWallet:

    def __init__(self, web: object, wallet: object) -> None:
        self.fails = 0  # Counter of fails during wallet connection.
        # Get the instance of the needed classes.
        self.web = web  # From the Webdriver class.
        self.wallet = wallet  # From the Wallet class.

    def login(self) -> bool:
        """Login to the Coinbase self.wallet."""
        try:
            print('Login to Coinbase self.wallet.', end=' ')
            self.web.window_handles(0)  # Switch to the Coinbase Wallet extension.
            self.web.driver.refresh()  # Reload the page to prevent a blank page.
            # Click on the "Import wallet" button.
            self.web.clickable('(//*[@data-testid="btn-import-existing-wallet"])')
            # Click on the "Enter recovery phrase" button.
            self.web.clickable('(//*[@data-testid="btn-import-recovery-phrase"])')
            self.web.send_keys(  # Input the recovery phrase.
                '//*[@data-testid="seed-phrase-input"]', self.wallet.recovery_phrase)
            # Click on the "Import Wallet" button.
            self.web.clickable('(//*[@data-testid="btn-import-wallet"])')
            # Input a new password or the same password of your account.
            self.web.send_keys('//*[@id="Password"]', self.wallet.password)
            self.web.send_keys('//*[@id="Verify password"]', self.wallet.password)
            # Click on the "I have read and agree to the..." checkbox.
            self.web.clickable(
                '(//*[@data-testid="terms-and-privacy-policy-parent"])')
            # Click on the "Submit" button.
            self.web.clickable('(//*[@data-testid="btn-password-continue"])')
            print(f'{GREEN}Logged to Coinbase self.wallet.{RESET}')
            return True
        except Exception:  # Failed - a web element is not accessible.
            self.fails += 1  # Increment the counter.
            if self.fails < 2:  # Retry login to the self.wallet.
                print(f'{RED}Login to Coinbase failed. Retrying.{RESET}')
                return self.login()
            print(f'{RED}Login to Coinbase failed. Restarting.{RESET}')
            self.web.quit()  # Stop the webdriver.
            return False

    def sign(self) -> None:
        """Sign the Coinbase Wallet contract to login to OpenSea."""
        self.web.window_handles(2)  # Switch to the Coinbase Wallet pop up tab.
        self.web.clickable('(//*[@data-testid="allow-authorize-button"])')
        try:  # Wait until the Coinbase Wallet pop up is closed.
            WDW(self.web.driver, 10).until(EC.number_of_windows_to_be(2))
        except TE:
            self.contract()  # Sign the contract a second time.
        self.web.window_handles(1)  # Switch back to the OpenSea tab.

    def contract(self, new_contract: bool = False) -> None:
        """Sign a Coinbase Wallet contract to upload or confirm sale."""
        self.web.window_handles(2)  # Switch to the Coinbase Wallet pop up tab.
        self.web.clickable('(//*[@data-testid="sign-message"])')
        try:  # Wait until the Coinbase Wallet pop up is closed.
            WDW(self.web.driver, 10).until(EC.number_of_windows_to_be(2))
        except TE:
            self.contract()  # Sign the contract a second time.
        self.web.window_handles(1)  # Switch back to the OpenSea tab.

    def close(self) -> None:
        """Close the Coinbase Wallet popup."""
        if len(self.web.driver.window_handles) > 2:
            try:
                self.web.window_handles(2)  # Switch to the Coinbase Wallet popup.
                self.web.driver.close()  # Close the popup extension.
                self.web.window_handles(1)  # Switch back to OpenSea.
            except Exception:
                pass  # Ignore the exception.
