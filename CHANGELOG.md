# Changelog

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
