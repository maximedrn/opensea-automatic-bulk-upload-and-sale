# Automatically upload your NFTs on Opensea using Python Selenium.

* **(_Version 1.3 - December 23, 2021_).**
* Sign up on [Opensea](https://opensea.io/?ref=0xDD135d5be0a23f6daAAE7D2d0580828c9e09402E) (Affiliate link).
* Sign up on [MetaMask](https://metamask.io/).

# Table of contents:

* **[Changelog](https://github.com/maximedrn/opensea_automatic_uploader#changelog).**
* **[What does this bot do?](https://github.com/maximedrn/opensea_automatic_uploader#what-does-this-bot-do)**
* **[To do list](https://github.com/maximedrn/opensea_automatic_uploader#to-do-list).**
* **[Instructions](https://github.com/maximedrn/opensea_automatic_uploader#instructions)**.
  * [Basic installation of Python for beginners](https://github.com/maximedrn/opensea_automatic_uploader#basic-installation-of-python-for-beginners).
  * [Configuration of the bot](https://github.com/maximedrn/opensea_automatic_uploader#configuration-of-the-bot).
* **[Known issues](https://github.com/maximedrn/opensea_automatic_uploader#known-issues).**
* **[Data files structure](https://github.com/maximedrn/opensea_automatic_uploader#data-files-structure).**
* **[Configuration of the sales part of the NFTs](https://github.com/maximedrn/opensea_automatic_uploader#configuration-of-the-sales-part-of-the-nfts).**

## Changelog:

* **Version 1.3:**
  * Important fixes.
  * CSV file modified: separator changed (from ";" to ";;").
* **Version 1.2:**
  * Possibility to set a price for each NFT added.  
    ➜ 1+ supplies and Polygon blockchain support added.
  * Supply input issue fixed.
  * Calendar method improved.
* **Version 1.2-alpha:**
  * Possibility to set a price for each NFT added.
* **Version 1.1:** 
  * XLSX support added.
  * PC-wide data file browse support.
  * Properties, Stats and Levels issues fixed ([Issue #1](https://github.com/maximedrn/opensea_automatic_uploader/issues/1)).
* **Version 1.0:** 
  * Inital commit.

## What does this bot do?

This script allows you to upload as many NFTs as you want to Opensea, all automatically and quickly (about 2.5 NFTs per minute).

➜ **See this collection (1000 NFTs) I uploaded within 4 hours: https://opensea.io/collection/crypto-parrot-nft.**  
➜ **If you sell any NFT with this bot, you can consider sharing some of your earnings. 😉:  
0xDD135d5be0a23f6daAAE7D2d0580828c9e09402E** (Ethereum).

## To do list:

* ✔ <strike>MetaMask automatic login.</strike>
* ✔ <strike>Opensea automatic login with MetaMask.</strike>
* ❌ Opensea automatic login with different wallets.
* ❌ Collection creator for Opensea.
* ✔ <strike>Automatic NFT uploader.</strike>
* ✔ <strike>Possibility to set a price for each NFT.</strike>  
  * ✔ Support for 1+ supplies and Polygon blockchain.
  * ❌ "Sell as bundle" part (not planned to be added).
  * ❌ **Sale part** (soon).
* ✔ <strike>Data file browsing feature.</strike>
* ✔ <strike>CSV structure reader and interpreter.</strike>
* ✔ <strike>JSON structure reader and interpreter.</strike>
* ✔ <strike>XLSX structure reader and interpreter.</strike>
* ❌ NFT maker local website.

## Instructions:

* ### Basic installation of Python for beginners:
  * Download this repository or clone it:
```
git clone https://github.com/maximedrn/opensea_automatic_uploader.git
```
  * It requires [Python](https://www.python.org/) 3.7 or a newest version.
  * Install [pip](https://pip.pypa.io/en/stable/installation/) to be able to have needed Python modules.
  * Open a command prompt in the repository folder and type:
```
pip install -r requirements.txt
```

* ### Configuration of the bot:
  * Download and install [Google Chrome](https://www.google.com/intl/en_en/chrome/).
  * Download the [ChromeDriver executable](https://chromedriver.chromium.org/downloads) that is compatible with the actual version of your Google Chrome browser and your OS (Operating System). Refer to: _[What version of Google Chrome do I have?](https://www.whatismybrowser.com/detect/what-version-of-chrome-do-i-have)_
  * Extract the executable file from the ZIP file and copy/paste it in the `assets/` folder of the repository. You may need to change the path of the file:
```python
class Webdriver:
    """Webdriver class and methods to prevent exceptions."""

    def __init__(self) -> None:
        """Contains the file paths of the webdriver and the extension."""
        # Used files path, change them with your path if necessary.
        self.webdriver_path = os.path.abspath('assets/chromedriver.exe')  # Edit this line with your executable path.
        self.metamask_extension_path = os.path.abspath('assets/MetaMask.crx')
        self.driver = self.webdriver()  # Start new webdriver.
```
  * **Not recommended:** Download a new version of MetaMask extension (version used for script: 10.1.1.0).
    * Add [Get CRX](https://chrome.google.com/webstore/detail/get-crx/dijpllakibenlejkbajahncialkbdkjc) extension to Chrome:
    * Go on [MetaMask](https://chrome.google.com/webstore/detail/metamask/nkbihfbeogaeaoehlefnkodbefgpgknn) Chrome Web Store webpage.
    * Click on "Get CRX" extension button on top right of your browser.
    * Then click on "Get CRX" button.
  * **Optional:** your MetaMask password and recovery phrase are asked when you first run the bot, but you can:
    * create and open the `assets/password.txt` file and write your MetaMask password;
    * create and open the `assets/recovery_phrase.txt` file and write your recovery phrase.
  * Create your NFTs data file containing all details of each NFT. It can be a JSON, CSV or XLSX file. Save it in the data folder.  
    **[What structure should the files have?](https://github.com/maximedrn/opensea_automatic_uploader#data-files-structure)**
    
## Known issues:

* If you are using a Linux distribution or MacOS, you may need to change some parts of the code:  
  * ChromeDriver extension may need to be changed from `.exe` to something else.
  * This method may need to be edited because a MacOS keyboard cannot select text using <kbd>Ctrl</kbd> <kbd>A</kbd>, it uses <kbd>⌘</kbd> <kbd>A</kbd>:
```python
def clear_text(self, element) -> None:
"""Clear text from an input."""
    self.clickable(element)  # Click on the element then clear its text.
    webdriver.ActionChains(self.driver).key_down(Keys.CONTROL).perform()  # Replace with "Keys.COMMAND".
    webdriver.ActionChains(self.driver).send_keys('a').perform()
    webdriver.ActionChains(self.driver).key_up(Keys.CONTROL).perform()  # Replace with "Keys.COMMAND".
```
* **If you use a JSON file for your NFT data, the file path should not contain a unique "\\". It can be a "/" or a "\\\\":**
```json
"file_path": "C:/Users/Admin/Desktop/MyNFTs/nft_0001.png",
// or:
"file_path": "C:\\Users\\Admin\\Desktop\\MyNFTs\\nft_0001.png",
// but not:
"file_path": "C:\Users\Admin\Desktop\MyNFTs\nft_0001.png", // You can see that "\" is highlighted in red.
```
* The bot may crash at the beginning when loading the MetaMask extension (a Selenium module issue):  
```
selenium.common.exceptions.WebDriverException: Message: unknown error: failed to wait for extension background page to load: chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/background.html from timeout: Timed out receiving message from renderer: 10.000
```
* The may crash at some points with this exception:
```
selenium.common.exceptions.WebDriverException: Message: chrome not reachable
```
* Sometimes the bot indicates that the upload has failed while the NFT has been uploaded (rare).
* The MetaMask login can failed if the contract is not signed.
* The calendar is unstable at points.

* ### Data files structure:

   * <strong>required value *</strong>
          
   <br>
   <table>
      <tbody>
         <tr>
            <td>Settings</td>
            <td>Types</td>
            <td>Examples</td>
         </tr>
         <tr>
            <td><strong>File Path *</strong></td>
            <td>String</td>
         </tr>
         <tr>
            <td><strong>NFT Name *</strong></td>
            <td>String</td>
         </tr>
         <tr>
            <td>External Link</td>
            <td>String</td>
         </tr>
         <tr>
            <td>Description</td>
            <td>String</td>
         </tr>
         <tr>
            <td>Collection</td>
            <td>String</td>
         </tr>
         <tr>
            <td>Properties</td>
            <td>List[[String, String], ...] or List[String, String]</td>
            <td>["type", "name"] or [["type", "name"], ["type", "name"]]</td>
         </tr>
         <tr>
            <td>Levels</td>
            <td>List[[String, Integer, Integer], ...] or List[String, Integer, Integer]</td>
            <td>["name", "value_from", "value_to"] or [["name", "value_from", "value_to"], ["name", "value_from", "value_to"]]</td>
         </tr>
         <tr>
            <td>Stats</td>
            <td>List[[String, Integer, Integer], ...] or List[String, Integer, Integer]</td>
            <td>["name", "value_from", "value_to"] or [["name", "value_from", "value_to"], ["name", "value_from", "value_to"]]</td>
         </tr>
         <tr>
            <td>Unlockable Content</td>
            <td>List[Boolean, String] or List[Boolean] or Boolean</td>
           <td>[True, "unlockable_content"] or [False] or False</td>
         </tr>
         <tr>
            <td>Explicit And Sensitive Content</td>
            <td>Boolean</td>
         </tr>
         <tr>
            <td>Supply</td>
            <td>Integer</td>
         </tr>
         <tr>
            <td>Blockchain</td>
            <td>String</td>
         </tr>
         <tr>
            <td>Sale Type (only for Ethereum Blockchain and 1 supply)</td>
            <td>String</td>
         </tr>
         <tr>
            <td><strong>Price *</strong></td>
            <td>Float or Integer</td>
         </tr>
         <tr>
            <td>Method (only for "Timed Auction")</td>
            <td>List[String, Float]</td>
            <td>["method", "price"] or ["method, ""]
         </tr>
         <tr>
            <td>Duration ("DD-MM-YYYY HH:MM")</td>
            <td>List[String, String] or List[String] or String</td>
            <td>["from_date", "to_date"] or ["days/weeks/months"] or "days/weeks/months"</td>
         </tr>
         <tr>
            <td>Specific Buyer</td>
            <td>List[Boolean, String] or [Boolean] or Boolean</td>
            <td>[True, "wallet"] or [False] or False
         </tr>
         <tr>
            <td>Quantity (only for 1+ supplies)</td>
            <td>Integer</td>
         </tr>
      </tbody>
   </table>

   And it gives you something like this ([CSV](https://github.com/maximedrn/opensea_automatic_uploader/blob/master/data/csv_structure.csv), [JSON](https://github.com/maximedrn/opensea_automatic_uploader/blob/master/data/json_structure.json), [XLSX](https://github.com/maximedrn/opensea_automatic_uploader/blob/master/data/xlsx_structure.xlsx)).
   
## Configuration of the sales part of the NFTs:

* If Blockhain is **Ethereum**:
  * If supply number is **equal to 1**:
    * If you chose a **Fixed Price**:
      * **Price** (ETH). 
      * **Duration**: from a date to an other date (less than 6 months) or:
        * 1 day.
        * 3 days.
        * 1 week.
        * 6 months.
      * **Sell as bundle.** ➜ **Not supported.**
      * **Reserve for specific buyer**. 
    * If you chose a **Timed Auction**:
      * 1st method: **Sell to highest bidder**:
        * **Starting Price** (WETH).
        * **Duration**: from a date to an other date (less than 6 months) or:
          * 1 day.
          * 3 days.
          * 1 week.
        * _Optional_: **Reserved Price** (WETH) greater than 1 WETH and greater than **Starting Price**.
      * 2nd method: **Sell with declining price**:
        * **Starting Price** (ETH).
        * **Duration**: from a date to an other date (less than 6 months) or:
          * 1 day.
          * 3 days.
          * 1 week.
        * **Ending Price** (ETH) less than **Starting Price**.
   * If supply number is **higher than 1**:  
     * **Price** (ETH). 
     * **Duration**: from a date to an other date (less than 6 months) or:
       * 1 day.
       * 3 days.
       * 1 week.
       * 6 months.
     * **Sell as bundle.** ➜ **Not supported.**
     * **Reserve for specific buyer**. 
* If Blockchain is **Polygon**:  
  * If supply number is **equal to 1**:  
    * **Price** (ETH). 
    * **Duration**: from a date to an other date (less than 6 months) or:
      * 1 day.
      * 3 days.
      * 1 week.
      * 6 months.
  * If supply number is **higher than 1**:  
    * **Quantity** (less or equal to the supply). 
    * **Price** (ETH). 
    * **Duration**: from a date to an other date (less than 6 months) or:
      * 1 day.
      * 3 days.
      * 1 week.
      * 6 months.
    * **Reserve for specific buyer**. 
