# Upload automatically your NFTs on Opensea using Python Selenium.

* **(_Version 1.1 - October 28, 2021)._**
* Sign up on [Opensea](https://opensea.io/?ref=0xDD135d5be0a23f6daAAE7D2d0580828c9e09402E) (Affiliate link).
* Sign up on [MetaMask](https://metamask.io/).

## Known issues:

* If you are using a Linux distribution or MacOS, you may need to change some parts of the code:  
  * Colorama module sometimes does not work.
  * ChromeDriver extension may need to be changed from `.exe` to something else.
* **If you use a JSON file for your NFT data, the file path should not contain a unique "\\". It can be a "/" or a "\\\\":**
```json
"file_path": "C:/Users/Admin/Desktop/MyNFTs/nft_0001.png",
// or:
"file_path": "C:\\Users\\Admin\\Desktop\\MyNFTs\\nft_0001.png",
// but not:
"file_path": "C:\Users\Admin\Desktop\MyNFTs\nft_0001.png", // You can see that "\" is highlighted in red.
```
* The bot may crash at the beginning when loading the MetaMask extension (Selenium module problem).
* Sometimes the bot indicates that the upload has failed while the NFT has been uploaded.
* The waiting time (`WebDriverWait().until()`) for the element to be clickable or visible is sometimes too short if your PC is slow and this raises an exception, so increase the time by 5 to 10 seconds:
```python
def element_clickable(self, element: str) -> None:
    """Click on element if it's clickable using Selenium."""
    WDW(self.driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, element))).click()

def element_visible(self, element: str, timer: int = 10):
    """Check if element is visible using Selenium."""
    return WDW(self.driver, timer).until(EC.visibility_of_element_located(
        (By.XPATH, element)))

def element_send_keys(self, element: str, keys: str) -> None:
    """Send keys to element if it's visible using Selenium."""
    try:
        WDW(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, element))).send_keys(keys)
    except TE:
        # Some elements are not visible but are still present.
        WDW(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, element))).send_keys(keys)
```

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
* ❌ Price setter for each NFT.
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
  * Open a command prompt in repository folder and type:
```
pip install -r requirements.txt
```

* ### Configuration of bot:

  * Download and install [Google Chrome](https://www.google.com/intl/en_en/chrome/).
  * Download the [ChromeDriver executable](https://chromedriver.chromium.org/downloads) that is compatible with the actual version of your Google Chrome browser and your OS (Operating System). Refer to: _[What version of Google Chrome do I have?](https://www.whatismybrowser.com/detect/what-version-of-chrome-do-i-have)_
  * Extract the executable from the ZIP file and copy/paste it in the `assets/` folder of the repository. You may need to change the path of the file:
```python
class Opensea(object):
    """Main class of Opensea automatic uploader."""

    def __init__(self, password: str, recovery_phrase: str) -> None:
        """Get the password and the recovery_phrase from the text file."""
        # Get recovery phrase of Metamask wallet.
        self.recovery_phrase = recovery_phrase
        self.password = password  # Get new password.
        # Used files path.
        self.webdriver_path = 'assets/chromedriver.exe'             # <-- Edit this line and change the ".exe".
        self.metamask_extension_path = 'assets/MetaMask.crx'
        self.driver = self.webdriver()  # Start new webdriver.
        # Opensea URLs.
        self.login_url = 'https://opensea.io/login?referrer=%2Fasset%2Fcreate'
        self.create_url = 'https://opensea.io/asset/create'
```
  * **Not recommended:** Download a new version of MetaMask extension (version used for script: 10.1.1.0).
    * Add [Get CRX](https://chrome.google.com/webstore/detail/get-crx/dijpllakibenlejkbajahncialkbdkjc) extension to Chrome:
    * Go on [MetaMask](https://chrome.google.com/webstore/detail/metamask/nkbihfbeogaeaoehlefnkodbefgpgknn) Chrome Web Store webpage.
    * Click on "Get CRX" extension button on top right of your browser.
    * Then click on "Get CRX" button.
  * **Optional:** password and recovery phrase are asked when you run the bot.
    * Open the `assets/password.txt` file and write your MetaMask password.
    * Open the `assets/recovery_phrase.txt` file and write your recovery phrase.
  * Create your NFTs data file containing all details of each NFT. It can be a JSON, CSV or XLSX file. Save it in the data folder.  
    **[What structure should the files have?](https://github.com/maximedrn/opensea_automatic_uploader#data-files-structure)**

* ### Data files structure:

  * **CSV file:**

    * <strong>required value *</strong>
    * _default value_
          
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
            <td>C:/Users/Admin/Desktop/MyNFTs/nft_0001.png;</td>
         </tr>
         <tr>
            <td><strong>NFT Name *</strong></td>
            <td>String</td>
            <td>NFT #1;</td>
         </tr>
         <tr>
            <td>External Link</td>
            <td>String</td>
            <td>https://www.google.com/;</td>
         </tr>
         <tr>
            <td>Description</td>
            <td>String</td>
            <td>This is my first NFT.;</td>
         </tr>
         <tr>
            <td>Collection</td>
            <td>String</td>
            <td>My First NFT;</td>
         </tr>
         <tr>
            <td>Properties</td>
            <td>List[[String, String], ...]</td>
            <td>["Dog", "Male"];</td>
         </tr>
         <tr>
            <td>Levels</td>
            <td>List[[String, Integer, Integer], ...]</td>
            <td>[["Speed", 2, 5], ["Width", 1, 10]];</td>
         </tr>
         <tr>
            <td>Stats</td>
            <td>List[[String, Integer, Integer], ...]</td>
            <td>[["Strenght", 10, 100], ["Age", 1, 99]];</td>
         </tr>
         <tr>
            <td>Unlockable Content  
               <br><i>False</i>
            </td>
            <td>List[Boolean, String]</td>
            <td>[True, "Thank you for purchasing my NFT!"];</td>
         </tr>
         <tr>
            <td>Explicit And Sensitive Content  
               <br><i>False</i>
            </td>
            <td>Boolean</td>
            <td>True;</td>
         </tr>
         <tr>
            <td>Supply  
               <br><i>1</i>
            </td>
            <td>Integer</td>
            <td>5;</td>
         </tr>
         <tr>
            <td>Blockchain  
               <br><i>Ethereum</i>
            </td>
            <td>String</td>
            <td>Polygon</td>
         </tr>
      </tbody>
   </table>

   #### And it gives you something like [this](https://github.com/maximedrn/opensea_automatic_uploader/blob/master/data/csv_structure.csv):
 ```
   file_path; nft_name; external_link; description; collection; properties; levels; stats; unlockable_content; explicit_and_sensitive_content; supply; blockchain
   C:/Users/Admin/Desktop/MyNFTs/nft_0001.png; NFT #1; https://www.google.com/; This is my first NFT.; My First NFT; ["Dog", "Male"]; [["Speed", 2, 5], ["Width", 1, 10]]; [["Strenght", 10, 100], ["Age", 1, 99]]; [True, "Thank you for purchasing my NFT!"]; True; 5; Polygon
   required; required; ; ; ; ; ; ; ; ; ; # Remove this line.
   ```
        
  * **XLSX file (same as CSV)**:
    
    * <strong>required value *</strong>
    * _default value_

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
            <td>C:/Users/Admin/Desktop/MyNFTs/nft_0001.png</td>
         </tr>
         <tr>
            <td><strong>NFT Name *</strong></td>
            <td>String</td>
            <td>NFT #1</td>
         </tr>
         <tr>
            <td>External Link</td>
            <td>String</td>
            <td>https://www.google.com/</td>
         </tr>
         <tr>
            <td>Description</td>
            <td>String</td>
            <td>This is my first NFT.</td>
         </tr>
         <tr>
            <td>Collection</td>
            <td>String</td>
            <td>My First NFT</td>
         </tr>
         <tr>
            <td>Properties</td>
            <td>List[[String, String], ...]</td>
            <td>["Dog", "Male"]</td>
         </tr>
         <tr>
            <td>Levels</td>
            <td>List[[String, Integer, Integer], ...]</td>
            <td>[["Speed", 2, 5], ["Width", 1, 10]]</td>
         </tr>
         <tr>
            <td>Stats</td>
            <td>List[[String, Integer, Integer], ...]</td>
            <td>[["Strenght", 10, 100], ["Age", 1, 99]]</td>
         </tr>
         <tr>
            <td>Unlockable Content  
               <br><i>False</i>
            </td>
            <td>List[Boolean, String]</td>
            <td>[True, "Thank you for purchasing my NFT!"]</td>
         </tr>
         <tr>
            <td>Explicit And Sensitive Content  
               <br><i>False</i>
            </td>
            <td>Boolean</td>
            <td>True</td>
         </tr>
         <tr>
            <td>Supply  
               <br><i>1</i>
            </td>
            <td>Integer</td>
            <td>5</td>
         </tr>
         <tr>
            <td>Blockchain  
               <br><i>Ethereum</i>
            </td>
            <td>String</td>
            <td>Polygon</td>
         </tr>
      </tbody>
   </table>
        
   #### And it gives you something like [this](https://github.com/maximedrn/opensea_automatic_uploader/blob/master/data/xlsx_structure.xlsx):
   
   <br>
   <table>
      <tbody>
         <tr>
            <td>File Path</td>
            <td>NFT Name</td>
            <td>External Link</td>
            <td>Description</td>
            <td>Collection</td>
            <td>Properties</td>
            <td>Levels</td>
            <td>Stats</td>
            <td>Unlockable Content</td>
            <td>Explicit And Sensitive Content</td>
            <td>Supply</td>
            <td>Blockchain</td>
         </tr>
         <tr>
            <td>C:/Users/Admin/Desktop/MyNFTs/nft_0001.png</font></td>
            <td>NFT #1</font></td>
            <td>https://www.google.com/</td>
            <td>This is my first NFT.</td>
            <td>My First NFT</td>
            <td>[["Dog", "Male"], ["Cat", "Female"]]</td>
            <td>[["Speed", 2, 5], ["Width", 1, 10]]</td>
            <td>[["Strenght", 10, 100], ["Age", 1, 99]]</td>
            <td>[True, "Thank you for purchasing my NFT!"]</td>
            <td>True</td>
            <td>5</td>
            <td>Polygon</td>
         </tr>
      </tbody>
   </table>

  * **JSON file:**

    * <strong>required value *</strong>
    * _default value_  

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
            <td>"file_path": "C:/Users/Admin/Desktop/MyNFTs/nft_0001.png",</td>
         </tr>
         <tr>
            <td><strong>NFT Name *</strong></td>
            <td>String</td>
            <td>"nft_name": "NFT #1",</td>
         </tr>
         <tr>
            <td>External Link</td>
            <td>String</td>
            <td>"external_link": "https://www.google.com/",</td>
         </tr>
         <tr>
            <td>Description</td>
            <td>String</td>
            <td>"description": "This is my first NFT.",</td>
         </tr>
         <tr>
            <td>Collection</td>
            <td>String</td>
            <td>"collection": "My First NFT",</td>
         </tr>
         <tr>
            <td>Properties</td>
            <td>List[[String, String], ...]</td>
            <td>"properties": [{"type": "Dog", "name": "Male"}, {"type": "Cat", "name": "Female"}],</td>
         </tr>
         <tr>
            <td>Levels</td>
            <td>List[[String, Integer, Integer], ...]</td>
            <td>"levels": [{"name": "Speed", "from": 2, "to": 5}, {"name": "Width", "from": 1, "to": 10}],</td>
         </tr>
         <tr>
            <td>Stats</td>
            <td>List[[String, Integer, Integer], ...]</td>
            <td>"stats": [{"name": "Strenght", "from": 10, "to": 100}, {"name": "Age", "from": 1, "to": 99}],</td>
         </tr>
         <tr>
            <td>Unlockable Content  
               <br><i>False</i>
            </td>
            <td>List[Boolean, String]</td>
            <td>"unlockable_content": [true, "Thank you for purchasing my NFT!"],</td>
         </tr>
         <tr>
            <td>Explicit And Sensitive Content  
               <br><i>False</i>
            </td>
            <td>Boolean</td>
            <td>"explicit_and_sensitive_content": true,</td>
         </tr>
         <tr>
            <td>Supply  
               <br><i>1</i>
            </td>
            <td>Integer</td>
            <td>"supply": 5,</td>
         </tr>
         <tr>
            <td>Blockchain  
               <br><i>Ethereum</i>
            </td>
            <td>String</td>
            <td>"blockchain": "Polygon",</td>
         </tr>
      </tbody>
   </table>
         
   #### And it gives you something like [this](https://github.com/maximedrn/opensea_automatic_uploader/blob/master/data/json_structure.json):
   ```json
   {
     "nft": [
       {
         "file_path": "C:/Users/Admin/Desktop/MyNFTs/nft_0001.png",
         "nft_name": "NFT #1",
         "external_link": "https://www.google.com/",
         "description": "This is my first NFT.",
         "collection": "My First NFT",
         "properties": [
           {
             "type": "Dog",
             "name": "Male"
           },
           {
             "type": "Cat",
             "name": "Female"
           }
         ],
         "levels": [
           {
             "name": "Speed",
             "from": 2,
             "to": 5
           },
           {
             "name": "Width",
             "from": 1,
             "to": 10
           }
         ],
         "stats": [
           {
             "name": "Strenght",
             "from": 10,
             "to": 100
           },
           {
             "name": "Age",
             "from": 1,
             "to": 99
           }
         ],
         "unlockable_content": [
           true,
           "Thank you for purchasing my NFT!"
         ],
         "explicit_and_sensitive_content": true,
         "supply": 5,
         "blockchain": "Polygon"
       },
       { // Remove this part below.
         "file_path": "required",
         "nft_name": "required",
         "external_link": "",
         "description": "",
         "collection": "",
         "properties": [],
         "levels": [],
         "stats": [],
         "unlockable_content": [],
         "explicit_and_sensitive_content": false,
         "supply": 1,
         "blockchain": "Ethereum"
       }
     ]
   }
   ```

## Set bot fully in the background:
```python
def webdriver(self):
   """Start webdriver and return state of it."""
   options = webdriver.ChromeOptions()  # Configure options for Chrome.
   options.add_extension(self.metamask_extension_path)  # Add extension.
   # options.add_argument("headless")  # Headless ChromeDriver.             # <-- Edit this line and remove the first "# ".
   options.add_argument("log-level=3")  # No logs is printed.
   options.add_argument("--mute-audio")  # Audio is muted.
   driver = webdriver.Chrome(self.webdriver_path, options=options)
   driver.maximize_window()  # Maximize window to reach all elements.
   return driver
```
