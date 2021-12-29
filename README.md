# Automatically upload your NFTs on Opensea using Python Selenium.

* **(_Version 1.4 - December 29, 2021_).**
* Sign up on [Opensea](https://opensea.io/?ref=0xDD135d5be0a23f6daAAE7D2d0580828c9e09402E) (Affiliate link).
* Sign up on [MetaMask](https://metamask.io/).


# Table of contents:

* **[What does this bot do?](https://github.com/maximedrn/opensea_automatic_uploader#what-does-this-bot-do)**
* **[Changelog](https://github.com/maximedrn/opensea_automatic_uploader#changelog).**
* **[To do list](https://github.com/maximedrn/opensea_automatic_uploader#to-do-list).**
* **[Instructions](https://github.com/maximedrn/opensea_automatic_uploader#instructions)**.
  * [Basic installation of Python for beginners](https://github.com/maximedrn/opensea_automatic_uploader#basic-installation-of-python-for-beginners).
  * [Configuration of the bot](https://github.com/maximedrn/opensea_automatic_uploader#configuration-of-the-bot).
* **[Data files structure](https://github.com/maximedrn/opensea_automatic_uploader#data-files-structure).**
  * [Upload and sale](https://github.com/maximedrn/opensea_automatic_uploader#upload-and-sale).
  * [Upload only](https://github.com/maximedrn/opensea_automatic_uploader#upload-only).
  * [Sale only](https://github.com/maximedrn/opensea_automatic_uploader#sale-only).
* **[Configuration of the sales part of the NFTs](https://github.com/maximedrn/opensea_automatic_uploader#configuration-of-the-sales-part-of-the-nfts).**
* **[Known issues and important things to know](https://github.com/maximedrn/opensea_automatic_uploader#known-issues-and-important-things-to-know).**


## What does this bot do?

This script allows you to upload and sell **as many NFTs as you want to Opensea**, all **automatically** and **quickly** (about 2.5 NFTs per minute).
**You can decide whether you want to upload or sell your NFTs, or both**. If you upload your NFTs and sell them later, a CSV file is created with the URL of the NFT as well as its Blockchain and supply number.

➜ **If you sell any NFT with this bot, you can consider sharing some of your earnings**: 😉
**0xDD135d5be0a23f6daAAE7D2d0580828c9e09402E** (Ethereum).  
➜ **Or you can buy me a NFT from my collection [Crypto Parrot](https://opensea.io/collection/crypto-parrot-nfts) if this bot was useful to you**.


## Changelog:

* **Version 1.4:**
  * You can now decide whether you want to upload or sell your NFTs, or both. **[#3](https://github.com/maximedrn/opensea_automatic_uploader/issues/3), [#22](https://github.com/maximedrn/opensea_automatic_uploader/issues/22)**.
  * Signing the MetaMask contract works every time. It can take 30 seconds to be signed when connecting to Opensea. **[#5](https://github.com/maximedrn/opensea_automatic_uploader/issues/5), [#17](https://github.com/maximedrn/opensea_automatic_uploader/issues/17)**.
  * After uploading the NFT, the bot would crash when it tried to sell it (the URL was not correct). Now it doesn't. **[#17](https://github.com/maximedrn/opensea_automatic_uploader/issues/17)**.
  * MacOS and Linux support improved.
  * Calendar method improved.
* **Version 1.3:**
  * Important fixes. **[#4](https://github.com/maximedrn/opensea_automatic_uploader/issues/4), [#6](https://github.com/maximedrn/opensea_automatic_uploader/issues/6), [#10](https://github.com/maximedrn/opensea_automatic_uploader/issues/10), [#11](https://github.com/maximedrn/opensea_automatic_uploader/issues/11), [#12](https://github.com/maximedrn/opensea_automatic_uploader/issues/12), [#14](https://github.com/maximedrn/opensea_automatic_uploader/issues/14)**.
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
  * Properties, Stats and Levels issues fixed. **[#1](https://github.com/maximedrn/opensea_automatic_uploader/issues/1)**.
* **Version 1.0:** 
  * Inital commit.


## To do list:

* ✔ <strike>MetaMask automatic login.</strike>
* ✔ <strike>Opensea automatic login with MetaMask.</strike>
* ❌ Opensea automatic login with different wallets.
* ❌ Collection creator for Opensea.
* ✔ <strike>Automatic NFT uploader.</strike>
* ✔ <strike>Possibility to set a price for each NFT.</strike>  
  * ✔ Support for 1+ supplies and Polygon blockchain.
  * ❌ "Sell as bundle" part (not planned to be added).
  * ✔ **Sale part**.
* ✔ <strike>Data file browsing feature.</strike>
* ✔ <strike>CSV structure reader and interpreter.</strike>
* ✔ <strike>JSON structure reader and interpreter.</strike>
* ✔ <strike>XLSX structure reader and interpreter.</strike>
* ❌ NFT maker local website.


## Instructions:

* ### Basic installation of Python for beginners:
  * [Download this repository](https://github.com/maximedrn/opensea_automatic_uploader/archive/refs/heads/master.zip) or clone it by typing this command in your command prompt:
```
git clone https://github.com/maximedrn/opensea_automatic_uploader.git
```
  * It requires [Python](https://www.python.org/) 3.7 or a newest version - _developped with Python 3.9.7_.
  * Install [pip](https://pip.pypa.io/en/stable/installation/) to be able to have needed Python modules.
  * Open a command prompt in the repository folder and type:
```
pip install -r requirements.txt
```
* ### Configuration of the bot:
  * Download and install [Google Chrome](https://www.google.com/intl/en_en/chrome/).
  * Download the [ChromeDriver executable](https://chromedriver.chromium.org/downloads) that is compatible with the actual version of your Google Chrome (or Chrome like) browser and your OS (Operating System). To know your Google Chrome (or Chrome like) browser version, refer to: **_[What version of Google Chrome do I have?](https://www.whatismybrowser.com/detect/what-version-of-chrome-do-i-have)_**
  * Extract the executable file from the ZIP file and copy/paste it in the `assets/` folder of the repository.
  * Create your NFTs data file containing all details of each NFT. It can be a JSON, CSV or XLSX file. You can save it in the `data/` folder.  
    **[What structure should the files have?](https://github.com/maximedrn/opensea_automatic_uploader#data-files-structure)**


## Data files structure:

* ### Upload and sale:

 <strong>Required values *</strong>
 <table>
    <tbody>
       <tr>
          <td>Settings</td>
          <td>Types</td>
          <td>Literal examples</td>
          <td>JSON examples</td>
          <td>CSV examples</td>
          <td>XLSX examples</td>
       </tr>
       <tr>
          <td><strong>File Path *</strong></td>
          <td>String</td>
          <td></td>
          <td>"file_path": "C:/Users/Admin/Desktop/NFT/nft_0001.png",</td>
          <td>C:/Users/Admin/Desktop/NFT/nft_0001.png;;</td>
          <td>C:/Users/Admin/Desktop/NFT/nft_0001.png</td>
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
          <td>"external_link": "https://github.com/maximedrn/opensea_automatic_uploader",
             <br>"external_link": "",
          </td>
          <td>https://github.com/maximedrn/opensea_automatic_uploader;;</td>
          <td>https://github.com/maximedrn/opensea_automatic_uploader</td>
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
             <br>"collection": "",
          </td>
          <td>My NFTs;;</td>
          <td>My NFTs.</td>
       </tr>
       <tr>
          <td>Properties</td>
          <td>List[[String, String], ...] or List[String, String]</td>
          <td>["type", "name"] or [["type", "name"], ["type", "name"]]</td>
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
          <td>List[[String, Integer, Integer], ...] or List[String, Integer, Integer]</td>
          <td>["name", value_from, value_to] or [["name", value_from, value_to], ["name", value_from, value_to]]</td>
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
          <td>List[[String, Integer, Integer], ...] or List[String, Integer, Integer]</td>
          <td>["name", value_from, value_to] or [["name", value_from, value_to], ["name", value_from, value_to]]</td>
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
          <td>List[Boolean, String] or List[Boolean] or Boolean</td>
          <td>[True, "unlockable_content"] or [False] or False</td>
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
          <td>["method", price] or ["method, ""]</td>
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
          <td>List[String, String] or List[String] or String</td>
          <td>["from_date", "to_date"] or ["days/weeks/months"] or "days/weeks/months"</td>
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
          <td>List[Boolean, String] or [Boolean] or Boolean</td>
          <td>[True, "wallet"] or [False] or False</td>
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
          <td></td>
       </tr>
    </tbody>
 </table>
 
  And it gives you something like this: [CSV](https://github.com/maximedrn/opensea_automatic_uploader/blob/master/data/csv_structure_upload_and_sale.csv), [JSON](https://github.com/maximedrn/opensea_automatic_uploader/blob/master/data/json_structure_upload_and_sale.json), [XLSX (must be downloaded to view it)](https://github.com/maximedrn/opensea_automatic_uploader/blob/master/data/xlsx_structure_upload_and_sale.xlsx).
 
* ### Upload only:

 <strong>Required values *</strong>
 <table>
    <tbody>
       <tr>
          <td>Settings</td>
          <td>Types</td>
          <td>Literal examples</td>
          <td>JSON examples</td>
          <td>CSV examples</td>
          <td>XLSX examples</td>
       </tr>
       <tr>
          <td><strong>File Path *</strong></td>
          <td>String</td>
          <td></td>
          <td>"file_path": "C:/Users/Admin/Desktop/NFT/nft_0001.png",</td>
          <td>C:/Users/Admin/Desktop/NFT/nft_0001.png;;</td>
          <td>C:/Users/Admin/Desktop/NFT/nft_0001.png</td>
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
          <td>"external_link": "https://github.com/maximedrn/opensea_automatic_uploader",
             <br>"external_link": "",
          </td>
          <td>https://github.com/maximedrn/opensea_automatic_uploader;;</td>
          <td>https://github.com/maximedrn/opensea_automatic_uploader</td>
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
             <br>"collection": "",
          </td>
          <td>My NFTs;;</td>
          <td>My NFTs.</td>
       </tr>
       <tr>
          <td>Properties</td>
          <td>List[[String, String], ...] or List[String, String]</td>
          <td>["type", "name"] or [["type", "name"], ["type", "name"]]</td>
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
          <td>List[[String, Integer, Integer], ...] or List[String, Integer, Integer]</td>
          <td>["name", value_from, value_to] or [["name", value_from, value_to], ["name", value_from, value_to]]</td>
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
          <td>List[[String, Integer, Integer], ...] or List[String, Integer, Integer]</td>
          <td>["name", value_from, value_to] or [["name", value_from, value_to], ["name", value_from, value_to]]</td>
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
          <td>List[Boolean, String] or List[Boolean] or Boolean</td>
          <td>[True, "unlockable_content"] or [False] or False</td>
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
          <td>"blockchain": "Polygon"
             <br>"blockchain" : ""
          </td>
          <td>Polygon</td>
          <td>Polygon</td>
       </tr>
    </tbody>
 </table>
 
 And it gives you something like this: [CSV](https://github.com/maximedrn/opensea_automatic_uploader/blob/master/data/csv_structure_upload_only.csv), [JSON](https://github.com/maximedrn/opensea_automatic_uploader/blob/master/data/json_structure_upload_only.json), [XLSX (must be downloaded to view it)](https://github.com/maximedrn/opensea_automatic_uploader/blob/master/data/xlsx_structure_upload_only.xlsx).
 
 * ### Sale only:
 
 If you have already uploaded your NFTs with this bot, a file has been generated with containing the URL, the Blockchain and the supply number of each NFT. You have to complete it with sale values.
 
 <strong>Required values *</strong>
 <table>
    <tbody>
       <tr>
          <td>Settings</td>
          <td>Types</td>
          <td>Literal examples</td>
          <td>JSON examples</td>
          <td>CSV examples</td>
          <td>XLSX examples</td>
       </tr>
       <tr>
          <td>NFT URL</td>
          <td>String</td>
          <td></td>
          <td>"nft_url": "https://opensea.io/assets/matic/0x2953399124f0cbb46d2cbacd8a89cf0599974963/99995353970554757559721471534129028266698199001274859511402524949800648966145",</td>
          <td>https://opensea.io/assets/matic/0x2953399124f0cbb46d2cbacd8a89cf0599974963/99995353970554757559721471534129028266698199001274859511402524949800648966145;;</td>
          <td>https://opensea.io/assets/matic/0x2953399124f0cbb46d2cbacd8a89cf0599974963/99995353970554757559721471534129028266698199001274859511402524949800648966145</td>
       </tr>
       <tr>
          <td>Supply</td>
          <td>Integer</td>
          <td></td>
          <td>"supply": 1,</td>
          <td>1;;</td>
          <td>1</td>
       </tr>
       <tr>
          <td>Blockchain</td>
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
          <td>"sale_type": "Timed Auction",</td>
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
          <td>["method", price] or ["method, ""]</td>
          <td>"method": ["Sell with declining price", 0.002],
             <br>"method": ["Sell to highest bidder", 0.05],
             <br>"method": ["Sell to highest bidder", ""],</td>
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
          <td>List[String, String] or List[String] or String</td>
          <td>["from_date", "to_date"] or ["days/weeks/months"] or "days/weeks/months"</td>
          <td>"duration": ["01-01-2022 14:00", "01-04-2022 15:00"],
             <br>"duration": ["1 week"],
             <br>"duration": "1 week",
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
          <td>List[Boolean, String] or [Boolean] or Boolean</td>
          <td>[True, "wallet"] or [False] or False</td>
          <td>"specific_buyer": [true, "0xDD135d5be0a23f6daAAE7D2d0580828c9e09402E"]
              <br>"specific_buyer": [false]
              <br>"specific_buyer": false</td>
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
          <td>"quantity": 4</td>
          <td>4</td>
          <td>4</td>
       </tr>
    </tbody>
 </table>

And it gives you something like this: [CSV](https://github.com/maximedrn/opensea_automatic_uploader/blob/master/data/csv_structure_sale_only.csv), [JSON](https://github.com/maximedrn/opensea_automatic_uploader/blob/master/data/json_structure_sale_only.json), [XLSX (must be downloaded to view it)](https://github.com/maximedrn/opensea_automatic_uploader/blob/master/data/xlsx_structure_sale_only.xlsx).


## Configuration of the sales part of the NFTs:

When you want to sell your NFTs, Opensea requires various details according to their Blockchain or supply number.

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
   <td><strong>Duration</strong> (from a date to an other date or 1 day, 3 days, 1 week, 6 months)</td>
   <td>Reserve for a <strong>specific buyer</strong></td>
   
   <td><strong>Price</strong> (ETH)</td>
   <td><strong>Duration</strong> (from a date to an other date or 1 day, 3 days, 1 week)</td>
   <td>Reserve for a <strong>specific buyer</strong></td>
   <td><i>(Optional)</i> <strong>Reserved Price</strong> (WETH) greater than 1 WETH and greater than <strong>Starting Price</strong>.</td>
   
   <td><strong>Starting Price</strong> (ETH)</td>
   <td><strong>Duration</strong> (from a date to an other date or 1 day, 3 days, 1 week)</td>
   <td><strong>Ending Price</strong> (ETH) less than the<strong>Starting Price</strong>.</td>
   <td>Reserve for a <strong>specific buyer</strong></td>
   
   <td><strong>Quantity</strong></td>
   <td><strong>Price</strong> (ETH)</td>
   <td><strong>Duration</strong> (from a date to an other date or 1 day, 3 days, 1 week, 6 months)</td>
   <td>Reserve for a <strong>specific buyer</strong></td>
   
   <td><strong>Price</strong> (ETH)</td>
   <td><strong>Duration</strong> (from a date to an other date or 1 day, 3 days, 1 week, 6 months)</td>
   <td>Reserve for a <strong>specific buyer</strong></td>
   
   <td><strong>Quantity</strong></td>
   <td><strong>Price</strong> (ETH)</td>
   <td><strong>Duration</strong> (from a date to an other date or 1 day, 3 days, 1 week, 6 months)</td>
   <td>Reserve for a <strong>specific buyer</strong></td>
  </tr>
 </tbody>
</table>


## Known issues and important things to know:

* **If you use a JSON file for your NFT data, the file path should not contain a unique "\\". It can be a "/" or a "\\\\":**
```json
// You can use this format for your path:
"file_path": "C:/Users/Admin/Desktop/MyNFTs/nft_0001.png",
// or this one:
"file_path": "C:\\Users\\Admin\\Desktop\\MyNFTs\\nft_0001.png",
// but not this one (you can see that "\" is highlighted in red):
"file_path": "C:\Users\Admin\Desktop\MyNFTs\nft_0001.png",
```
* The bot may crash at the beginning when loading the MetaMask extension (a Selenium module issue), An error like the one below should appear:  
```
selenium.common.exceptions.WebDriverException:
Message: unknown error: failed to wait for extension background page to load:
chrome-extension://nkbihfbeogaeaoehlefnkodbefpgknn/background.html from timeout:
Timed out receiving message from renderer: 10.000
```
