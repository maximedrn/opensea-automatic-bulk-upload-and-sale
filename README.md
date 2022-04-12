# Automatically and massively upload and sell your non-fungible tokens on OpenSea using Python Selenium.
_A Selenium Python bot to automatically and bulky upload and sell your NFTs on OpenSea  
  (all metadata integrated - Ethereum and Polygon supported) - reCAPTCHA solver included._

---

### **Please read the README file before using this tool, opening a problem or a discussion, or contacting me.**  
  ➜ _Open an issue?_ Provide an **excerpt from your metadata file**, your **operating system** and **detail your error**.  
  ➜ Make sure you have the **latest modules, browser and bot installed**.  
  ➜ Read the [pinned **and** opened issues](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues), see the [example metadata files](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/tree/master/data). 

---

### **If you want to promote the tools of this bot and benefit from a percentage of sales of them, you can join my [affiliate program](https://maximedrn.gumroad.com/affiliates) (_25% of the price of a sale will be yours_).**

* **(_Version 1.6.9 - April 12, 2022_).**  
* Sign up on [OpenSea](https://opensea.io/).
* Sign up on [MetaMask](https://metamask.io/).
* Sign up on [Coinbase](https://www.coinbase.com/).
* _If you want to use the 2Captcha API to resolve reCAPTCHAs_.  
  **Paid service**: $2.99 per 1000 reCAPTCHAs.  
  Sign up on [2Captcha](https://2captcha.com?from=13853725) (affiliate link).

---

# Table of contents

* **[What does this bot do?](#what-does-this-bot-do)** 
* **Useful tools to have for this bo.**
  * [Discover them](https://maximedrn.gumroad.com/).
  * [Create metadata file on your phone](#create-metadata-file-on-your-phone).
  * [Scrape your collection (URLs scraper)](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/tree/master/extension-tools/collection-scraper).
  * [Make your file compatible](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/tree/master/extension-tools/file-compatibilizer).
  * [Easily generate your metadata file](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/tree/master/extension-tools/generic-file).
* **[Changelog](#changelog).**
* **[Prerequisites for reCAPTCHA solver](#prerequisites-for-recaptcha-solver)**.
* **[Instructions](#instructions)**.
  * [Basic installation of Python for beginners](#basic-installation-of-python-for-beginners).
  * [Configuration of the bot](#configuration-of-the-bot).
  * [Run the bot](#run-the-bot).
* **[Data files structure](#data-files-structure).**
  * [Upload and sale](#upload-and-sale).
  * [Upload only](#upload-only).
  * [Sale only](#sale-only).
* **[Configuration of the sale part of the NFTs](#configuration-of-the-sale-part-of-the-nfts).**

## What does this bot do?

This script allows you to upload and sell **as many NFTs as you want to OpenSea**, all **automatically** and **quickly**. **All metadata are integrated**, and the **Ethereum** and **Polygon** Blockchains are supported.  

**You can decide whether you want to upload or sell your NFTs, or both**. If you upload your NFTs and sell them later, a CSV file is created with the URL of the NFT as well as its Blockchain and supply number.

➜ **If you sell any NFT with this bot, you can consider sharing some of your earnings**: 😉
**0xDD135d5be0a23f6daAAE7D2d0580828c9e09402E** (Ethereum).  
➜ **Or you can buy me a NFT from my collection [Crypto Parrot](https://opensea.io/collection/crypto-parrot-nfts) if this bot was useful to you**.

## Changelog

**Versions 1.6.9 to 1.6.9.3:**
* Added a new feature for collections. You can now use the URL format of your collection. This can solve the problem of collections not being found or clicked in the list.  
    From `Crypto Parrot NFTs` to `crypto-parrot-nfts`, depending on the URL of your collection: `https://opensea.io/collection/crypto-parrot-nfts/`.
* Minor fixes about version 1.6.9.

<details>
  <summary><strong>Old versions</strong></summary><br />

* **Version 1.6.8 + 1.6.8.1:**
  * Added support for the 2Captcha API. **[#239](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/239)**.
  * Minor fixes.
* **Version 1.6.7:**
  * Improved MetaMask wallet switching, you can use the default account by skipping this step.
  * Fixed the `gateway` problem. **[#249](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/249)**.
* **Version 1.6.6:**
  * You can now select the wallet you want to use with MetaMask (many thanks to **[EmilianoBruni](https://github.com/EmilianoBruni)**!). **[#36](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/36), [#103](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/103)**.  
  _[How to get my private key?](https://metamask.zendesk.com/hc/en-us/articles/360015289632-How-to-Export-an-Account-Private-Key)_
* **Version 1.6.5:**
  * Merge the `main.py` and `main-manual-resolution.py` files.
  * Dissociation of the requirements files, one for the bot and one for the reCAPTCHA solver.
* **Version 1.6.4:**
  * The bot did not go to the sale page after the sequence of a failure and a success. **[#225](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/225)**.
* **Version 1.6.3:**
  * Added support for Coinbase Wallet (many thanks to **[MathieuAndrade](https://github.com/MathieuAndrade)**!).
* **Version 1.6.2:**
  * Wyvern 2.3 contract signature fixed for ChromeDriver and GeckoDriver. **[#152](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/152), [#165](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/165), [#183](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/183), [#201](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/201)**.
  * Minor corrections and improvements.
  * Yolov5x6 and Real-ESRGAN models, and the `recaptcha.py` file are not loaded when the "Sale only" option is selected.
* **Version 1.6.1:**
  * Updated the `requirements.txt` file, conflicts and problems seem to be corrected.
  * Removed unnecessary files from the `yolov5/` directory.
  * Fixed the problem of connection to OpenSea.
  * Improved reCAPTCHA verification when solved.
* **Version 1.6.0:**
  * The OpenSea connection problem seems to be fixed. An open tabs check has been added. **[#159](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/159), [#167](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/167), [#181](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/181), [#187](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/187)**.
  * reCAPTCHA solver added (Real ESRGAN + Yolov5x6 models used with PyTorch). **[#157](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/157), [#179](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/179), [#186](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/186)**.  
    ➜ Future improvements: models of crosswalks, chimneys, bridges.
* **Version 1.5.12:**
  * Wyvern 2.3 contract support (need feedbacks). **[#152](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/152), [#161](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/161), [#165](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/165)**. 
* **Version 1.5.11:**
  * <strike>Correction of the MetaMask contract signature (feedback needed).</strike> **[#144](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/144)**.
  * <strike>Wyvern 2.3 contract support (beta - need feedbacks).</strike> **[#152](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/152)**.
  * _In progress: improved support for MacOS (M1) - duration and contract list issues._
* **Version 1.5.10:**
  * Minor fixes concerning the `sale()` method of the OpenSea class.
  * Fixed exception iteration error.
* **Version 1.5.9:**
  * The `close()` method of the Webdriver class has been fixed. It creates an exception when listing NFTs. As a result, it does not try to list them a second time. **[#144](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/144), [#145](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/145), [#149](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/149)**.
  * During the download, when the webdriver starts, sometimes an error occurs and creates an exception. It was supposed to close the webdriver but it caused the bot to crash.
  * The download of webdriver requires a manual entry of the path after a number of failures.
* **Version 1.5.8:**
  * Errors related to incorrectly formatted files are now supported. An error is displayed but the bot does not stop abruptly. **[#90](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/90)**.
  * False listing errors are reduced, the robot checks a second time if the NFT is correctly listed.
* **Version 1.5.7:**
  * With each failed upload or sale, the bot retries a second time before saving the NFT data in an autogenerated file.
  * The duration has been fixed for GeckoDriver (Mozilla Firefox).  **[#121](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/121)**.
* **Version 1.5.6:**
  * The `dict_to_list()` method has been optimized and shortened.
  * Minor fixes.
* **Version 1.5.5:**
  * Fixed the `metamask_contract()` method. It was not signing the contract when completing the listing for the Ethereum Blockchain.
  * Minor fixes.
* **Version 1.5.4:**
  * The HTTPConnectionPool error in Selenium is fixed, it was caused by defining the driver inside a loop. Now the bot will print an error and restart to launch the bot. **[#112](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/112)**.  
    ➜ For more informations: **[Reddit - Ralphc360's comment](https://www.reddit.com/r/selenium/comments/cuynft/comment/f85odbh/?utm_source=share&utm_medium=web2x&context=3)**.
  * You can now sell your NFTs on the Ethereum Blockchain for free.
* **Version 1.5.3:**
  * Fixed the Webdriver-Manager module, it was downloading the ChromeDriver or GeckoDriver at each webdriver launch. Now it uses the path of the downloaded webdriver. **[#112](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/112)**.
  * Fixed the collection input. **[#108](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/108)**.
* **Version 1.5.2:**
  * Headless mode support. Download Mozilla Firefox and you can use this bot in the background without any interface.
    Note: Firefox may be unstable and some features may work differently or not at all.  **[#64](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/64), [#69](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/discussions/69), [#106](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/106)**.
  * Fixed the connection to the MetaMask success indicator.
* **Version 1.5.1:**
  * Fixed the problem of the worker version 1.5.0. The bot now continues to upload and does not restart the upload from the beginning. **[#107](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/107)**.
* **Version 1.5.0:**
  * The reCAPTCHAs can now be bypassed. The bot restarts for each upload - it's a bit slow but it works. **[#98](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/98), [#102](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/pull/102)**.  
    Thanks to **[Kanishka-Chandra](https://github.com/Kanishka-Chandra)** and **[elwanm](https://github.com/elwanm)**.
  * The bot restarts after 3 failed connections to the wallet or to OpenSea.
* **Version 1.4.9:**
  * Minor fixes.
  * Developers can now add new wallets if they wish.
  * ChromeDriver is automatically downloaded - no need to do it manually (`pip install -r requirements.txt` required).
  * _The reCAPTCHAs solver is not integrated/configured._
* **Version 1.4.8:**
  * <strike>Added a new feature that allows to upload more than 50 items in a collection. Requires to be activated (asked at launch).</strike> (Method used: https://www.youtube.com/watch?v=8wpmjh8xrXo). **Update:** This method is useless because [OpenSea went back on its words](https://twitter.com/opensea/status/1486843201352716289). The limit has been removed.
  * Minor fix.
* **Version 1.4.7:**
  * The default language of ChromeDriver is now English to ensure maximum compatibility. The date did not work in some countries because of the different formats that OpenSea offers. **[#67](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/67)**.
  * Minor fix (Colorama module).
* **Version 1.4.6:**
  * The duration has been corrected. OpenSea does not allow to change the year when the next year is more than 6 months away. So it was impossible to enter the month without it being replaced by December (12 - maximum number because the year was entered instead); **Note: maximum duration is 6 months. [#55](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/55)**.
  * The connection to OpenSea has *certainly* been corrected. (need feedback about this - I don't have any problems on my side). **[#53](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/53), [#58](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/58), [#61](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/61)**.
* **Version 1.4.5:**
  * Minor fix for Linux users. The `clear_text(self)` method inserts an "A" when it tries to clear the inputs before sending the data. **[#39](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/39)**.
* **Version 1.4.4:**
  * Connection to OpenSea with MetaMask corrected. Download of the extension was requested. **[#53](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/53)**.
  * Connection to OpenSea with MetaMask improved.
* **Version 1.4.3:**
  * File preview is now added. **[#48](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/48)**.
* **Version 1.4.2:**
  * Listing of NFT on the Ethereum Blockchain is fully supported. **Be sure to make a deposit and have more than 0.05 ETH on your wallet.**
* **Version 1.4.1:**
  * Small fix for XLSX files. Empty cells were interpreted as "NaN", which is not interpreted as an empty string for Python. **[#18](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/18), [#23](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/23)**.
* **Version 1.4:**
  * You can now decide whether you want to upload or sell your NFTs, or both. **[#3](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/3), [#22](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/22)**.
  * Signing the MetaMask contract works every time. It can take 30 seconds to be signed when connecting to OpenSea. **[#5](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/5), [#17](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/17)**.
  * After uploading the NFT, the bot would crash when it tried to sell it (the URL was not correct). Now it doesn't. **[#17](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/17)**.
  * MacOS and Linux support improved.
  * Calendar method improved.
* **Version 1.3:**
  * Important fixes. **[#4](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/4), [#6](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/6), [#10](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/10), [#11](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/11), [#12](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/12), [#14](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/14)**.
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
  * Properties, Stats and Levels issues fixed. **[#1](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/1)**.
* **Version 1.0:** 
  * Inital commit.

</details>

## Prerequisites for reCAPTCHA solver

You will need a graphics card (GPU) with CUDA (Compute Unified Device Architecture).
* Search for your GPU on [GPUZoo](https://www.gpuzoo.com/) and check if CUDA is compatible (Cores / Texture -> CUDA).
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

## Instructions

* [Download the repository](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/archive/refs/heads/master.zip) or clone it by typing this command in your command prompt:
    
    ```
    git clone https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale.git
    ```

* ### Basic installation of Python for beginners:
  * It requires [Python](https://www.python.org/) 3.9.7+ (3.10 can be unstable) - _developped with Python 3.9.9_.
  * Install [pip](https://pip.pypa.io/en/stable/installation/) to be able to have needed Python modules.

* ### Configuration of the bot:
  * Extract the repository folder from the ZIP file, you should have a folder named  `opensea-automatic-bulk-upload-and-sale-master`.
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
  * Create your NFTs data file containing all details of each NFT. It can be a JSON, CSV or XLSX file. You can save it in the `data/` folder.  
    **[What structure should the files have?](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale#data-files-structure)**
* ### Run the bot:
  * Open a command prompt in the `opensea-automatic-bulk-upload-and-sale-master/` folder path.
  * Type one of these commands to run the bot:
    
    * ```
      python main.py
      ```
    * ```
      python3 main.py
      ```


## Data files structure

![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) &nbsp; **➜ Easily generate your metadata file using this [tool](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/tree/master/extension-tools/generic-file).**

* If you do not want to add details to the values not required, leave:
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

<strong>Required values *</strong>  
  (Mandatory value in certain specified cases)

* ### Upload and sale

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
           <br>"file_path": ["C:/Users/Admin/Desktop/NFT/nft_0001.mp4", "C:/Users/Admin/Desktop/NFT/nft_0001-preview.png"],</td>
           <td>C:/Users/Admin/Desktop/NFT/nft_0001.png;;
           <br>["C:/Users/Admin/Desktop/NFT/nft_0001.mp4", "C:/Users/Admin/Desktop/NFT/nft_0001-preview.png"];;</td>
           <td>C:/Users/Admin/Desktop/NFT/nft_0001.png
           <br>["C:/Users/Admin/Desktop/NFT/nft_0001.mp4", "C:/Users/Admin/Desktop/NFT/nft_0001-preview.png"];;</td>
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
              <br>my-nfts;;</td>
           <td>My NFTs
              <br>my-nfts</td>
        </tr>
        <tr>
           <td>Properties</td>
           <td>List[[String, String], ...]
            <br>List[String, String]</td>
           <td>["type", "name"]
            <br>[["type", "name"], ["type", "name"]]</td>
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
            <br>List[String, Integer, Integer]</td>
           <td>["name", value_from, value_to]
            <br>[["name", value_from, value_to], ["name", value_from, value_to]]</td>
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
            <br>List[String, Integer, Integer]</td>
           <td>["name", value_from, value_to]
            <br>[["name", value_from, value_to], ["name", value_from, value_to]]</td>
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
            <br>Boolean</td>
           <td>[True, "unlockable_content"]
            <br>[False]
            <br>False</td>
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
            <br>["method, ""]</td>
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
            <br>String</td>
           <td>["from_date", "to_date"]
            <br>["days/weeks/months"]
            <br>"days/weeks/months"</td>
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
            <br>Boolean</td>
           <td>[True, "wallet"]
            <br>[False]
            <br>False</td>
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
 
* ### Upload only

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
           <br>"file_path": ["C:/Users/Admin/Desktop/NFT/nft_0001.mp4", "C:/Users/Admin/Desktop/NFT/nft_0001-preview.png"],</td>
           <td>C:/Users/Admin/Desktop/NFT/nft_0001.png;;
           <br>["C:/Users/Admin/Desktop/NFT/nft_0001.mp4", "C:/Users/Admin/Desktop/NFT/nft_0001-preview.png"];;</td>
           <td>C:/Users/Admin/Desktop/NFT/nft_0001.png
           <br>["C:/Users/Admin/Desktop/NFT/nft_0001.mp4", "C:/Users/Admin/Desktop/NFT/nft_0001-preview.png"];;</td>
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
              <br>my-nfts;;</td>
           <td>My NFTs
              <br>my-nfts</td>
        </tr>
        <tr>
           <td>Properties</td>
           <td>List[[String, String], ...]
            <br>List[String, String]</td>
           <td>["type", "name"]
            <br>[["type", "name"], ["type", "name"]]</td>
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
            <br>List[String, Integer, Integer]</td>
           <td>["name", value_from, value_to]
            <br>[["name", value_from, value_to], ["name", value_from, value_to]]</td>
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
            <br>List[String, Integer, Integer]</td>
           <td>["name", value_from, value_to]
            <br>[["name", value_from, value_to], ["name", value_from, value_to]]</td>
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
            <br>Boolean</td>
           <td>[True, "unlockable_content"]
            <br>[False]
            <br>False</td>
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
 
  And it gives you something like this: [JSON](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/blob/master/data/json_structure_upload_only.json), [CSV](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/blob/master/data/csv_structure_upload_only.csv), [XLSX (must be downloaded to view it)](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/blob/master/data/xlsx_structure_upload_only.xlsx).
 
* ### Sale only
 
  If you have already uploaded your NFTs with this bot, a file has been generatcontaining the URL, the Blockchain and the supply number of each NFT. You have to complete it with sale values.

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
           <td>"nft_url": "https://opensea.io/assets/matic/0x2953399124f0cbb46d2cbacd8a89cf0599974963/99995353970554757559721471534129028266698199001274859511402524949800648966145",</td>
           <td>https://opensea.io/assets/matic/0x2953399124f0cbb46d2cbacd8a89cf0599974963/99995353970554757559721471534129028266698199001274859511402524949800648966145;;</td>
           <td>https://opensea.io/assets/matic/0x2953399124f0cbb46d2cbacd8a89cf0599974963/99995353970554757559721471534129028266698199001274859511402524949800648966145</td>
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
             <br>"sale_type": "",</td>
           <td>Timed Auction;;</td>
           <td>Timed Auction</td>
        </tr>
        <tr>
           <td><strong>Price *</strong></td>
           <td>Float or Integer</td>
           <td></td>
           <td>"price": 5,
              <br>"price: 0.25,</td>
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
            <br>["method, ""]</td>
           <td>"method": ["Sell with declining price", 0.002],
              <br>"method": ["Sell to highest bidder", 0.05],
              <br>"method": ["Sell to highest bidder", ""],
              <br>"method": "",</td>
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
            <br>String</td>
           <td>["from_date", "to_date"]
            <br>["days/weeks/months"]
            <br>"days/weeks/months"</td>
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
            <br>Boolean</td>
           <td>[True, "wallet"]
            <br>[False]
            <br>False</td>
           <td>"specific_buyer": [true, "0xDD135d5be0a23f6daAAE7D2d0580828c9e09402E"]
               <br>"specific_buyer": [false]
               <br>"specific_buyer": false,
               <br>specific_buyer": "",</td>
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
             <br>"quantity": ""</td>
           <td>4</td>
           <td>4</td>
        </tr>
     </tbody>
  </table>

  And it gives you something like this: [JSON](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/blob/master/data/json_structure_sale_only.json), [CSV](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/blob/master/data/csv_structure_sale_only.csv), [XLSX (must be downloaded to view it)](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/blob/master/data/xlsx_structure_sale_only.xlsx).


## Configuration of the sale part of the NFTs

When you want to sell your NFTs, Opensea requires various details according to their Blockchain or supply number.  
**Note: The maximum duration of sale should be at most 6 months. It must be entered in the form of start date - end date.**  

Make sure to **deposit Ethereum (ETH/WETH)** or **Polygon (MATIC)** on your wallet before proceeding to the sale. Otherwise the bot will cancel the sale. Opensea needs an **Ethereum** wallet with more than **0.05 ETH** or a **Polygon** wallet with a deposit of **any amount**. For **Ethereum**, you have to make a first listing manually before using this bot.

![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) &nbsp; **➜ You have already uploaded your NFTs on OpenSea and you don't want to copy the URLs one by one?** Use this [tool](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/tree/master/extension-tools/collection-scraper)!

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
