# Automatically convert and make compatible a file with the OpenSea upload and sale bot using Python.
_A Python bot to automatically convert and make compatible a file with the OpenSea upload and sale robot._

---

**Please ensure that [OpenSea Automatic Bulk Upload and Sale](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale) bot works on your computer before reading and purchasing this repository**.  
Please read the README file before using this tool, opening a problem or a discussion, or contacting me.  
➜ Open an issue? Provide your operating system and detail your error.  
➜ Make sure you have the latest modules and bot installed.  
➜ Read the pinned and opened issues.

---

* **(_Version 1.0.0 - April 06, 2022_).**

<a href="https://maximedrn.gumroad.com/l/opensea-file-compatibilizer">
 
![Image of the product](https://public-files.gumroad.com/vx289yn5796wyb9lkz8whfqjqai8)
 
</a>

# Table of contents

* **[What does this bot do?](#what-does-this-bot-do)**
* **[Changelog](#changelog).**
* **[Instructions](#instructions)**.
  * [Basic installation of Python for beginners](#basic-installation-of-python-for-beginners).
  * [Configuration of the bot](#configuration-of-the-bot).
  * [Run the bot](#run-the-bot).

## What does this bot do?

This script allows you to convert or make compatible a file with the bot [OpenSea Automatic Bulk Upload and Sale](https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale), **automatically** and **quickly**.

You just have to choose your file and select its file type to arrange the details in a specific order **or** the type in which you want to convert it (from `Upload` to `Upload & Sale`, from `Upload & Sale` to `Upload`, etc).

## Changelog

* **Version 1.0.0:**
  * Initial commit.

## Instructions

* ### Basic installation of Python for beginners:
  * It requires [Python](https://www.python.org/) 3.9.7+ (3.10 can be unstable) - _developped with Python 3.9.11_.
  * Install [pip](https://pip.pypa.io/en/stable/installation/) to be able to have needed Python modules.

* ### Configuration of the bot:
  * Extract the repository folder from the ZIP file, you should have a folder named  `opensea-file-compatibilizer`.
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
  * Open a command prompt in the `opensea-file-compatibilizer/` folder path.
  * Type one of these commands to run the bot:
    
    * ```
      python compatibilizer.py
      ```
    * ```
      python3 compatibilizer.py
      ```
   * Choose your file and select its file type to arrange the details in a specific order **or** the type in which you want to convert it (from `Upload` to `Upload & Sale`, from `Upload & Sale` to `Upload`, etc).
   * The file will be saved in the `data/` folder.
