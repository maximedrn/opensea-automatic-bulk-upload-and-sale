# Automatically scrape your collections on OpenSea using Python and JavaScript Puppeteer.
_A Python and JavaScript Puppeteer bot to automatically scrape your collections on OpenSea._

---

**Please ensure that [OpenSea Automatic Bulk Upload and Sale](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale) bot works on your computer before reading and purchasing this repository**.  
Please read the README file before using this tool, opening a problem or a discussion, or contacting me.  
⇒ Open an issue? Provide your operating system and detail your error.  
⇒ Make sure you have the latest modules and bot installed.  
⇒ Read the pinned and opened issues.

---

* **(_Version 1.0.0 - April 04, 2022_).**

# Table of contents

* **[What does this bot do?](https://github.com/maximedrn/opensea-collection-scraper#what-does-this-bot-do)**
* **[Changelog](https://github.com/maximedrn/opensea-collection-scraper#changelog).**
* **[Instructions](https://github.com/maximedrn/opensea-collection-scraper#instructions)**.
  * [Basic installation of Python for beginners](https://github.com/maximedrn/opensea-collection-scraper#basic-installation-of-python-for-beginners).
  * [Basic installation of NodeJS for beginners](https://github.com/maximedrn/opensea-collection-scraper#basic-installation-of-nodejs-for-beginners).
  * [Configuration of the bot](https://github.com/maximedrn/opensea-collection-scraper#configuration-of-the-bot).
  * [Run the bot](https://github.com/maximedrn/opensea-collection-scraper#run-the-bot).

## What does this bot do?

This script allows you to scrape the URLs of NFTs from your collection, **automatically** and **quickly**. It is an extension of the [OpenSea Automatic Bulk Upload and Sale](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale) bot that facilitates the sale of NFTs already uploaded to OpenSea before, without the help of the latter.

You simply enter the name of your collection (based on the collection URL: `https://opensea.io/collection/crypto-parrot-nfts` ➜ `crypto-parrot-nfts`) and the URLs will be stored in JSON, CSV, and XLSX files that you simply fill in with the other [sale details](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale#configuration-of-the-sale-part-of-the-nfts).

## Changelog

* **Version 1.0.0:**
  * Initial commit.

## Instructions

* **Buy the [full version](https://maximedrn.gumroad.com/l/opensea-collection-scraper) of this bot on Gumroad after proceeding to these steps.**  
  ⇒ 25% discount with the code `opensea` for the first 10 who passed through [this link](https://maximedrn.gumroad.com/l/opensea-collection-scraper/opensea).

* ### Basic installation of Python for beginners:
  * It requires [Python](https://www.python.org/) 3.9.7+ (3.10 can be unstable) - _developped with Python 3.9.11_.
  * Install [pip](https://pip.pypa.io/en/stable/installation/) to be able to have needed Python modules.

* ### Basic installation of NodeJS for beginners:
  * Download and install [Node.js](https://nodejs.org/) LTS version.

* ### Configuration of the bot:
  * Extract the repository folder from the ZIP file, you should have a folder named  `opensea-collection-scraper`.
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
  * Still in your command prompt, type this command (may require ``sudo`` on MacOS and Linux and administrator privileges for Windows - a `node_modules/` folder should be created):
    
    ```
    npm install
    ```
* ### Run the bot:
  * Open a command prompt in the `opensea-collection-scraper/` folder path.
  * Type one of these commands to run the bot:
    
    * ```
      python scraper.py
      ```
    * ```
      python3 scraper.py
      ```
   * Enter the name of your collection, based on the collection URL: `https://opensea.io/collection/crypto-parrot-nfts` ➜ `crypto-parrot-nfts`.
   * JSON, CSV and XLSX files will be generated and stored in the `data/` folder of the repository.
