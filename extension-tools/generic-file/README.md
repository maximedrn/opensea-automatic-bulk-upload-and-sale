# Automatically create a file that is fully ready for upload, sale or both using a generic 21-detail file.
_A Python bot to automatically create a fully ready file for upload, sale or both._

---

**Please ensure that [OpenSea Automatic Bulk Upload and Sale](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale) bot works on your computer before reading and purchasing this repository**.  
Please read the README file before using this tool, opening a problem or a discussion, or contacting me.  
⇒ Open an issue? Provide your operating system and detail your error.  
⇒ Make sure you have the latest modules and bot installed.  
⇒ Read the pinned and opened issues.

---

* **(_Version 1.0.0 - April 09, 2022_).**

# Table of contents

* **[What does this bot do?](#what-does-this-bot-do)**
* **[Changelog](#changelog).**
* **[Instructions](#instructions)**.
  * [Basic installation of Python for beginners](#basic-installation-of-python-for-beginners).
  * [Configuration of the bot](#configuration-of-the-bot).
  * [Run the bot](#run-the-bot).

## What does this bot do?

This script allows you to generate a whole file from a generic file or to modify a file by replacing massively some values by others.

You just have to fill a simple generic file with 21 details (18 for NFTs and 3 for formatting and file parameters) and run the script. Your file will be generated with common values for all your NFTs.

## Changelog

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
