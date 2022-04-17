# Automatically create a file that is fully ready for upload, sale or both using a generic 21-detail file.
_A Python bot to automatically create a fully ready file for upload, sale or both._

---

**Please ensure that [OpenSea Automatic Bulk Upload and Sale](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale) bot works on your computer before reading and purchasing this repository**.  
Please read the README file before using this tool, opening a problem or a discussion, or contacting me.  
⇒ Open an issue? Provide your operating system and detail your error.  
⇒ Make sure you have the latest modules and bot installed.  
⇒ Read the pinned and opened issues.

---

* **(_Version 1.1.0 - April 17, 2022_).**

# Table of contents

* **[What does this bot do?](#what-does-this-bot-do)**
* **[Changelog](#changelog).**
* **[Instructions](#instructions)**.
  * [Basic installation of Python for beginners](#basic-installation-of-python-for-beginners).
  * [Configuration of the bot](#configuration-of-the-bot).
  * [Run the bot](#run-the-bot).
* **[How to complete the generic file?](#how-to-complete-the-generic-file)**

## What does this bot do?

This script allows you to generate a whole file from a generic file or to modify a file by replacing massively some values by others.

You just have to fill a simple generic file with 21 details (18 for NFTs and 3 for formatting and file parameters) and run the script. Your file will be generated with common values for all your NFTs.

## Changelog

* **Version 1.1.0:**
  * Added support for preview file in the generic file.
  * Fixed the problem of unlockable content to false when set to true in the data file.
* **Version 1.0.0:**
  * Initial commit.

## Instructions

* **Buy the [full version](https://maximedrn.gumroad.com/l/opensea-generic-file) of this bot on Gumroad after proceeding to these steps.**  
  ⇒ 25% discount with the code `generate` for the first 5 who passed through [this link](https://maximedrn.gumroad.com/l/opensea-generic-file/generate).
* ### Basic installation of Python for beginners:
  * It requires [Python](https://www.python.org/) 3.9.7+ (3.10 can be unstable) - _developped with Python 3.9.11_.
  * Install [pip](https://pip.pypa.io/en/stable/installation/) to be able to have needed Python modules.

* ### Configuration of the bot:
  * Extract the repository folder from the ZIP file, you should have a folder named  `opensea-generic-file`.
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
* ### Run the bot:
  * Open a command prompt in the `opensea-generic-file/` folder path.
  * Type one of these commands to run the bot:
    
    * ```
      python generic.py
      ```
    * ```
      python3 generic.py
      ```
   * Choose your generic file, select the type of the new file (`Upload`, `Sale` or `Upload & Sale`) and choose a metadata file or the lenght of the file.
   * The file will be saved in the `data/` folder.

## How to complete the generic file?

In the details part of the generic file, you have to complete with the value you want to put in your metadata file.

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
