# -*- coding: utf-8 -*-
# app/services/wallets/coinbase_self.wallet.py


"""
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn
"""


# Selenium module imports: pip install selenium
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.common.exceptions import TimeoutException as TE

#  Python internal imports.
from ...utils.colors import GREEN, RED, RESET
from ...utils.const import COINBASE_WALLET_IMPORT


class CoinbaseWallet:
    """Allow the connection and the signature of contracts."""

    def __init__(self, web: object, wallet: object) -> None:
        self.fails = 0  # Counter of fails during wallet connection.
        # Get the instance of the needed classes.
        self.web = web  # From the Webdriver class.
        self.wallet = wallet  # From the Wallet class.

    def login(self) -> bool:
        """Login to the Coinbase Wallet."""
        try:
            print('Login to Coinbase Wallet.', end=' ')
            self.web.window_handles(0)  # Switch to the Coinbase extension.
            self.web.driver.refresh()  # Prevent a blank page.
            self.web.clickable(  # Click on the "Import wallet" button.
                '//*[@data-testid="btn-import-existing-wallet"]')
            self.web.clickable(  # Click on the "Enter recovery phrase" button.
                '//*[@data-testid="btn-import-recovery-phrase"]')
            if (self.wallet  # If the recovery phrase / password are not set.
                    .recovery_phrase == '' and self.wallet.password == ''):
                input(COINBASE_WALLET_IMPORT)
                print(f'{GREEN}Logged to Coinbase Wallet.{RESET}')
                self.wallet.success = True
                return  # User log in to Coinbase Wallet.
            self.web.send_keys(  # Input the recovery phrase.
                '//*[@data-testid="seed-phrase-input"]',
                self.wallet.recovery_phrase)
            # Click on the "Import Wallet" button.
            self.web.clickable('//*[@data-testid="btn-import-wallet"]')
            # Input a new password or the same password of your account.
            self.web.send_keys('//*[@id="Password"]', self.wallet.password)
            self.web.send_keys(  # Input a second time the password.
                '//*[@id="Verify password"]', self.wallet.password)
            self.web.clickable(  # Click on the "I have read..." checkbox.
                '//*[@data-testid="terms-and-privacy-policy-parent"]')
            # Click on the "Submit" button.
            self.web.clickable('//*[@data-testid="btn-password-continue"]')
            print(f'{GREEN}Logged to Coinbase Wallet.{RESET}')
            self.wallet.success = True
        except Exception:  # Failed - a web element is not accessible.
            self.fails += 1  # Increment the counter.
            if self.fails < 2:  # Retry login to the Coinbase Wallet.
                print(f'{RED}Login to Coinbase Wallet'
                      f' failed. Retrying.{RESET}')
                self.login()
            else:  # Failed twice - the wallet is not accessible.
                print(f'{RED}Login to Coinbase Wallet'
                      f' failed. Restarting.{RESET}')
                self.web.quit()  # Stop the webdriver.
                self.wallet.success = False

    def sign(self, _: bool, __: int) -> None:
        """Sign the Coinbase Wallet contract to login to OpenSea."""
        self.web.window_handles(2)  # Switch to the Coinbase Wallet pop up tab.
        self.web.clickable('//*[@data-testid="allow-authorize-button"]')
        try:  # Wait until the Coinbase Wallet pop up is closed.
            WDW(self.web.driver, 10).until(EC.number_of_windows_to_be(2))
        except TE:
            self.contract()  # Sign the contract a second time.
        self.web.window_handles(1)  # Switch back to the OpenSea tab.

    def contract(self, _: bool) -> None:
        """Sign a Coinbase Wallet contract to upload or confirm sale."""
        self.web.window_handles(2)  # Switch to the Coinbase Wallet pop up tab.
        self.web.clickable('//*[@data-testid="sign-message"]')
        try:  # Wait until the Coinbase Wallet pop up is closed.
            WDW(self.web.driver, 10).until(EC.number_of_windows_to_be(2))
        except TE:
            self.contract()  # Sign the contract a second time.
        self.web.window_handles(1)  # Switch back to the OpenSea tab.

    def close(self) -> None:
        """Close the Coinbase Wallet popup."""
        try:
            if len(self.web.driver.window_handles) > 2:
                self.web.window_handles(2)  # Switch to the Coinbase popup.
                self.web.driver.close()  # Close the popup extension.
                self.web.window_handles(1)  # Switch back to OpenSea.
        except Exception:
            pass  # Ignore the exception.
