# Automatically and massively upload and list your non-fungible tokens on the OpenSea marketplace using Python Selenium.

_A Selenium Python bot to automatically and bulky upload and list your NFTs on OpenSea  
  All metadata integrated - Ethereum and Polygon supported - reCAPTCHA solver services included._  
➜ **[Version 1.7.13](#versions-1713)** (May 25, 2022).

If you like :green_heart: my work and this tool:
*  Do not hesitate to **fork :fork_and_knife:** this repository.
*  Do not hesitate to **add a star :star:** to this repository.

**Need help or have a specific request?  
Look at my offers on <a href="https://fr.fiverr.com/maximedrn/help-you-to-transfer-and-list-your-nfts-to-opensea">Fiverr <img src="https://user-images.githubusercontent.com/91475935/169694667-68824ed9-10a3-46ee-9fc1-23ec91496121.png" height="15px" /></a>.  
Contact me via [Telegram](https://t.me/maximedrn) or email me at [maxime_drean@yahoo.com](mailto:maxime_drean@yahoo.com).**

---

### **New**: Bypass reCAPTCHAs using this OpenSea exploit: **[reCAPTCHA Bypasser](#recaptcha-bypasser)**.  
Watch the videos ([1](https://www.youtube.com/watch?v=Xph_sjbWoyE) - [2](https://www.youtube.com/watch?v=dpPsd279XWk)) to see **how fast** the upload is with this exploit!  
Estimates: **400 NFTs per hour**, or an average of **10,000 NFTs in one day** with one process.  
**Try the demonstration version of this tool [here](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/releases/tag/Demonstration).**

https://user-images.githubusercontent.com/91475935/167429628-277de819-f3f8-44f7-86dc-33d11577d10b.mp4

---

# Table of contents

* **[Introduction](#introduction)**, video demonstration and useful links. 
* **[What does this bot do?](#what-does-this-bot-do)** What can I do with it? How easy does it make my job?
* **[Frequently asked questions](#frequently-asked-questions)** about this bot.
* **[Instructions](#instructions) to install and configure this bot**.
  * [Installation of Python](#installation-of-python), step by step learn how to install Python.
  * [Installation and configuration of the bot](#installation-and-configuration-of-the-bot), step by step learn how to download and configure this bot.
  * [Configuration of the reCAPTCHA solver using Yolov5x6](#configuration-of-the-recaptcha-solver-using-yolov5x6), a solver that use pre-trained models to solve reCAPTCHAs automatically.
  * [How to run the bot?](#how-to-run-the-bot) - discover different features of the bot.
* **[Metadata files structure](#metadata-files-structure).**
  * [Important things to know](#important-things-to-know) about empty details, JSON path format, etc.
  * ["Upload and sale" metadata file](#upload-and-sale-metadata-file) table of details.
  * ["Upload only" metadata file](#upload-only-metadata-file) table of details.
  * ["Sale only" metadata file](#sale-only-metadata-file) table of details.
  * [Explanation of the different details for the listing part](#explanation-of-the-different-details-for-the-listing-part).
* **[Useful tools to have for this bot](#useful-tools-to-have-for-this-bot).**
  * [Collection Scraper](#collection-scraper), scrape your collection easily, distinguish the duplicates, the missing ones, and the unique ones.
  * [Deletion](#deletion), massive deletion of NFTs from your account, can be combined with the Collection Scraper. 
  * [Generic File Maker](#generic-file-maker), easily generate your metadata file from only 21 details.
  * [Multiprocessing](#multiprocessing), upload and list your NFTs **two to five times faster**.
  * [reCAPTCHA Bypasser](#recaptcha-bypasser) (**demonstration: [1](https://www.youtube.com/watch?v=Xph_sjbWoyE) - [2](https://www.youtube.com/watch?v=dpPsd279XWk))**, use a new exploit to bypass reCAPTCHAs on OpenSea. Rediscover the upload on OpenSea before reCAPTCHAs.
  * [File Compatibilizer and Converter](#file-compatibilizer-and-converter), convert your file from a specific structure (**HashLips**) to another one and make your file compatible.
* **[Repository structure](#repository-structure)**, see how the file structure should be and which files can be deleted according to your choices.
* **[Changelog](#changelog-4)** and new features.


# Introduction

**[![How to upload 10k+ NFTs to OpenSea?](https://user-images.githubusercontent.com/91475935/166058768-1b7da2b4-59d4-4445-ad10-a725a31905fa.png)](https://www.youtube.com/watch?v=sM-YncZmZzc)**

**Please read the README file before using this tool, opening an issue or a discussion, or contacting me.**  
_You will certainly find a solution by **reading :book:** or consulting the issues already present._

* **Want to open an issue?**
   * Explain your problem in a few lines, accompanied by **images :framed_picture:** or a **video :clapper:**.
   * Provide an **excerpt from your metadata file :spiral_notepad:**.
   * Specify your **operating system :gear:** as well as the **version of Python :snake:** used and that of the bot.
* Make sure you have the latest version of the Python modules, browser and bot installed.
* Read the **pinned :pushpin: and opened issues**, see the structure of the metadata files.

**Useful links :link: and websites to consult before using this bot:**
* Sign up on [OpenSea](https://opensea.io/).
* Sign up on [MetaMask](https://metamask.io/).
* Sign up on [Coinbase](https://www.coinbase.com/join/dran_n7) (affiliate link).
* Sign up on [2Captcha](https://2captcha.com?from=13853725) (affiliate link).  
  **Paid service**: $2.99 per 1000 reCAPTCHAs.


# What does this bot do?

With this bot, **you can choose to upload, list or even both your non-fungible tokens** on the OpenSea marketplace.  

You just have to **create a metadata file** following the requested structure, JSON, CSV and XLSX (Excel file) formats are available.  
This file will include every detail for each NFT.  
Then, you just have to **launch the bot** and **select the action you want to perform**, as well as the metadata file created.  
Finally, **the bot will automate the tedious task of uploading or listing NFTs, one by one by hand, for several days**.  

* Absolutely **all upload details are supported**, you can add as many properties as you want.
* **All file formats** offered by OpenSea **are compatible**, including images, videos or even 3D models.
* **Ethereum and Polygon blockchains are supported**, and the switch between these two blockchains is also supported.
* In case of failure during an upload, a listing or when you only want to upload your NFTs on OpenSea, **a file is generated with details already filled** in or to be filled in.

You can see an example of collections transferred with this bot:
* **[Crypto Parrot](https://opensea.io/collection/crypto-parrot-nfts)**, transferred and listed before reCAPTCHAs.
* **[Rainbow Color Gradients](https://opensea.io/collection/rainbow-color-gradient)**, transferred and listed using the reCAPTCHA Bypasser.


# Frequently asked questions

### Should I be worried about using my wallet credentials?

According to **Rule #1** of the MetaMask "Safety Tips", it is requested to "**Never share your 12-word Secret Recovery Phrase (SRP) or private keys**". However, your wallet credentials are **only used** for the purpose of connecting to your wallet extension. The bot follows the procedure for the first connection to a wallet on a new browser (importing from a recovery phrase followed by creating a new password). Thus, none of this information is recovered, everything happens on your side. Moreover, you are free to choose whether or not to save your credentials in text files in the `assets/` folder.

### Which solver is the best?

It all depends on your choices and the equipment you have.
* If you have a powerful computer (running Windows or Linux) and you don't want to pay for a paid service, you should choose option number 2: the reCAPTCHA solver with Yolov5x6.
* If you don't have a powerful computer but don't mind paying for a service, you have 2 solutions.
  * The first one is option number 3 ([2Captcha](https://2captcha.com?from=13853725)) which is convenient if you want to upload a small collection at an affordable price.
  * The second option is option number 4 ([reCAPTCHA Bypasser](#recaptcha-bypasser)) which, in addition to speeding up the upload speed, allows you to upload as many collections as you want.
* If your computer is not powerful enough and you don't want to pay, choose the first option: manual resolution.

<table>
   <tbody>
      <tr>
         <td />
         <td><strong>reCAPTCHA bypasser</strong></td>
         <td><strong>2Captcha solver</strong></td>
         <td><strong>Yolov5x6 solver</strong></td>
         <td><strong>Manual resolution</strong></td>
      </tr>
      <tr>
         <td><strong>Solving speed</strong></td>
         <td><strong>Instant / 0 second</strong></td>
         <td>from 20 to 30 seconds</td>
         <td>from 20 to 30 seconds</td>
         <td>from 10 to 60 seconds</td>
      </tr>
      <tr>
         <td><strong>Upload time</strong></td>
         <td><strong>~ 6,5 seconds</strong></td>
         <td>From 30 to 40 seconds</td>
         <td>From 30 to 40 seconds</td>
         <td>More than 1 minute</td>
      </tr>
      <tr>
         <td><strong>Number of NFTs per hour</strong></td>
         <td><strong>Up to 400 NFTs</strong></td>
         <td>From 100 to 110 NFTs</td>
         <td>From 100 to 110 NFTs</td>
         <td>From 50 to 60 NFTs</td>
      </tr>
      <tr>
         <td><strong>Price</strong></td>
         <td>From $3 to $5 per month</td>
         <td>29.90$ per 10,000 NFTs</td>
         <td><strong>Free</strong></td>
         <td><strong>Free</strong></td>
      </tr>
      <tr>
         <td><strong>Automatic</strong></td>
         <td>✅</td>
         <td>✅</td>
         <td>✅</td>
         <td>❌</td>
      </tr>
      <tr>
         <td><strong>Works on any computer</strong></td>
         <td>✅</td>
         <td>✅</td>
         <td>❌</td>
         <td>✅</td>
      </tr>
      <tr>
         <td><strong>Unlimited</strong></td>
         <td>✅</td>
         <td>❌</td>
         <td>❌</td>
         <td>❌</td>
      </tr>
   </tbody>
</table>

### Is there an easy way to get the URLs of already uploaded NFTs?

A tool to retrieve URLs from NFTs is available. You can learn more about this tool [here](#collection-scraper).

### How to find missing and duplicates NFTs in my collection?

A tool to extract NFTs to get the missing and duplicates is available. You can learn more about this tool [here](#collection-scraper).
Then if you want to remove duplicates, you can use this tool [here](#deletion).

### Is there a quick way to create metadata file?

A tool to generate a complete metadata file from a single file is available. You can learn more about this tool [here](#generic-file-maker).


# Instructions

**[![How to install and setup the tool?](https://user-images.githubusercontent.com/91475935/166057944-fcf6a4a9-f0e4-407e-a918-64e345260f7c.png)](https://www.youtube.com/watch?v=jtERa6i9e1k)**

## Installation of Python

* Download and install [Python](https://www.python.org/) _(version 3.9.11 recommended)_ according to your operating system.
  * Make sure you add Python in your path by checking the checkbox when you run the installation.
* Check that your version of Python is correct by typing one of these commands in a command prompt:

  * ```
    python --version
    ```
  * ```
    python3 --version
    ```
  * ```
    py --version
    ```
* If pip is not installed by default with Python, install [pip](https://pip.pypa.io/en/stable/installation/) to be able to have needed Python modules.
* Verify that pip is correctly installed by typing one of thess commands in a command prompt:

  * ```
    pip --version
    ```
  * ```
    pip3 --version
    ```  
  
## Installation and configuration of the bot

* [Download this repository](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/archive/refs/heads/master.zip) or clone it by typing this command in your command prompt (it requires [Git](https://git-scm.com/downloads)):
    
    ```
    git clone https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale.git
    ```
* Extract the repository folder from the ZIP file, you should have a folder named  `opensea-automatic-bulk-upload-and-sale-master/`.
* Open a command prompt in the repository folder and type one of these commands (may require ``sudo`` on MacOS and Linux and administrator privileges for Windows):
    
  * ```
    pip install -r requirements.txt
    ```
  * ```
    pip3 install -r requirements.txt
    ```
  * ```
    python -m pip install -r requirements.txt
    ```
  * ```
    python3 -m pip install -r requirements.txt
    ```
  * ```
    py -m pip install -r requirements.txt
    ```
* Download and install [Google Chrome](https://www.google.com/intl/en_en/chrome/) and/or [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new/).
* Create your metadata file containing all details of each NFT. It can be a JSON, CSV or XLSX file. You can save it in the `data/` folder.  
  **[What structure should my metadata file have?](#metadata-files-structure)**

</details>

## Configuration of the reCAPTCHA solver using Yolov5x6

➜ _Yolov5x6 and RealESRGAN, ignore this if you use the 2Captcha solver, the [reCAPTCHA bypasser](#recaptcha-bypasser) or the manual solution._  
➜ _Only available for Windows and Linux users._

* You will **need a one of these graphics card (GPU)**:
  * GTX 1080.
  * RTX 2060, RTX 2070, RTX 2080.
  * RTX 2050, RTX 3060, RTX 3070, RTX 3080, RTX 3090.
  * Any Ti version of these graphics cards.
* Open a command prompt and type this command to check your CUDA version (it must be 11.6 or higher): 

  ```
  nvidia-smi
  ```
* If your CUDA version is earlier than 11.3, try to update it at the [NVIDIA website](https://developer.nvidia.com/cuda-downloads).
* Then type one of these commands to install PyTorch (may require ``sudo`` on Linux and administrator privileges for Windows):
  
  * ```
    pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio===0.11.0+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html
    ```
  * ```
    pip3 install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio===0.11.0+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html
    ```
  
  Or select one of the commands [here](https://pytorch.org/get-started/locally/) depending on your computer.  
  _Previous versions of PyTorch with older CUDA version: https://pytorch.org/get-started/previous-versions/_
* Install the required modules for the reCAPTCHA solver typing one of these commands (may require ``sudo`` on Linux and administrator privileges for Windows):

  * ```
    pip install -r requirements_recaptcha.txt
    ```
  * ```
    pip3 install -r requirements_recaptcha.txt
    ```
  * ```
    python -m pip install -r requirements_recaptcha.txt
    ```
  * ```
    python3 -m pip install -r requirements_recaptcha.txt
    ```
  * ```
    py -m pip install -r requirements_recaptcha.txt
    ```
  
## How to run the bot?

* Open a command prompt in the `opensea-automatic-bulk-upload-and-sale-master/` folder path.
* Type one of these commands to run the bot:
    
  * ```
    python main.py
    ```
  * ```
    python3 main.py
    ```
 * You should see this appear:

   ```diff
   + Created by Maxime Dréan.
   + Copyright © 2022 Maxime Dréan. All rights reserved.
   + Any distribution, modification or commercial use is strictly prohibited.

   Extension tools available here: https://maximedrn.gumroad.com/
   Tutorials on YouTube: https://www.youtube.com/channel/UCoqpR1OLbswIyQVatKBoGxA

   ! Choose a wallet:
   1 - MetaMask
   2 - Coinbase Wallet
   # Enter the number of the wallet: 1 or 2.
   Wallet: 

   # Enter the password of or a new password for your wallet.
   What is your wallet password?
   # Enter "y" or "n" depending on whether you want to save this detail or not.
   Do you want to save your password in a text file? (y/n)
   + Saved.
   ! Not saved.

   # Enter the recovery phrase of your wallet.
   What is your wallet recovery phrase?
   # Enter "y" or "n" depending on whether you want to save this detail or not.
   Do you want to save your recovery phrase in a text file? (y/n)
   + Saved.
   ! Not saved.

   # Enter the name of your account if you want to change your account on your wallet.
   What is your account number? (Press [ENTER] to ignore this step)
   # Enter "y" or "n" depending on whether you want to save this detail or not.
   Do you want to save your private key in a text file? (y/n)
   + Saved.
   ! Not saved.

   ! Choose an action to perform:
   1 - Upload and sell NFTs (18 details/NFT).
   2 - Upload NFTs (12 details/NFT).
   3 - Sell NFTs (9 details/NFT including 3 autogenerated).
   # Enter the number of the action: 1, 2 or 3.
   Action number:

   ! Choose a reCAPTCHA solver:
   1 - Manual solver.
   2 - Automatic solver using Yolov5.
   3 - Automatic solver using 2Captcha.
   # Enter the number of the solver you want to use: 1, 2 or 3.
   Action number:

   ! Choose a browser:
   1 - ChromeDriver (Google Chrome) - No headless mode.
       Must used in foreground, you see what's happening.
   2 - GeckoDriver (Mozilla Firefox)- Headless mode.
       Can be used in background while doing something else.
   # Enter the number of browser you want to use: 1 or 2.
   Browser:

   ! Choose your file:
   0 - Browse a file on PC.
   1 - data\json_structure_sale_only.json
   2 - data\json_structure_upload_and_sale.json
   3 - data\json_structure_upload_only.json
   6 - data\csv_structure_sale_only.csv
   7 - data\csv_structure_upload_and_sale.csv
   8 - data\csv_structure_upload_only.csv
   10 - data\xlsx_structure_sale_only.xlsx
   11 - data\xlsx_structure_upload_and_sale.xlsx
   12 - data\xlsx_structure_upload_only.xlsx
   # Enter the number of the metadata file you want to use - 0 if your file is not in the "data/" folder.
   File number:
   ```
* Then it will download a webdriver according to your choice and your browser version.
  * If the download fails, you can download the [ChromeDriver](https://chromedriver.chromium.org/downloads) according to your Google Chrome browser version, or the [GeckoDriver](https://github.com/mozilla/geckodriver/releases) according to your Mozilla Firefox browser version.
  * To know the version of your browser, consult these sites:
    * Google Chrome: [What version of Chrome do I have?](https://www.whatismybrowser.com/detect/what-version-of-chrome-do-i-have)
    * Mozilla Firefox: [What version of Firefox do I have?](https://www.whatismybrowser.com/detect/what-version-of-firefox-do-i-have)
 * If you selected the automatic reCAPTCHA solver using Yolov5, 2 files will be downloaded:
   * `realesrgan/RealESRGAN_x4plus.pth`: 63.9 MB. Available [here](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/releases/tag/RealESRGAN) if the download fails.
   * `yolov5/yolov5x6.pt`: 269 MB. Available [here](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/releases/tag/Yolov5x6) if the download fails.

# Metadata files structure

**[![How to create my metadata file?](https://user-images.githubusercontent.com/91475935/166058945-6b2bdbeb-db8d-4f87-929a-4e481818c957.png)](https://www.youtube.com/watch?v=67eRggoadOQ)**

**➜ Easily generate your metadata file using this [tool](#generic-file-maker).**

## Important things to know

* If you do not want to add details to the values not required (**all details are required**), leave:
  * **a blank cell** for XLSX files (Excel):
    <table>
     <tbody>
      <tr>
       <td>File Path</td>
       <td>NFT Name</td>
       <td>Description</td>
      </tr>
      <tr>
       <td>C:/Users/Admin/Desktop/NFT/nft_0001.png</td>
       <td>NFT #1</td>
       <td></td>
      </tr>
     </tbody>
    </table>

  * **a white space with two semicolons** for CSV files:
    ```csv
    file_path;; nft_name;; description;;
    C:/Users/Admin/Desktop/NFT/nft_0001.png;; NFT #1;; ;;
    ```
  * **an empty string** for JSON files: 
    ```json
    "file_path": "C:/Users/Admin/Desktop/NFT/nft_0001.png",
    "nft_name": "NFT #1",
    "description": "",
    ```

* **The file path should not contain a unique "\\". It can be a "/" or a "\\\\", as you can see for the JSON file *(it applies to all file formats)*:**
  
  ```json
  // You can use this format for your path:
  "file_path": "C:/Users/Admin/Desktop/MyNFTs/nft_0001.png",
  // or this one:
  "file_path": "C:\\Users\\Admin\\Desktop\\MyNFTs\\nft_0001.png",
  // but not this one (you can see that "\" is highlighted in red):
  "file_path": "C:\Users\Admin\Desktop\MyNFTs\nft_0001.png",
  ```

* <strong>Required values *</strong>
* Mandatory value in certain specified cases are in brackets
  
</details>

## "Upload and sale" metadata file

When you want to sell your NFTs, Opensea requires various details according to their Blockchain or supply number.  
**Note: The maximum duration of sale should be at most 6 months.**  

Make sure to **deposit Ethereum (ETH/WETH)** or **Polygon (MATIC)** on your wallet before proceeding to the sale. Otherwise the bot will cancel the sale. Opensea needs an **Ethereum** wallet with more than **0.05 ETH** or a **Polygon** wallet with a deposit of **any amount**. For **Ethereum**, you have to make a first listing manually before using this bot.

<table>
   <tbody>
      <tr>
         <td>Details</td>
         <td>Data Types</td>
         <td>Literal examples</td>
         <td>JSON examples</td>
         <td>CSV examples</td>
         <td>XLSX examples</td>
      </tr>
      <tr>
         <td><strong>File Path * </strong>(The preview is only for files that are not images)</td>
         <td>String or List</td>
         <td></td>
         <td>"file_path": "C:/Users/Admin/Desktop/NFT/nft_0001.png",
            <br>"file_path": ["C:/Users/Admin/Desktop/NFT/nft_0001.mp4", "C:/Users/Admin/Desktop/NFT/nft_0001-preview.png"],
         </td>
         <td>C:/Users/Admin/Desktop/NFT/nft_0001.png;;
            <br>["C:/Users/Admin/Desktop/NFT/nft_0001.mp4", "C:/Users/Admin/Desktop/NFT/nft_0001-preview.png"];;
         </td>
         <td>C:/Users/Admin/Desktop/NFT/nft_0001.png
            <br>["C:/Users/Admin/Desktop/NFT/nft_0001.mp4", "C:/Users/Admin/Desktop/NFT/nft_0001-preview.png"];;
         </td>
      </tr>
      <tr>
         <td><strong>NFT Name *</strong></td>
         <td>String</td>
         <td></td>
         <td>"nft_name": "NFT #1",</td>
         <td>NFT #1;;</td>
         <td>NFT #1</td>
      </tr>
      <tr>
         <td>External Link</td>
         <td>String</td>
         <td></td>
         <td>"external_link": "https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale",
            <br>"external_link": "",
         </td>
         <td>https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale;;</td>
         <td>https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale</td>
      </tr>
      <tr>
         <td>Description</td>
         <td>String</td>
         <td></td>
         <td>"description": "This is my first NFT.",
            <br>"description": "",
         </td>
         <td>This is my first NFT.;;</td>
         <td>This is my first NFT.</td>
      </tr>
      <tr>
         <td>Collection</td>
         <td>String</td>
         <td></td>
         <td>"collection": "My NFTs",
            <br>"collection": "my-nfts",
            <br>"collection": "",
         </td>
         <td>My NFTs;;
            <br>my-nfts;;
         </td>
         <td>My NFTs
            <br>my-nfts
         </td>
      </tr>
      <tr>
         <td>Properties</td>
         <td>List[[String, String], ...]
            <br>List[String, String]
         </td>
         <td>["type", "name"]
            <br>[["type", "name"], ["type", "name"]]
         </td>
         <td>"properties": [{ "type": "Dog", "name": "Male" }, { "type": "Cat", "name": "Female" }],
            <br>"properties": [{ "type": "Dog", "name": "Male" }],
            <br>"properties": "",
         </td>
         <td>[["Dog", "Male"], ["Cat", "Female"]];;
            <br>[["Dog", "Male"]];;
            <br>["Dog", "Male"];;
         </td>
         <td>[["Dog", "Male"], ["Cat", "Female"]]
            <br>[["Dog", "Male"]]
            <br>["Dog", "Male"]
         </td>
      </tr>
      <tr>
         <td>Levels</td>
         <td>List[[String, Integer, Integer], ...]
            <br>List[String, Integer, Integer]
         </td>
         <td>["name", value_from, value_to]
            <br>[["name", value_from, value_to], ["name", value_from, value_to]]
         </td>
         <td>"levels": [{ "name": "Speed", "from": 2, "to": 5 }, { "name": "Width", "from": 1, "to": 10 }],
            <br>"levels": [{ "name": "Speed", "from": 2, "to": 5 }],
            <br>"levels": "",
         </td>
         <td>[["Speed", 2, 5], ["Width", 1, 10]];;
            <br>[["Speed", 2, 5]];;
            <br>["Speed", 2, 5];;
         </td>
         <td>[["Speed", 2, 5], ["Width", 1, 10]]
            <br>[["Speed", 2, 5]]
            <br>["Speed", 2, 5]
         </td>
      </tr>
      <tr>
         <td>Stats</td>
         <td>List[[String, Integer, Integer], ...]
            <br>List[String, Integer, Integer]
         </td>
         <td>["name", value_from, value_to]
            <br>[["name", value_from, value_to], ["name", value_from, value_to]]
         </td>
         <td>"stats": [{ "name": "Strenght", "from": 10, "to": 100 }, { "name": "Age", "from": 1, "to": 99 }],
            <br>"stats": [{ "name": "Strenght", "from": 10, "to": 100 }],
            <br>"stats": "",
         </td>
         <td>[["Strenght", 10, 100], ["Age", 1, 99]];;
            <br>[["Strenght", 10, 100]];;
            <br>["Strenght", 10, 100];;
         </td>
         <td>[["Strenght", 10, 100], ["Age", 1, 99]]
            <br>[["Strenght", 10, 100]]
            <br>["Strenght", 10, 100]
         </td>
      </tr>
      <tr>
         <td>Unlockable Content</td>
         <td>List[Boolean, String]
            <br>List[Boolean]
            <br>Boolean
         </td>
         <td>[True, "unlockable_content"]
            <br>[False]
            <br>False
         </td>
         <td>"unlockable_content": [true, "Thank you for purchasing my NFT!"],
            <br>"unlockable_content": [false],
            <br>"unlockable_content": false,
            <br>"unlockable_content": "",
         </td>
         <td>[True, "Thank you for purchasing my NFT!"];;
            <br>[False];;
            <br>False;;
         </td>
         <td>[True, "Thank you for purchasing my NFT!"]
            <br>[False]
            <br>False
         </td>
      </tr>
      <tr>
         <td>Explicit And Sensitive Content</td>
         <td>Boolean</td>
         <td></td>
         <td>"explicit_and_sensitive_content": true,
            <br>"explicit_and_sensitive_content": false,
            <br>"explicit_and_sensitive_content": "",
         </td>
         <td>True;;
            <br>False;;
         </td>
         <td>True
            <br>False
         </td>
      </tr>
      <tr>
         <td>Supply</td>
         <td>Integer</td>
         <td></td>
         <td>"supply": 1,
            <br>"supply" : "",
         </td>
         <td>1;;</td>
         <td>1</td>
      </tr>
      <tr>
         <td>Blockchain</td>
         <td>String</td>
         <td></td>
         <td>"blockchain": "Polygon",
            <br>"blockchain" : "",
         </td>
         <td>Polygon;;</td>
         <td>Polygon</td>
      </tr>
      <tr>
         <td>Sale Type (only for Ethereum Blockchain and 1 supply)</td>
         <td>String</td>
         <td></td>
         <td>"sale_type": "Timed Auction",
            <br>"sale_type": "",
         </td>
         <td>Timed Auction;;</td>
         <td>Timed Auction</td>
      </tr>
      <tr>
         <td><strong>Price *</strong></td>
         <td>Float or Integer</td>
         <td></td>
         <td>"price": 5,
            <br>"price": 0.25,
         </td>
         <td>5;;
            <br>0.25;;
         </td>
         <td>5
            <br>0.25
         </td>
      </tr>
      <tr>
         <td>Method (only for "Timed Auction")</td>
         <td>List[String, Float]</td>
         <td>["method", price]
            <br>["method, ""]
         </td>
         <td>"method": ["Sell with declining price", 0.002],
            <br>"method": ["Sell to highest bidder", 0.05],
            <br>"method": ["Sell to highest bidder", ""],
            <br>"method": "",
         </td>
         <td>["Sell with declining price", 0.002];;
            <br>["Sell to highest bidder", 0.05];;
            <br>["Sell to highest bidder", ""];;
         </td>
         <td>["Sell with declining price", 0.002]
            <br>["Sell to highest bidder", 0.05]
            <br>["Sell to highest bidder", ""]
         </td>
      </tr>
      <tr>
         <td>Duration ("DD-MM-YYYY HH:MM")</td>
         <td>List[String, String]
            <br>List[String]
            <br>String
         </td>
         <td>["from_date", "to_date"]
            <br>["days/weeks/months"]
            <br>"days/weeks/months"
         </td>
         <td>"duration": ["01-01-2022 14:00", "01-04-2022 15:00"],
            <br>"duration": ["1 week"],
            <br>"duration": "1 week",
            <br>"duration": "",
         </td>
         <td>["01-01-2022 14:00", "01-04-2022 15:00"];;
            <br>["1 week"];;
            <br>1 week;;
         </td>
         <td>["01-01-2022 14:00", "01-04-2022 15:00"]
            <br>["1 week"]
            <br>1 week
         </td>
      </tr>
      <tr>
         <td>Specific Buyer</td>
         <td>List[Boolean, String]
            <br>[Boolean]
            <br>Boolean
         </td>
         <td>[True, "wallet"]
            <br>[False]
            <br>False
         </td>
         <td>"specific_buyer": [true, "0xDD135d5be0a23f6daAAE7D2d0580828c9e09402E"],
            <br>"specific_buyer": [false],
            <br>"specific_buyer": false,
            <br>"specific_buyer": "",
         </td>
         <td>[True, "0xDD135d5be0a23f6daAAE7D2d0580828c9e09402E"];;
            <br>[False];;
            <br>False;;
         </td>
         <td>[True, "0xDD135d5be0a23f6daAAE7D2d0580828c9e09402E"]
            <br>[False]
            <br>False
         </td>
      </tr>
      <tr>
         <td><strong>Quantity * (only for 1+ supplies)</strong></td>
         <td>Integer</td>
         <td></td>
         <td>"quantity": 4
            <br>"quantity": ""
         </td>
         <td>4</td>
         <td>4</td>
      </tr>
   </tbody>
</table>
 
And it gives you something like this: [JSON](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/blob/master/data/json_structure_upload_and_sale.json), [CSV](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/blob/master/data/csv_structure_upload_and_sale.csv), [XLSX (must be downloaded to view it)](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/blob/master/data/xlsx_structure_upload_and_sale.xlsx).
 
## "Upload only" metadata file

<details>
    <summary>Display the table.</summary>
    <br />
    <table>
        <tbody>
            <tr>
                <td>Details</td>
                <td>Data Types</td>
                <td>Literal examples</td>
                <td>JSON examples</td>
                <td>CSV examples</td>
                <td>XLSX examples</td>
            </tr>
            <tr>
                <td><strong>File Path *</strong> (The preview is only for files that are not images)</td>
                <td>String or List</td>
                <td></td>
                <td>"file_path": "C:/Users/Admin/Desktop/NFT/nft_0001.png",
                    <br>"file_path": ["C:/Users/Admin/Desktop/NFT/nft_0001.mp4", "C:/Users/Admin/Desktop/NFT/nft_0001-preview.png"],
                </td>
                <td>C:/Users/Admin/Desktop/NFT/nft_0001.png;;
                    <br>["C:/Users/Admin/Desktop/NFT/nft_0001.mp4", "C:/Users/Admin/Desktop/NFT/nft_0001-preview.png"];;
                </td>
                <td>C:/Users/Admin/Desktop/NFT/nft_0001.png
                    <br>["C:/Users/Admin/Desktop/NFT/nft_0001.mp4", "C:/Users/Admin/Desktop/NFT/nft_0001-preview.png"];;
                </td>
            </tr>
            <tr>
                <td><strong>NFT Name *</strong></td>
                <td>String</td>
                <td></td>
                <td>"nft_name": "NFT #1",</td>
                <td>NFT #1;;</td>
                <td>NFT #1</td>
            </tr>
            <tr>
                <td>External Link</td>
                <td>String</td>
                <td></td>
                <td>"external_link": "https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale",
                    <br>"external_link": "",
                </td>
                <td>https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale;;</td>
                <td>https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale</td>
            </tr>
            <tr>
                <td>Description</td>
                <td>String</td>
                <td></td>
                <td>"description": "This is my first NFT.",
                    <br>"description": "",
                </td>
                <td>This is my first NFT.;;</td>
                <td>This is my first NFT.</td>
            </tr>
            <tr>
                <td>Collection</td>
                <td>String</td>
                <td></td>
                <td>"collection": "My NFTs",
                    <br>"collection": "my-nfts",
                    <br>"collection": "",
                </td>
                <td>My NFTs;;
                    <br>my-nfts;;
                </td>
                <td>My NFTs
                    <br>my-nfts
                </td>
            </tr>
            <tr>
                <td>Properties</td>
                <td>List[[String, String], ...]
                    <br>List[String, String]
                </td>
                <td>["type", "name"]
                    <br>[["type", "name"], ["type", "name"]]
                </td>
                <td>"properties": [{ "type": "Dog", "name": "Male" }, { "type": "Cat", "name": "Female" }],
                    <br>"properties": [{ "type": "Dog", "name": "Male" }],
                    <br>"properties": "",
                </td>
                <td>[["Dog", "Male"], ["Cat", "Female"]];;
                    <br>[["Dog", "Male"]];;
                    <br>["Dog", "Male"];;
                </td>
                <td>[["Dog", "Male"], ["Cat", "Female"]]
                    <br>[["Dog", "Male"]]
                    <br>["Dog", "Male"]
                </td>
            </tr>
            <tr>
                <td>Levels</td>
                <td>List[[String, Integer, Integer], ...]
                    <br>List[String, Integer, Integer]
                </td>
                <td>["name", value_from, value_to]
                    <br>[["name", value_from, value_to], ["name", value_from, value_to]]
                </td>
                <td>"levels": [{ "name": "Speed", "from": 2, "to": 5 }, { "name": "Width", "from": 1, "to": 10 }],
                    <br>"levels": [{ "name": "Speed", "from": 2, "to": 5 }],
                    <br>"levels": "",
                </td>
                <td>[["Speed", 2, 5], ["Width", 1, 10]];;
                    <br>[["Speed", 2, 5]];;
                    <br>["Speed", 2, 5];;
                </td>
                <td>[["Speed", 2, 5], ["Width", 1, 10]]
                    <br>[["Speed", 2, 5]]
                    <br>["Speed", 2, 5]
                </td>
            </tr>
            <tr>
                <td>Stats</td>
                <td>List[[String, Integer, Integer], ...]
                    <br>List[String, Integer, Integer]
                </td>
                <td>["name", value_from, value_to]
                    <br>[["name", value_from, value_to], ["name", value_from, value_to]]
                </td>
                <td>"stats": [{ "name": "Strenght", "from": 10, "to": 100 }, { "name": "Age", "from": 1, "to": 99 }],
                    <br>"stats": [{ "name": "Strenght", "from": 10, "to": 100 }],
                    <br>"stats": "",
                </td>
                <td>[["Strenght", 10, 100], ["Age", 1, 99]];;
                    <br>[["Strenght", 10, 100]];;
                    <br>["Strenght", 10, 100];;
                </td>
                <td>[["Strenght", 10, 100], ["Age", 1, 99]]
                    <br>[["Strenght", 10, 100]]
                    <br>["Strenght", 10, 100]
                </td>
            </tr>
            <tr>
                <td>Unlockable Content</td>
                <td>List[Boolean, String]
                    <br>List[Boolean]
                    <br>Boolean
                </td>
                <td>[True, "unlockable_content"]
                    <br>[False]
                    <br>False
                </td>
                <td>"unlockable_content": [true, "Thank you for purchasing my NFT!"],
                    <br>"unlockable_content": [false],
                    <br>"unlockable_content": false,
                    <br>"unlockable_content": "",
                </td>
                <td>[True, "Thank you for purchasing my NFT!"];;
                    <br>[False];;
                    <br>False;;
                </td>
                <td>[True, "Thank you for purchasing my NFT!"]
                    <br>[False]
                    <br>False
                </td>
            </tr>
            <tr>
                <td>Explicit And Sensitive Content</td>
                <td>Boolean</td>
                <td></td>
                <td>"explicit_and_sensitive_content": true,
                    <br>"explicit_and_sensitive_content": false,
                    <br>"explicit_and_sensitive_content": "",
                </td>
                <td>True;;
                    <br>False;;
                </td>
                <td>True
                    <br>False
                </td>
            </tr>
            <tr>
                <td><strong>Supply *</strong></td>
                <td>Integer</td>
                <td></td>
                <td>"supply": 1,</td>
                <td>1;;</td>
                <td>1</td>
            </tr>
            <tr>
                <td><strong>Blockchain *</strong></td>
                <td>String</td>
                <td></td>
                <td>"blockchain": "Polygon"</td>
                <td>Polygon</td>
                <td>Polygon</td>
            </tr>
        </tbody>
    </table>
</details>
 
And it gives you something like this: [JSON](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/blob/master/data/json_structure_upload_only.json), [CSV](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/blob/master/data/csv_structure_upload_only.csv), [XLSX (must be downloaded to view it)](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/blob/master/data/xlsx_structure_upload_only.xlsx).
  
## "Sale only" metadata file

If you have already uploaded your NFTs with this bot, a file has been generated containing the URL, the Blockchain and the supply number of each NFT. You have to complete it with sale values.
  
When you want to sell your NFTs, Opensea requires various details according to their Blockchain or supply number.  
**Note: The maximum duration of sale should be at most 6 months.**  

Make sure to **deposit Ethereum (ETH/WETH)** or **Polygon (MATIC)** on your wallet before proceeding to the sale. Otherwise the bot will cancel the sale. Opensea needs an **Ethereum** wallet with more than **0.05 ETH** or a **Polygon** wallet with a deposit of **any amount**. For **Ethereum**, you have to make a first listing manually before using this bot.

<details>
    <summary>Display the table.</summary>
    <br />
    <table>
        <tbody>
            <tr>
                <td>Details</td>
                <td>Data Types</td>
                <td>Literal examples</td>
                <td>JSON examples</td>
                <td>CSV examples</td>
                <td>XLSX examples</td>
            </tr>
            <tr>
                <td><strong>NFT URL * </strong></td>
                <td>String</td>
                <td></td>
                <td>"nft_url": "https://opensea.io/assets/matic/...",</td>
                <td>https://opensea.io/...;;</td>
                <td>https://opensea.io/assets/matic/...</td>
            </tr>
            <tr>
                <td><strong>Supply *</strong></td>
                <td>Integer</td>
                <td></td>
                <td>"supply": 1,</td>
                <td>1;;</td>
                <td>1</td>
            </tr>
            <tr>
                <td><strong>Blockchain *</strong></td>
                <td>String</td>
                <td></td>
                <td>"blockchain": "Polygon",</td>
                <td>Polygon;;</td>
                <td>Polygon</td>
            </tr>
            <tr>
                <td>Sale Type (only for Ethereum Blockchain and 1 supply)</td>
                <td>String</td>
                <td></td>
                <td>"sale_type": "Timed Auction",
                    <br>"sale_type": "",
                </td>
                <td>Timed Auction;;</td>
                <td>Timed Auction</td>
            </tr>
            <tr>
                <td><strong>Price *</strong></td>
                <td>Float or Integer</td>
                <td></td>
                <td>"price": 5,
                    <br>"price: 0.25,
                </td>
                <td>5;;
                    <br>0.25;;
                </td>
                <td>5
                    <br>0.25
                </td>
            </tr>
            <tr>
                <td>Method (only for "Timed Auction")</td>
                <td>List[String, Float]</td>
                <td>["method", price]
                    <br>["method, ""]
                </td>
                <td>"method": ["Sell with declining price", 0.002],
                    <br>"method": ["Sell to highest bidder", 0.05],
                    <br>"method": ["Sell to highest bidder", ""],
                    <br>"method": "",
                </td>
                <td>["Sell with declining price", 0.002];;
                    <br>["Sell to highest bidder", 0.05];;
                    <br>["Sell to highest bidder", ""];;
                </td>
                <td>["Sell with declining price", 0.002]
                    <br>["Sell to highest bidder", 0.05]
                    <br>["Sell to highest bidder", ""]
                </td>
            </tr>
            <tr>
                <td>Duration ("DD-MM-YYYY HH:MM")</td>
                <td>List[String, String]
                    <br>List[String]
                    <br>String
                </td>
                <td>["from_date", "to_date"]
                    <br>["days/weeks/months"]
                    <br>"days/weeks/months"
                </td>
                <td>"duration": ["01-01-2022 14:00", "01-04-2022 15:00"],
                    <br>"duration": ["1 week"],
                    <br>"duration": "1 week",
                    <br>"duration": "",
                </td>
                <td>["01-01-2022 14:00", "01-04-2022 15:00"];;
                    <br>["1 week"];;
                    <br>1 week;;
                </td>
                <td>["01-01-2022 14:00", "01-04-2022 15:00"]
                    <br>["1 week"]
                    <br>1 week
                </td>
            </tr>
            <tr>
                <td>Specific Buyer</td>
                <td>List[Boolean, String]
                    <br>[Boolean]
                    <br>Boolean
                </td>
                <td>[True, "wallet"]
                    <br>[False]
                    <br>False
                </td>
                <td>"specific_buyer": [true, "0xDD135d5be0a23f6daAAE7D2d0580828c9e09402E"]
                    <br>"specific_buyer": [false]
                    <br>"specific_buyer": false,
                    <br>specific_buyer": "",
                </td>
                <td>[True, "0xDD135d5be0a23f6daAAE7D2d0580828c9e09402E"];;
                    <br>[False];;
                    <br>False;;
                </td>
                <td>[True, "0xDD135d5be0a23f6daAAE7D2d0580828c9e09402E"]
                    <br>[False]
                    <br>False
                </td>
            </tr>
            <tr>
                <td><strong>Quantity * (only for 1+ supplies)</strong></td>
                <td>Integer</td>
                <td></td>
                <td>"quantity": 4
                    <br>"quantity": ""
                </td>
                <td>4</td>
                <td>4</td>
            </tr>
        </tbody>
    </table>
</details>

And it gives you something like this: [JSON](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/blob/master/data/json_structure_sale_only.json), [CSV](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/blob/master/data/csv_structure_sale_only.csv), [XLSX (must be downloaded to view it)](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/blob/master/data/xlsx_structure_sale_only.xlsx).

## Explanation of the different details for the listing part

<table>
    <tbody>
        <tr>
            <td colspan="15">Ethereum</td>
            <td colspan="7">Polygon</td>
        </tr>
        <tr>
            <td colspan="11">Supply number equal to 1</td>
            <td colspan="4">Supply number higher than 1</td>
            <td colspan="3">Supply number equal to 1</td>
            <td colspan="4">Supply number higher than 1</td>
        </tr>
        <tr>
            <td colspan="3">Fixed Price</td>
            <td colspan="8">Timed Auction</td>
            <td colspan="4"></td>
            <td colspan="3"></td>
            <td colspan="4"></td>
        </tr>
        <tr>
            <td colspan="3"></td>
            <td colspan="4">Sell to highest bidder</td>
            <td colspan="4">Sell with declining price</td>
            <td colspan="4"></td>
            <td colspan="3"></td>
            <td colspan="4"></td>
        </tr>
        <tr>
            <td><strong>Price</strong> (ETH)</td>
            <td><strong>Duration</strong> (from a date to an other date <strong>or</strong> 1 day, 3 days, 1 week, 1 month)</td>
            <td>Reserve for a <strong>specific buyer</strong></td>
            <td><strong>Price</strong> (ETH)</td>
            <td><strong>Duration</strong> (from a date to an other date <strong>or</strong> 1 day, 3 days, 1 week)</td>
            <td><i>(Optional)</i> <strong>Reserved Price</strong> (WETH) greater than 1 WETH and greater than the <strong>Starting Price</strong>.</td>
            <td>Reserve for a <strong>specific buyer</strong></td>
            <td><strong>Starting Price</strong> (ETH)</td>
            <td><strong>Duration</strong> (from a date to an other date or 1 day, 3 days, 1 week)</td>
            <td><strong>Ending Price</strong> (ETH) less than the <strong>Starting Price</strong>.</td>
            <td>Reserve for a <strong>specific buyer</strong></td>
            <td><strong>Quantity</strong></td>
            <td><strong>Price</strong> (ETH)</td>
            <td><strong>Duration</strong> (from a date to an other date <strong>or</strong> 1 day, 3 days, 1 week, 1 month)</td>
            <td>Reserve for a <strong>specific buyer</strong></td>
            <td><strong>Price</strong> (ETH)</td>
            <td><strong>Duration</strong> (from a date to an other date <strong>or</strong> 1 day, 3 days, 1 week, 1 month)</td>
            <td>Reserve for a <strong>specific buyer</strong></td>
            <td><strong>Quantity</strong></td>
            <td><strong>Price</strong> (ETH)</td>
            <td><strong>Duration</strong> (from a date to an other date <strong>or</strong> 1 day, 3 days, 1 week, 1 month)</td>
            <td>Reserve for a <strong>specific buyer</strong></td>
        </tr>
    </tbody>
</table>
  
</details>

# Useful tools to have for this bot

All these tools are not free and are only add-ons. You can still use the bot without these tools.  
The complete list of tools is available on [Gumroad](https://maximedrn.gumroad.com/).  
If you are not able to pay by Paypal or credit card on Gumroad, contact me on Telegram. You will be able to make a payment by cryptocurrency.

## Collection Scraper

[![Collection Scraper](https://user-images.githubusercontent.com/91475935/166142344-cd0bd61e-6ea5-45fc-bdd6-a007c991ed19.png)](https://maximedrn.gumroad.com/l/opensea-collection-scraper)

With this OpenSea collection scraper, you can retrieve the entire URLs of the NFTs of a collection automatically.  
It facilitates the listing of NFTs already uploaded to OpenSea before, without the help of the latter.  

The bot takes care of sorting among the NFTs by creating different files compatible with the "Sale only" part of the bot.  
Thus a "**full**" file containing all NFTs, a "**unique**" file containing each NFT individually based on their names, a "**duplicate**" file containing all duplicated NFTs of the collection and a "**missing**" file containing all missing NFTs will be created, and these in all formats compatible with the bot (JSON, CSV and XLSX).  
**Purchase this tool - [Collection Scraper](https://maximedrn.gumroad.com/l/opensea-collection-scraper).**

<details>
  <summary>View this section.</summary>
  <br />

### Installation

* Download and install [Node.js](https://nodejs.org/) LTS version.
* Extract the repository folder from the ZIP file, you should have a folder named `opensea-collection-scraper/`.
* Open a command prompt in the repository folder and type one of these commands (may require sudo on MacOS and Linux and administrator privileges for Windows):

  * ```
    pip install -r requirements.txt
    ```
  * ```
    pip3 install -r requirements.txt
    ```
  * ```
    python -m pip install -r requirements.txt
    ```
  * ```
    python3 -m pip install -r requirements.txt
    ```
  * ```
    py -m pip install -r requirements.txt
    ```
* Still in your command prompt, type this command (may require sudo on MacOS and Linux and administrator privileges for Windows - a `node_modules/` folder should be created):
  
  ```
  npm install
  ```
  
### Run the bot

* Open a command prompt in the `opensea-collection-scraper/` folder path and type one of these commands to run the bot:

  * ```
    python scraper.py
    ```
  * ```
    python3 scraper.py
    ```
* Enter the name of your collection, based on the collection URL: `https://opensea.io/collection/crypto-parrot-nfts` ➜ `crypto-parrot-nfts`.
* JSON, CSV and XLSX files will be generated and stored in the `data/` folder of the repository.  

### Changelog

* **Version 1.3.0:**
  * Major fixes.
  * The collection limit is 20,000 NFTs maximum.
  * The bot now scrapes twice.
* **Version 1.2.0:**
  * Correction of missing name in CSV files.
  * Correction of the creation of missing files.
  * Improved functioning of the duplicate detector.
* **Version 1.1.0:**
  * Adding the creation of a file containing duplicates.
  * Added the creation of a file containing the missing.
  * Added the name of the NFTs in the files for sale.
* **Version 1.0.0:**
  * Initial commit.

</details>

## Deletion

[![Deletion](https://user-images.githubusercontent.com/91475935/167246640-f4a7764f-37ae-46e6-9d5a-91b100eb6d1c.png)](https://maximedrn.gumroad.com/l/opensea-deletion)

With this Deletion tool, you can massively remove NFTs from your account. All you have to do is create a file containing the URL of the NFTs you want to delete, then launch the main bot and select the fourth option. It is even easier if you have the [Collection Scraper](#collection-scraper) tool, which automatically creates a file compatible with this tool.

**Purchase this tool - [Deletion](https://maximedrn.gumroad.com/l/opensea-deletion).**

<details>
  <summary>View this section.</summary>
  <br />

### Installation and run the bot

* **Make sure you have version 1.7.5 or higher.**
* Extract the file from the ZIP file, you should have a file named `delete.py`.
* Navigate to the "Upload and Sale" bot repository, and place this file in this directory: `opensea-automatic-bulk-upload-and-sale/app/services/processes/delete.py`.
* Start the main bot and at action select the 4th option.
  
### File structure

**This works exactly like a "Sale Only" file where only the first value will be taken into account (`nft_url`).**

<table>
   <tbody>
      <tr>
         <td>Details</td>
         <td>Data Types</td>
         <td>Literal examples</td>
         <td>JSON examples</td>
         <td>CSV examples</td>
         <td>XLSX examples</td>
      </tr>
      <tr>
         <td><strong>NFT URL * </strong></td>
         <td>String</td>
         <td></td>
         <td>"nft_url": "https://opensea.io/assets/matic/..."</td>
         <td>https://opensea.io/...</td>
         <td>https://opensea.io/assets/matic/...</td>
      </tr>
   </tbody>
</table>

### Changelog

* **Version 1.0.0:**
  * Initial commit.

</details>
  
## Generic File Maker

[![Generic File Maker](https://user-images.githubusercontent.com/91475935/166142331-6afe4920-f34a-47c1-9dfc-4e8ffd3ae57a.png)](https://maximedrn.gumroad.com/l/opensea-generic-file)

With this OpenSea collection scraper, you can generate a whole file from a generic file or modify a file by replacing massively some values by others.  
You just have to fill a simple generic file with 21 details (18 for NFTs and 3 for formatting and file parameters) and run the script.  
Your file will be generated with common values for all your NFTs.  
It faciliates the creation of your metadata file.  
**Purchase this tool - [Generic File Maker](https://maximedrn.gumroad.com/l/opensea-generic-file).**

<details>
  <summary>View this section.</summary>
  <br />

### Installation

* Extract the repository folder from the ZIP file, you should have a folder named `opensea-generic-file/`.
* Open a command prompt in the repository folder and type one of these commands (may require sudo on MacOS and Linux and administrator privileges for Windows):

  * ```
    pip install -r requirements.txt
    ```
  * ```
    pip3 install -r requirements.txt
    ```
  * ```
    python -m pip install -r requirements.txt
    ```
  * ```
    python3 -m pip install -r requirements.txt
    ```
  * ```
    py -m pip install -r requirements.txt
    ```
  
### Run the bot

* Open a command prompt in the `opensea-generic-file/` folder path and type one of these commands to run the bot:

  * ```
    python generic.py
    ```
  * ```
    python3 generic.py
    ```
* You should see this appear:
  ```diff
  + Created by Maxime Dréan.
  + Copyright © 2022 Maxime Dréan. All rights reserved.
  + Any distribution, modification or commercial use is strictly prohibited.

  ! Choose an action to perform:
  1 - Duplicate from existing file.
  2 - Generate a new file.
  # Enter the number of the action: 1 (if you already have a metadata file) or 2 (if you want to create a new file).
  Action number:

  ! Choose your generic file:
  0 - Browse a file on PC.
  1 - generic\generic-file-blank.json
  2 - generic-file-example.json
  # Enter the number of the generic file you want to use.
  File number:

  ! Convert to/file type:
  1 - Upload & sale (18 details).
  2 - Upload (12 details).
  3 - Sale (9 details).
  # Enter the number of the file structure.
  Action number:

  # This part appears if you choose "Duplicate from an existing file".
  ! Choose your data file:
  0 - Browse a file on PC.
  1 - data/_metadata.json
  # Enter the number of the metadata file you want to use - 0 if your file is not in the "data/" folder.
  File number:

  Creating file. Done.
  + Saved in data/b2ef894e.json.
  ```

### Changelog

* **Version 1.1.0:**
  * Added support for preview file in the generic file.
  * Fixed the problem of unlockable content to false when set to true in the data file.
* **Version 1.0.0:**
  * Initial commit.

### How to complete the generic file?

* In the details part of the generic file, you have to complete with the value you want to put in your metadata file.

* What does the value "`incrementation`" mean?  
  You may have different file names, URLs or descriptions for each of your NFTs, so these details will be different for each NFT.
  * `number`: it will use a numeric value for incrementing (1, 2, 3, 4, etc).
  * ``letter``: it will use the alphabet for incrementing (`A` to `Z`, then `AA` to `AZ`, etc).
  
  **This value (number or letter) will be added wherever you place `{}` in your detail.**

* What does the "format" value mean?  
  This is the way `"increment": "number",` will work.
  * `0` : default value, numbers will be incremented in a basic way.
  * `-1`: it will add a specific number of digits depending on the number of NFTs (10000 NFTs ➜ `00001`, `00002`, etc).
  * Any strictly positive number: number of digits (3 digits ➜ `001`, ... `100`, etc).

* Settings part:
  * `overwrite`: it will overwrite the entire contents of a metadata file.
  * `overwrite_empty`: it will overwrite the details of a metadata file only if they are as default value.
  * `append`: it will append the value of any list of dictionary details (properties, levels, stats).

</details>

## Multiprocessing

[![Multiprocessing](https://user-images.githubusercontent.com/91475935/166142605-8ce3d606-4b12-4b95-8f6d-20358dd41904.png)](https://maximedrn.gumroad.com/l/opensea-multiprocessing)


With this multi-processor tool, you can download and list your NFTs **two to five times faster**.
It splits your file into two subfiles, one taking the odd indexes in the metadata file and the other taking the even indexes.  
Then two command prompts open and work like the main bot but at the same time.  

Note: it requires a fairly powerful computer (a minimum of 8GB of RAM and a processor with a minimum of 2 cores).  
If your computer has some mismatch with the main bot, do not buy this tool.

**Purchase this tool - [Multiprocessing](https://maximedrn.gumroad.com/l/opensea-multiprocessing).**

<details>
  <summary>View this section.</summary>
  <br />

### Installation

* **Make sure you have version 1.7.10 or higher.**
* Extract the 2 files from the ZIP file, you should have a file named `multiprocessing.py` and another named `task.py`.
* Navigate to the "Upload and Sale" bot repository, and place these two files in the parent directory (`opensea-automatic-upload-and-sale/`).
  
### Run the bot

* Open a command prompt in the repository folder (same as the main bot) and type one of these commands to run the bot:

  * ```
    python multiprocessing.py
    ```
  * ```
    python3 multiprocess.py
    ```
* Select your choices as in the main bot.
* When two command prompts are open, you can close the `multiprocessing.py` tab.
* Now the bot runs multiple instances and upload/list or both your NFTs.

### Changelog

* **Version 1.1.0:**
  * You can now choose the amount of processes you want to run simultaneously (between 1 and 5).
  * Remove the output on save that make the process slower.
* **Version 1.0.0:**
  * Initial commit.

</details>

## reCAPTCHA Bypasser

[![reCAPTCHA Bypasser](https://user-images.githubusercontent.com/91475935/167246654-ffd2059a-e1da-41b2-b152-b81486f1f0e3.png)](https://maximedrn.gumroad.com/l/opensea-no-recaptcha)
**Demonstration videos available: [1](https://www.youtube.com/watch?v=Xph_sjbWoyE) - [2](https://www.youtube.com/watch?v=dpPsd279XWk)**.

With this tool, you can upload your NFTs without reCAPTCHA on OpenSea. It uses an exploit that bypass the reCAPTCHA.  
The upload speed is such that there would be no reCAPTCHA. Rediscover OpenSea before reCAPTCHAs!  
Up to 400 NFTs per hour and much more with the [Multiprocessing tool](#multiprocessing).  
**Purchase this tool - [reCAPTCHA Bypasser](https://maximedrn.gumroad.com/l/opensea-no-recaptcha).**

<details>
  <summary>View this section.</summary>
  <br />

### Installation and run the bot

* **Make sure you have version 1.7.3 or higher.**
* Extract the file from the ZIP file, you should have a file named `no-captcha.py`.
* Place it in this directory: `opensea-automatic-bulk-upload-and-sale/app/services/solvers/`.
* Start the main bot and at reCAPTCHA select the 4th option.
  
</details>
  
## File Compatibilizer and Converter

[![File Compatibilizer](https://user-images.githubusercontent.com/91475935/166142304-b457f939-375e-452d-b4b7-1fa47db0adc3.png)](https://maximedrn.gumroad.com/l/opensea-file-compatibilizer)

With this file compatibilizer, you can convert a metadata file of one specific type into another (`Upload` into `Upload and Sale`, into `Sale` and vice versa).
In addition, it organizes the details in a specific order to be compatible with the bot. You can convert a folder containing HashLips JSON files into a single compatible file.  
**Purchase this tool - [File Compatibilizer](https://maximedrn.gumroad.com/l/opensea-file-compatibilizer).**

<details>
  <summary>View this section.</summary>
  <br />

### Installation

* Extract the repository folder from the ZIP file, you should have a folder named `opensea-file-compatibilizer/`.
* Open a command prompt in the repository folder and type one of these commands (may require sudo on MacOS and Linux and administrator privileges for Windows):

  * ```
    pip install -r requirements.txt
    ```
  * ```
    pip3 install -r requirements.txt
    ```
  * ```
    python -m pip install -r requirements.txt
    ```
  * ```
    python3 -m pip install -r requirements.txt
    ```
  * ```
    py -m pip install -r requirements.txt
    ```
  
### Run the bot

* Open a command prompt in the `opensea-file-compatibilizer/` folder path and type one of these commands to run the bot:

  * ```
    python compatibilizer.py
    ```
  * ```
    python3 compatibilizer.py
    ```
* Choose your file.
* Select its file type to arrange the details in a specific order or the type in which you want to convert it.
* The file will be saved in the `data/` folder.

### Changelog

* **Version 1.0.0:**
  * Initial commit.

</details>


# Repository structure

Absolutely all files must be present for the bot to work properly. Some files are available by purchasing external tools, these allow to facilitate the task of uploading or listing on OpenSea or offer new features.

<details>
  <summary>Display the repository structure.</summary>
  <br />

```css
opensea-automatic-upload-and-sale-master
├── .github  /* Can be removed. */
│   ╰── workflows  /* Can be removed. */
│       ├── codeql-analysis.yml  /* Can be removed. */
│       ╰── stale_issues.yml  /* Can be removed. */
├── app
│   ├── common
│   │   ├── __init__.py
│   │   ├── reader.py
│   │   ├── save.py
│   │   ╰── structure.py
│   ├── services
│   │   ├── processes
│   │   │   ├── __init__.py
│   │   │   ├── login.py
│   │   │   ├── delete.py  /* Available in the "Deletion" tool. */
│   │   │   ├── sale.py
│   │   │   ╰── upload.py
│   │   ├── solvers
│   │   │   ├── __init__.py
│   │   │   ├── no_captcha.py  /* Can be removed if you don't want to use the reCAPTCHA exploit. */
│   │   │   ├── recaptcha_callback.js  /* Can be removed if you don't want to use the 2Captcha solver. */
│   │   │   ├── recaptcha.py  /* Can be removed if you don't want to use the Yolov5x6 reCAPTCHA solver. */
│   │   │   ├── solver.py
│   │   │   ╰── two_captcha.py  /* Can be removed if you don't want to use the 2Captcha solver. */
│   │   ├── wallets
│   │   │   ├── __init__.py
│   │   │   ├── coinbase_wallet.py  /* Can be removed if you don't want to use Coinbase Wallet. */
│   │   │   ├── metamask.py  /* Can be removed if you don't want to use MetaMask. */
│   │   │   ╰── wallet.py
│   │   ├── __init__.py
│   │   ╰── webdriver.py
│   ├── utils
│   │   ├── __init__.py
│   │   ├── colors.py
│   │   ├── const.py
│   │   ├── func.py
│   │   ├── user.py
│   │   ╰── values.py
│   ╰── __init__.py
├── assets
│   ├── classes.json  /* Can be removed if you don't want to use the Yolov5x6 reCAPTCHA solver. */
│   ├── CoinbaseWallet.crx  /* Can be removed if you don't want to use the Coinbase Wallet extension. */
│   ├── MetaMask.crx  /* Can be removed if you don't want to use the MetaMask wallet with Google Chrome. */
│   ╰── MetaMask.xpi  /* Can be removed if you don't want to use the MetaMask wallet with Mozilla Firefox. */
├── data
│   ├── examples  /* Can be removed. */
│   │   ├── csv_structure_sale_only.csv
│   │   ├── csv_structure_upload_and_sale.csv
│   │   ├── csv_structure_upload_only.csv
│   │   ├── json_structure_sale_only.json
│   │   ├── json_structure_upload_and_sale.json
│   │   ├── json_structure_upload_only.json
│   │   ├── xlsx_structure_sale_only.xlsx
│   │   ├── xlsx_structure_upload_and_sale.xlsx
│   │   ╰── xlsx_structure_upload_only.xlsx
│   ├── csv_structure_sale_only.csv  /* Can be removed. */
│   ├── csv_structure_upload_and_sale.csv  /* Can be removed. */
│   ├── csv_structure_upload_only.csv  /* Can be removed. */
│   ├── json_structure_sale_only.json  /* Can be removed. */
│   ├── json_structure_upload_and_sale.json  /* Can be removed. */
│   ├── json_structure_upload_only.json  /* Can be removed. */
│   ├── xlsx_structure_sale_only.xlsx  /* Can be removed. */
│   ├── xlsx_structure_upload_and_sale.xlsx  /* Can be removed. */
│   ╰── xlsx_structure_upload_only.xlsx  /* Can be removed. */
├── realesrgan  /* Can be removed if you don't want to use the Yolov5x6 reCAPTCHA solver. */
│   ├── archs
│   │   ├── __init__.py
│   │   ├── discriminator_arch.py
│   │   ╰── srvgg_arch.py
│   ├── data
│   │   ├── __init__.py
│   │   ├── realesrgan_dataset.py
│   │   ╰── realesrgan_paired_dataset.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── realesrgan_model.py
│   │   ╰── realesrnet_model.py
│   ├── __init__.py
│   ├── RealESRGAN_x4plus.pth
│   ╰── utils.py
├── yolov5  /* Can be removed if you don't want to use the Yolov5x6 reCAPTCHA solver. */
│   ├── models
│   │   ├── hub
│   │   │   ╰── yolov5x6.yaml
│   │   ├── __init__.py
│   │   ├── common.py
│   │   ├── experimental.py
│   │   ├── yolo.py
│   │   ╰── yolov5x.yaml
│   ├── utils
│   │   ├── __init__.py
│   │   ├── activations.py
│   │   ├── augmentations.py
│   │   ├── autoanchor.py
│   │   ├── datasets.py
│   │   ├── downloads.py
│   │   ├── general.py
│   │   ├── metrics.py
│   │   ├── plots.py
│   │   ╰── torch_utils.py
│   ├── export.py
│   ├── hubconf.py
│   ╰── yolov5x6.pt
├── .gitignore  /* Can be removed. */
├── LICENSE  /* Can be removed. */
├── README.md  /* Can be removed. */
├── requirements_recaptcha.txt  /* Can be removed after installing modules. */
├── requirements.txt  /* Can be removed after installing modules. */
├── main.py
├── multiprocess.py  /* Available in the "Multiprocess" tool. */
╰── task.py  /* Available in the "Multiprocess" tool. */
```
  
</details>


# Changelog

## Versions 1.7.13:
 * Fixed a problem when no collection is mentioned in the metadata file and a default collection is used on OpenSea. The upload was leading to an error.

<details>
  <summary>Earlier versions.</summary>

### Versions 1.7.12 and 1.7.12.1:
 * Fixed the listing problems. **[#300](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/300)**.
  
### Version 1.7.11:
 * Fixed the "Sale Only" problem. **[#300](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/300)**.
 * Replaced the change of account with the private key by the name of the account.
  
### Version 1.7.10:
 * Added line break support for description (add a `\n` to break the line).
 * Minor fixes.
 * Added support with the new version of the [Multiprocessing](#multiprocessing) tool.
  
### Version 1.7.9:
 * Minor corrections for the contract signature on MetaMask.
 * Fixed an error that sometimes occurred when the collection is not mentioned.
 
### Version 1.7.8:
 * Correction of the listing on Polygon when the option "Upload and Sale" is selected.
  
### Version 1.7.7:
 * You can now choose whether you want to configure your wallet manually or not.
 * Minor changes.
  
### Version 1.7.6:
 * Fixed failure of the contract signature on Polygon blockchain. **[#288](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/288)**.
  
### Version 1.7.5:
 * Added support for the [OpenSea Deletion](#deletion) tool.
 * Minor fixes about the listing part.
  
### Version 1.7.4:
 * Correction of the listing in loop after a failure.
 * Correction of an incorrect file for the generated listing file.
 * Minor corrections and modifications.

### Version 1.7.3:
 * Added support for a new [reCAPTCHA ~solver~ bypasser](#recaptcha-bypasser) exploit.
  
### Versions 1.7.2 and 1.7.2.1:
 * Modification of the `main.py` file to make it more compatible with the new future tools.
 * Fixed `list index out of range` error with unlockable content.
  
### Version 1.7.1:
  * Fixed the several issues with the Coinbase Wallet. **[#278](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/278)**.

### Version 1.7.0:
  * Split the `main.py` file into different structures to make the bot more modular and compatible with future tools.
  * Fixed the problem of connecting to OpenSea which opens a tab to download MetaMask.
  
### Version 1.6.14:
  * Fixed the problem of the URL with the "Sale only".
  * Minor fixes.

### Version 1.6.13:
  * Improved manual resolution for reCAPTCHA. **[#264](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/264)**.
  * Fixed some issues with blockchain change. **[#262](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/262)**.
  * Minor fixes.

### Version 1.6.12:
  * Added support for blockchain switching on MetaMask (need feedback - may not work with Coinbase Wallet). **[#262](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/262)**.
  * Fixed `list index out of range` error with reCAPTCHA solver using CUDA. **[#263](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/263)**.
  * Removed unnecessary printouts used during development.
  * Minor corrections for sale part.

### Version 1.6.11:
  * Fixed the problem with the collection. **[#258](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/258)**.
  * Fixed 2Captcha callback function. **[#259](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/259)**.
  * Fixed the problem with downloading the pre-trained file (`urllib.error.URLError: urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate`) by changing the download method.

### Versions 1.6.10 and 1.6.10.1:
  * Fixed restarting the upload or sale when it fails the first time. **[#253](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/253)**.
  * Minor correction concerning the connection to OpenSea: the bot made the browser restart instead of trying a second time.

### Versions 1.6.9 to 1.6.9.3:
  * Added a new feature for collections. You can now use the URL format of your collection. This can solve the problem of collections not being found or clicked in the  list.  
    From `Crypto Parrot NFTs` to `crypto-parrot-nfts`, depending on the URL of your collection: `https://opensea.io/collection/crypto-parrot-nfts/`.
  * Minor fixes about version 1.6.9.

### Versions 1.6.8 and 1.6.8.1:
  * Added support for the 2Captcha API. **[#239](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/239)**.
  * Minor fixes.

### Version 1.6.7:
  * Improved MetaMask wallet switching, you can use the default account by skipping this step.
  * Fixed the `gateway` problem. **[#249](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/249)**.

### Version 1.6.6:
  * You can now select the wallet you want to use with MetaMask (many thanks to **[EmilianoBruni](https://github.com/EmilianoBruni)**!). **[#36](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/36), [#103](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/103)**.  
  _[How to get my private key?](https://metamask.zendesk.com/hc/en-us/articles/360015289632-How-to-Export-an-Account-Private-Key)_

### Version 1.6.5:
  * Merge the `main.py` and `main-manual-resolution.py` files.
  * Dissociation of the requirements files, one for the bot and one for the reCAPTCHA solver.

### Version 1.6.4:
  * The bot did not go to the sale page after the sequence of a failure and a success. **[#225](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/225)**.

### Version 1.6.3:
  * Added support for Coinbase Wallet (many thanks to **[MathieuAndrade](https://github.com/MathieuAndrade)**!).

### Version 1.6.2:
  * Wyvern 2.3 contract signature fixed for ChromeDriver and GeckoDriver. **[#152](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/152), [#165](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/165), [#183](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/183), [#201](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/201)**.
  * Minor corrections and improvements.
  * Yolov5x6 and Real-ESRGAN models, and the `recaptcha.py` file are not loaded when the "Sale only" option is selected.

### Version 1.6.1:
  * Updated the `requirements.txt` file, conflicts and problems seem to be corrected.
  * Removed unnecessary files from the `yolov5/` directory.
  * Fixed the problem of connection to OpenSea.
  * Improved reCAPTCHA verification when solved.

### Version 1.6.0:
  * The OpenSea connection problem seems to be fixed. An open tabs check has been added. **[#159](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/159), [#167](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/167), [#181](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/181), [#187](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/187)**.
  * reCAPTCHA solver added (Real ESRGAN + Yolov5x6 models used with PyTorch). **[#157](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/157), [#179](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/179), [#186](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/186)**.  
    ➜ Future improvements: models of crosswalks, chimneys, bridges.

### Version 1.5.12:
  * Wyvern 2.3 contract support (need feedbacks). **[#152](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/152), [#161](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/161), [#165](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/165)**. 

### Version 1.5.11:
  * <strike>Correction of the MetaMask contract signature (feedback needed).</strike> **[#144](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/144)**.
  * <strike>Wyvern 2.3 contract support (beta - need feedbacks).</strike> **[#152](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/152)**.
  * _In progress: improved support for MacOS (M1) - duration and contract list issues._

### Version 1.5.10:
  * Minor fixes concerning the `sale()` method of the OpenSea class.
  * Fixed exception iteration error.

### Version 1.5.9:
  * The `close()` method of the Webdriver class has been fixed. It creates an exception when listing NFTs. As a result, it does not try to list them a second time. **[#144](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/144), [#145](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/145), [#149](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/149)**.
  * During the download, when the webdriver starts, sometimes an error occurs and creates an exception. It was supposed to close the webdriver but it caused the bot to crash.
  * The download of webdriver requires a manual entry of the path after a number of failures.

### Version 1.5.8:
  * Errors related to incorrectly formatted files are now supported. An error is displayed but the bot does not stop abruptly. **[#90](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/90)**.
  * False listing errors are reduced, the robot checks a second time if the NFT is correctly listed.

### Version 1.5.7:
  * With each failed upload or sale, the bot retries a second time before saving the NFT data in an autogenerated file.
  * The duration has been fixed for GeckoDriver (Mozilla Firefox).  **[#121](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/121)**.

### Version 1.5.6:
  * The `dict_to_list()` method has been optimized and shortened.
  * Minor fixes.

### Version 1.5.5:
  * Fixed the `metamask_contract()` method. It was not signing the contract when completing the listing for the Ethereum Blockchain.
  * Minor fixes.

### Version 1.5.4:
  * The HTTPConnectionPool error in Selenium is fixed, it was caused by defining the driver inside a loop. Now the bot will print an error and restart to launch the bot. **[#112](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/112)**.  
    ➜ For more informations: **[Reddit - Ralphc360's comment](https://www.reddit.com/r/selenium/comments/cuynft/comment/f85odbh/?utm_source=share&utm_medium=web2x&context=3)**.
  * You can now sell your NFTs on the Ethereum Blockchain for free.

### Version 1.5.3:
  * Fixed the Webdriver-Manager module, it was downloading the ChromeDriver or GeckoDriver at each webdriver launch. Now it uses the path of the downloaded webdriver. **[#112](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/112)**.
  * Fixed the collection input. **[#108](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/108)**.

### Version 1.5.2:
  * Headless mode support. Download Mozilla Firefox and you can use this bot in the background without any interface.
    Note: Firefox may be unstable and some features may work differently or not at all.  **[#64](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/64), [#69](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/discussions/69), [#106](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/106)**.
  * Fixed the connection to the MetaMask success indicator.

### Version 1.5.1:
  * Fixed the problem of the worker version 1.5.0. The bot now continues to upload and does not restart the upload from the beginning. **[#107](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/107)**.

### Version 1.5.0:
  * The reCAPTCHAs can now be bypassed. The bot restarts for each upload - it's a bit slow but it works. **[#98](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/98), [#102](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/pull/102)**.  
    Thanks to **[Kanishka-Chandra](https://github.com/Kanishka-Chandra)** and **[elwanm](https://github.com/elwanm)**.
  * The bot restarts after 3 failed connections to the wallet or to OpenSea.

### Version 1.4.9:
  * Minor fixes.
  * Developers can now add new wallets if they wish.
  * ChromeDriver is automatically downloaded - no need to do it manually (`pip install -r requirements.txt` required).
  * _The reCAPTCHAs solver is not integrated/configured._

### Version 1.4.8:
  * <strike>Added a new feature that allows to upload more than 50 items in a collection. Requires to be activated (asked at launch).</strike> (Method used: https://www.youtube.com/watch?v=8wpmjh8xrXo). **Update:** This method is useless because [OpenSea went back on its words](https://twitter.com/opensea/status/1486843201352716289). The limit has been removed.
  * Minor fix.

### Version 1.4.7:
  * The default language of ChromeDriver is now English to ensure maximum compatibility. The date did not work in some countries because of the different formats that OpenSea offers. **[#67](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/67)**.
  * Minor fix (Colorama module).

### Version 1.4.6:
  * The duration has been corrected. OpenSea does not allow to change the year when the next year is more than 6 months away. So it was impossible to enter the month without it being replaced by December (12 - maximum number because the year was entered instead); **Note: maximum duration is 6 months. [#55](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/55)**.
  * The connection to OpenSea has *certainly* been corrected. (need feedback about this - I don't have any problems on my side). **[#53](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/53), [#58](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/58), [#61](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/61)**.

### Version 1.4.5:
  * Minor fix for Linux users. The `clear_text(self)` method inserts an "A" when it tries to clear the inputs before sending the data. **[#39](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/39)**.

### Version 1.4.4:
  * Connection to OpenSea with MetaMask corrected. Download of the extension was requested. **[#53](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/53)**.
  * Connection to OpenSea with MetaMask improved.

### Version 1.4.3:
  * File preview is now added. **[#48](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/48)**.

### Version 1.4.2:
  * Listing of NFT on the Ethereum Blockchain is fully supported. **Be sure to make a deposit and have more than 0.05 ETH on your wallet.**

### Version 1.4.1:
  * Small fix for XLSX files. Empty cells were interpreted as "NaN", which is not interpreted as an empty string for Python. **[#18](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/18), [#23](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/23)**.

### Version 1.4.0:
  * You can now decide whether you want to upload or sell your NFTs, or both. **[#3](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/3), [#22](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/22)**.
  * Signing the MetaMask contract works every time. It can take 30 seconds to be signed when connecting to OpenSea. **[#5](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/5), [#17](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/17)**.
  * After uploading the NFT, the bot would crash when it tried to sell it (the URL was not correct). Now it doesn't. **[#17](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/17)**.
  * MacOS and Linux support improved.
  * Calendar method improved.

### Version 1.3.0:
  * Important fixes. **[#4](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/4), [#6](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/6), [#10](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/10), [#11](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/11), [#12](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/12), [#14](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/14)**.
  * CSV file modified: separator changed (from ";" to ";;").

### Version 1.2.0:
  * Possibility to set a price for each NFT added.  
    ➜ 1+ supplies and Polygon blockchain support added.
  * Supply input issue fixed.
  * Calendar method improved.

### Version 1.2.0-alpha:
  * Possibility to set a price for each NFT added.

### Version 1.1.0:
  * XLSX support added.
  * PC-wide data file browse support.
  * Properties, Stats and Levels issues fixed. **[#1](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/1)**.

### Version 1.0.0:
  * Inital commit.
  
</details>
  
