<p align="center">In order to have the best experience and performance with this tool, make sure to use the latest version.</p>

<hr />

<h3>Version 1.11.0</h3>
<ul>
<li>Modification of the system which reduces memory usage.</li>
<li>Added new checkers for the collection URL to avoid errors when its value is slightly incorrect.</li>
<li>Images are now disabled in processes to improve speed.</li>
</ul> 


<strong>Version 1.10.9</strong>
<ul>
<li>Added a conversion from <code>1 week</code> to <code>7 days</code>.</li>
<li>Correction of an error when the reserve price is equal to <code>''</code> (default value when there is no reserve price).</li>
</ul> 

<strong>Version 1.10.8</strong>
<ul>
<li>Fixed an issue in the console when using the custom Google Chrome profile.</li>
<li>Added a setting to disable the GPU on Google Chrome (problems occurred with the virtual machine when it was enabled)..</li>
</ul> 

<strong>Version 1.10.7</strong>
<ul>
<li>It now automatically changes the working directory to avoid problems.</li>
<li>When you browse a data file, the File Explorer window is now in the foreground.</li>
</ul> 

<strong>Version 1.10.6</strong>
<ul>
<li>Fixed an issue with supply when uploading in a collection.</li>
</ul> 

<strong>Version 1.10.5</strong>
<ul>
<li>Increased the speed of the bot by easing the memory only once in 10 times.</li>
</ul>

<strong>Version 1.10.4</strong>
<ul>
<li>Added support for transferring the reCAPTCHA Bypasser class instance from the Multiprocessing tool.</li>
</ul>

<strong>Version 1.10.3</strong>
<ul>
<li>Removed the <code>collection()</code> function to search for a collection in the dropdown list. The collection can be accessed from the URL.</li>
</ul>

<strong>Version 1.10.2</strong>
<ul>
<li>The input of the collection is now deleted before typing the name of the collection.</li>
</ul>

<strong>Version 1.10.1</strong>
<ul>
<li>Fixed a problem with the webdriver path on MacOS and Linux when it was impossible to download it automatically.</li>
<li>It is now possible to choose a starting value in your metadata file, this avoids using the <code>divide.py</code> file.</li>
</ul>

<strong>Version 1.10.0</strong>
<ul>
<li>Fixed the bug about a lack of memory that made the bot stop after a certain number of uploads or listings.
<br />The error was due to the bot being too fast, which prevented the memory from being emptied.
<br />From now on, the bot waits between 2 and 5 seconds on a blank <code>data:,</code> page, so that the memory rests and decreases drastically.
<br />Moreover, this may improve the listing on the Ethereum blockchain since it is limited.</li>
</ul>

<strong>Version 1.9.8</strong>
<ul>
<li>Changed some functions called on upload or listing failure to put them in a <code>try/except</code> to avoid exceptions.
<br /> <i>Feedback is needed.</i></li>
<li>Remove the <code>try/except</code> in the <code>process()</code> function.</li>
</ul>

<strong>Version 1.9.7</strong>
<ul>
<li>Fixed an issue with the automatic saving of properties, levels and stats when an upload fails.</li>
<li>Added a <code>try/except</code> in the <code>process()</code> function to avoid abrupt stops.</li>
</ul>

<strong>Version 1.9.6</strong>
<ul>
<li>Listing now works perfectly on Ethereum. The only case of failure is the <code>Failed to fetch</code> error that sometimes appears.
<br />In this case, it will retry until the item is listed.</li>
</ul>

<strong>Version 1.9.5</strong>
<ul>
<li>Added an exception to not stop the bot when it fails to save the metadata in a file.</li>
<li>Attempt to improve the listing on Ethereum between errors.</li>
</ul>

<strong>Version 1.9.4</strong>
<ul>
<li>Added a function that checks if the NFT is already listed or not for the <code>Sale Only</code>.</li>
</ul>

<strong>Version 1.9.3</strong>
<ul>
<li>Fixed the value checker for the different duration format.</li>
</ul>

<strong>Version 1.9.2</strong>
<ul>
<li>Replaced <code>Keys.ENTER</code> by <code>Keys.RETURN</code> to make the toggle button switchable on MacOS.</li>
<li>Added a value checker for the date due to the different format of OpenSea (<code>DD-MM-YYYY</code> or <code>MM-DD-YYYY</code>).</li>
</ul>

<strong>Version 1.9.1</strong>
<ul>
<li>Fixed the <code>clear_text()</code> method for Linux systems.</li>
</ul>

<strong>Version 1.9.0</strong>
<ul>
<li>You can now use this bot with your own Google Chrome profile, without the need to import your wallet. It only requires your password.</li>
<li>Changing the way credentials are stored from different files into a single JSON file.</li>
</ul>

<strong>Version 1.8.4</strong>
<ul>
<li>Fixed the private key import on the GeckoDriver.</li>
<li>Fixed the Ethereum contract signature on the ChromeDriver.</li>
<li>Fixed the login to MetaMask on the GeckoDriver.</li>
<li>Improved the login to MetaMask on the ChromeDriver.</li>
</ul>

<strong>Version 1.8.3</strong>
<ul>
<li>Fixed an error with SLL when checking for the bot version.</li>
</ul>

<strong>Version 1.8.2</strong>
<ul>
<li>Fixed properties, levels and stats when saving the file automatically.</li>
<li>Correction of the <code>divide.py</code> file.</li>
</ul>

<strong>Version 1.8.1</strong>
<ul>
<li>Added a feature to check if a red error message is displayed at the bottom right of the screen during listing.</li>
<li>You can now choose the number of failures allowed by the bot (edit the <code>app/utils/const.py</code> file).</li>
<li>Fixed wrong path when trying to access <code>assets/geckodriver.exe</code> when it can&#39;t download it automatically.</li>
</ul>

<strong>Version 1.8.0</strong>
<ul>
<li>Add a version check at the beginning of the bot.</li>
</ul>

<strong>Version 1.7.19</strong>
<ul>
<li>Generated metadata files are now saved in a JSON format.</li>
<li>Metadata files generated from an &quot;Upload and Sale&quot; used for an &quot;Upload only&quot; are now fully completed.</li>
<li>Fixed incomplete generated file for &quot;Sale only&quot;.</li>
<li>Improved the detection of listed NFTs.  <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/319">#319</a></strong>.</li>
<li>Removed the 404 page error check for the upload that causes a duplicate upload.  <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/319">#319</a></strong>.</li>
</ul>

<strong>Version 1.7.18</strong>
<ul>
<li>Fixed switching and signing on Polygon.</li>
<li>Fixed bot stopping when it tried to check a 404 page error on a MetaMask popup.</li>
<li>Added the path of extensions when it raises an error when it can&#39;t find them.</li>
</ul>

<strong>Version 1.7.17</strong>
<ul>
<li>Re-add the account change with the private key.</li>
<li>Metadata files no longer appear with the full path.</li>
</ul>

<strong>Version 1.7.16</strong>
<ul>
<li>Fixed the duration problem with the <code>[&quot;DD-MM-YYYY&quot;, &quot;DD-MM-YYYY&quot;]</code> format.</li>
<li>Created a specific function for the 404 page error.</li>
<li>Fixed the problem of the switch to Polygon, the click on the button &quot;Switch&quot; is no longer necessary.</li>
</ul>

<strong>Version 1.7.15</strong>
<ul>
<li>Added detection for the &quot;This page is lost&quot; and &quot;Oops! Something went wrong&quot; messages.</li>
</ul>

<strong>Version 1.7.14</strong>
<ul>
<li>Fixed the problem when the Webdriver-Manager module could not download a webdriver and created an infinite loop because of a missing function return.</li>
<li>Added the display of an error when something goes wrong when starting the webdriver.</li>
<li>Added a file to order your file according to the name of your NFTs, this is useful when you want to complete your file with the <a href="Generic-File-Maker">Generic File Maker</a>.  </li>
</ul>

<strong>Version 1.7.13</strong>
<ul>
<li>Fixed a problem when no collection is mentioned in the metadata file and a default collection is used on OpenSea. The upload was leading to an error.</li>
<li>Added a file to split your metadata file when you want to restart the process after stopping it.</li>
</ul>

<strong>Version 1.7.12</strong>
<ul>
<li>Fixed the listing problems. <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/300">#300</a></strong>.</li>
</ul>

<strong>Version 1.7.11</strong>
<ul>
<li>Fixed the &quot;Sale Only&quot; problem. <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/300">#300</a></strong>.</li>
<li>Replaced the change of account with the private key by the name of the account.</li>
</ul>

<strong>Version 1.7.10</strong>
<ul>
<li>Added line break support for description (add a <code>\n</code> to break the line).</li>
<li>Minor fixes.</li>
<li>Added support with the new version of the <a href="Multiprocessing">Multiprocessing</a> tool.</li>
</ul>

<strong>Version 1.7.9</strong>
<ul>
<li>Minor corrections for the contract signature on MetaMask.</li>
<li>Fixed an error that sometimes occurred when the collection is not mentioned.</li>
</ul>

<strong>Version 1.7.8</strong>
<ul>
<li>Correction of the listing on Polygon when the option &quot;Upload and Sale&quot; is selected.</li>
</ul>

<strong>Version 1.7.7</strong>
<ul>
<li>You can now choose whether you want to configure your wallet manually or not.</li>
<li>Minor changes.</li>
</ul>

<strong>Version 1.7.6</strong>
<ul>
<li>Fixed failure of the contract signature on Polygon blockchain. <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/288">#288</a></strong>.</li>
</ul>

<strong>Version 1.7.5</strong>
<ul>
<li>Added support for the <a href="Deletion">OpenSea Deletion</a> tool.</li>
<li>Minor fixes about the listing part.</li>
</ul>

<strong>Version 1.7.4</strong>
<ul>
<li>Correction of the listing in loop after a failure.</li>
<li>Correction of an incorrect file for the generated listing file.</li>
<li>Minor corrections and modifications.</li>
</ul>

<strong>Version 1.7.3</strong>
<ul>
<li>Added support for a new <a href="reCAPTCHA-ypasser">reCAPTCHA bypasser</a> exploit.</li>
</ul>

<strong>Version 1.7.2</strong>
<ul>
<li>Modification of the <code>main.py</code> file to make it more compatible with the new future tools.</li>
<li>Fixed <code>list index out of range</code> error with unlockable content.</li>
</ul>

<strong>Version 1.7.1</strong>
<ul>
<li>Fixed the several issues with the Coinbase Wallet. <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/278">#278</a></strong>.</li>
</ul>

<strong>Version 1.7.0</strong>
<ul>
<li>Split the <code>main.py</code> file into different structures to make the bot more modular and compatible with future tools.</li>
<li>Fixed the problem of connecting to OpenSea which opens a tab to download MetaMask.</li>
</ul>

<strong>Version 1.6.14</strong>
<ul>
<li>Fixed the problem of the URL with the &quot;Sale only&quot;.</li>
<li>Minor fixes.</li>
</ul>

<strong>Version 1.6.13</strong>
<ul>
<li>Improved manual resolution for reCAPTCHA. <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/264">#264</a></strong>.</li>
<li>Fixed some issues with blockchain change. <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/262">#262</a></strong>.</li>
<li>Minor fixes.</li>
</ul>

<strong>Version 1.6.12</strong>
<ul>
<li>Added support for blockchain switching on MetaMask (need feedback - may not work with Coinbase Wallet). <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/262">#262</a></strong>.</li>
<li>Fixed <code>list index out of range</code> error with reCAPTCHA solver using CUDA. <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/263">#263</a></strong>.</li>
<li>Removed unnecessary printouts used during development.</li>
<li>Minor corrections for sale part.</li>
</ul>

<strong>Version 1.6.11</strong>
<ul>
<li>Fixed the problem with the collection. <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/258">#258</a></strong>.</li>
<li>Fixed 2Captcha callback function. <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/259">#259</a></strong>.</li>
<li>Fixed the problem with downloading the pre-trained file (<code>urllib.error.URLError: urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate</code>) by changing the download method.</li>
</ul>

<strong>Version 1.6.10</strong>
<ul>
<li>Fixed restarting the upload or sale when it fails the first time. <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/253">#253</a></strong>.</li>
<li>Minor correction concerning the connection to OpenSea: the bot made the browser restart instead of trying a second time.</li>
</ul>

<strong>Version 1.6.9</strong>
<ul>
<li>Added a new feature for collections. You can now use the URL format of your collection. This can solve the problem of collections not being found or clicked in the  list.<br>From <code>Crypto Parrot NFTs</code> to <code>crypto-parrot-nfts</code>, depending on the URL of your collection: <code>https://opensea.io/collection/crypto-parrot-nfts/</code>.</li>
<li>Minor fixes about version 1.6.9.</li>
</ul>

<strong>Version 1.6.8</strong>
<ul>
<li>Added support for the 2Captcha API. <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/239">#239</a></strong>.</li>
<li>Minor fixes.</li>
</ul>

<strong>Version 1.6.7</strong>
<ul>
<li>Improved MetaMask wallet switching, you can use the default account by skipping this step.</li>
<li>Fixed the <code>gateway</code> problem. <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/249">#249</a></strong>.</li>
</ul>

<strong>Version 1.6.6</strong>
<ul>
<li>You can now select the wallet you want to use with MetaMask (many thanks to <strong><a href="https://github.com/EmilianoBruni">EmilianoBruni</a></strong>!). <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/36">#36</a>, <a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/103">#103</a></strong>.<br><em><a href="https://metamask.zendesk.com/hc/en-us/articles/360015289632-How-to-Export-an-Account-Private-Key">How to get my private key?</a></em></li>
</ul>

<strong>Version 1.6.5</strong>
<ul>
<li>Merge the <code>main.py</code> and <code>main-manual-resolution.py</code> files.</li>
<li>Dissociation of the requirements files, one for the bot and one for the reCAPTCHA solver.</li>
</ul>

<strong>Version 1.6.4</strong>
<ul>
<li>The bot did not go to the sale page after the sequence of a failure and a success. <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/225">#225</a></strong>.</li>
</ul>

<strong>Version 1.6.3</strong>
<ul>
<li>Added support for Coinbase Wallet (many thanks to <strong><a href="https://github.com/MathieuAndrade">MathieuAndrade</a></strong>!).</li>
</ul>

<strong>Version 1.6.2</strong>
<ul>
<li>Wyvern 2.3 contract signature fixed for ChromeDriver and GeckoDriver. <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/152">#152</a>, <a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/165">#165</a>, <a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/183">#183</a>, <a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/201">#201</a></strong>.</li>
<li>Minor corrections and improvements.</li>
<li>Yolov5x6 and Real-ESRGAN models, and the <code>recaptcha.py</code> file are not loaded when the &quot;Sale only&quot; option is selected.</li>
</ul>

<strong>Version 1.6.1</strong>
<ul>
<li>Updated the <code>requirements.txt</code> file, conflicts and problems seem to be corrected.</li>
<li>Removed unnecessary files from the <code>yolov5/</code> directory.</li>
<li>Fixed the problem of connection to OpenSea.</li>
<li>Improved reCAPTCHA verification when solved.</li>
</ul>

<strong>Version 1.6.0</strong>
<ul>
<li>The OpenSea connection problem seems to be fixed. An open tabs check has been added. <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/159">#159</a>, <a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/167">#167</a>, <a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/181">#181</a>, <a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/187">#187</a></strong>.</li>
<li>reCAPTCHA solver added (Real ESRGAN + Yolov5x6 models used with PyTorch). <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/157">#157</a>, <a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/179">#179</a>, <a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/186">#186</a></strong>.<br>➜ Future improvements: models of crosswalks, chimneys, bridges.</li>
</ul>

<strong>Version 1.5.12</strong>
<ul>
<li>Wyvern 2.3 contract support (need feedbacks). <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/152">#152</a>, <a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/161">#161</a>, <a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/165">#165</a></strong>. </li>
</ul>

<strong>Version 1.5.11</strong>
<ul>
<li><strike>Correction of the MetaMask contract signature (feedback needed).</strike> <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/144">#144</a></strong>.</li>
<li><strike>Wyvern 2.3 contract support (beta - need feedbacks).</strike> <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/152">#152</a></strong>.</li>
<li><em>In progress: improved support for MacOS (M1) - duration and contract list issues.</em></li>
</ul>

<strong>Version 1.5.10</strong>
<ul>
<li>Minor fixes concerning the <code>sale()</code> method of the OpenSea class.</li>
<li>Fixed exception iteration error.</li>
</ul>

<strong>Version 1.5.9</strong>
<ul>
<li>The <code>close()</code> method of the Webdriver class has been fixed. It creates an exception when listing NFTs. As a result, it does not try to list them a second time. <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/144">#144</a>, <a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/145">#145</a>, <a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/149">#149</a></strong>.</li>
<li>During the download, when the webdriver starts, sometimes an error occurs and creates an exception. It was supposed to close the webdriver but it caused the bot to crash.</li>
<li>The download of webdriver requires a manual entry of the path after a number of failures.</li>
</ul>

<strong>Version 1.5.8</strong>
<ul>
<li>Errors related to incorrectly formatted files are now supported. An error is displayed but the bot does not stop abruptly. <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/90">#90</a></strong>.</li>
<li>False listing errors are reduced, the robot checks a second time if the NFT is correctly listed.</li>
</ul>

<strong>Version 1.5.7</strong>
<ul>
<li>With each failed upload or sale, the bot retries a second time before saving the NFT data in an autogenerated file.</li>
<li>The duration has been fixed for GeckoDriver (Mozilla Firefox).  <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/121">#121</a></strong>.</li>
</ul>

<strong>Version 1.5.6</strong>
<ul>
<li>The <code>dict_to_list()</code> method has been optimized and shortened.</li>
<li>Minor fixes.</li>
</ul>

<strong>Version 1.5.5</strong>
<ul>
<li>Fixed the <code>metamask_contract()</code> method. It was not signing the contract when completing the listing for the Ethereum Blockchain.</li>
<li>Minor fixes.</li>
</ul>

<strong>Version 1.5.4</strong>
<ul>
<li>The HTTPConnectionPool error in Selenium is fixed, it was caused by defining the driver inside a loop. Now the bot will print an error and restart to launch the bot. <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/112">#112</a></strong>.<br>➜ For more informations: <strong><a href="https://www.reddit.com/r/selenium/comments/cuynft/comment/f85odbh/?utm_source=share&amp;utm_medium=web2x&amp;context=3">Reddit - Ralphc360&#39;s comment</a></strong>.</li>
<li>You can now sell your NFTs on the Ethereum Blockchain for free.</li>
</ul>

<strong>Version 1.5.3</strong>
<ul>
<li>Fixed the Webdriver-Manager module, it was downloading the ChromeDriver or GeckoDriver at each webdriver launch. Now it uses the path of the downloaded webdriver. <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/112">#112</a></strong>.</li>
<li>Fixed the collection input. <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/108">#108</a></strong>.</li>
</ul>

<strong>Version 1.5.2</strong>
<ul>
<li>Headless mode support. Download Mozilla Firefox and you can use this bot in the background without any interface.
Note: Firefox may be unstable and some features may work differently or not at all.  <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/64">#64</a>, <a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/discussions/69">#69</a>, <a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/106">#106</a></strong>.</li>
<li>Fixed the connection to the MetaMask success indicator.</li>
</ul>

<strong>Version 1.5.1</strong>
<ul>
<li>Fixed the problem of the worker version 1.5.0. The bot now continues to upload and does not restart the upload from the beginning. <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/107">#107</a></strong>.</li>
</ul>

<strong>Version 1.5.0</strong>
<ul>
<li>The reCAPTCHAs can now be bypassed. The bot restarts for each upload - it&#39;s a bit slow but it works. <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/98">#98</a>, <a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/pull/102">#102</a></strong>.<br>Thanks to <strong><a href="https://github.com/Kanishka-Chandra">Kanishka-Chandra</a></strong> and <strong><a href="https://github.com/elwanm">elwanm</a></strong>.</li>
<li>The bot restarts after 3 failed connections to the wallet or to OpenSea.</li>
</ul>

<strong>Version 1.4.9</strong>
<ul>
<li>Minor fixes.</li>
<li>Developers can now add new wallets if they wish.</li>
<li>ChromeDriver is automatically downloaded - no need to do it manually (<code>pip install -r requirements.txt</code> required).</li>
<li><em>The reCAPTCHAs solver is not integrated/configured.</em></li>
</ul>

<strong>Version 1.4.8</strong>
<ul>
<li><strike>Added a new feature that allows to upload more than 50 items in a collection. Requires to be activated (asked at launch).</strike> (Method used: <a href="https://www.youtube.com/watch?v=8wpmjh8xrXo">https://www.youtube.com/watch?v=8wpmjh8xrXo</a>). <strong>Update:</strong> This method is useless because <a href="https://twitter.com/opensea/status/1486843201352716289">OpenSea went back on its words</a>. The limit has been removed.</li>
<li>Minor fix.</li>
</ul>

<strong>Version 1.4.7</strong>
<ul>
<li>The default language of ChromeDriver is now English to ensure maximum compatibility. The date did not work in some countries because of the different formats that OpenSea offers. <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/67">#67</a></strong>.</li>
<li>Minor fix (Colorama module).</li>
</ul>

<strong>Version 1.4.6</strong>
<ul>
<li>The duration has been corrected. OpenSea does not allow to change the year when the next year is more than 6 months away. So it was impossible to enter the month without it being replaced by December (12 - maximum number because the year was entered instead); <strong>Note: maximum duration is 6 months. <a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/55">#55</a></strong>.</li>
<li>The connection to OpenSea has <em>certainly</em> been corrected. (need feedback about this - I don&#39;t have any problems on my side). <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/53">#53</a>, <a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/58">#58</a>, <a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/61">#61</a></strong>.</li>
</ul>

<strong>Version 1.4.5</strong>
<ul>
<li>Minor fix for Linux users. The <code>clear_text(self)</code> method inserts an &quot;A&quot; when it tries to clear the inputs before sending the data. <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/39">#39</a></strong>.</li>
</ul>

<strong>Version 1.4.4</strong>
<ul>
<li>Connection to OpenSea with MetaMask corrected. Download of the extension was requested. <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/53">#53</a></strong>.</li>
<li>Connection to OpenSea with MetaMask improved.</li>
</ul>

<strong>Version 1.4.3</strong>
<ul>
<li>File preview is now added. <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/48">#48</a></strong>.</li>
</ul>

<strong>Version 1.4.2</strong>
<ul>
<li>Listing of NFT on the Ethereum Blockchain is fully supported. <strong>Be sure to make a deposit and have more than 0.05 ETH on your wallet.</strong></li>
</ul>

<strong>Version 1.4.1</strong>
<ul>
<li>Small fix for XLSX files. Empty cells were interpreted as &quot;NaN&quot;, which is not interpreted as an empty string for Python. <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/18">#18</a>, <a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/23">#23</a></strong>.</li>
</ul>

<strong>Version 1.4.0</strong>
<ul>
<li>You can now decide whether you want to upload or sell your NFTs, or both. <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/3">#3</a>, <a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/22">#22</a></strong>.</li>
<li>Signing the MetaMask contract works every time. It can take 30 seconds to be signed when connecting to OpenSea. <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/5">#5</a>, <a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/17">#17</a></strong>.</li>
<li>After uploading the NFT, the bot would crash when it tried to sell it (the URL was not correct). Now it doesn&#39;t. <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/17">#17</a></strong>.</li>
<li>MacOS and Linux support improved.</li>
<li>Calendar method improved.</li>
</ul>

<strong>Version 1.3.0</strong>
<ul>
<li>Important fixes. <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/4">#4</a>, <a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/6">#6</a>, <a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/10">#10</a>, <a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/11">#11</a>, <a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/12">#12</a>, <a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/14">#14</a></strong>.</li>
<li>CSV file modified: separator changed (from &quot;;&quot; to &quot;;;&quot;).</li>
</ul>

<strong>Version 1.2.0</strong>
<ul>
<li>Possibility to set a price for each NFT added.<br>➜ 1+ supplies and Polygon blockchain support added.</li>
<li>Supply input issue fixed.</li>
<li>Calendar method improved.</li>
</ul>

<strong>Version 1.1.0</strong>
<ul>
<li>XLSX support added.</li>
<li>PC-wide data file browse support.</li>
<li>Properties, Stats and Levels issues fixed. <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/1">#1</a></strong>.</li>
</ul>

<strong>Version 1.0.0</strong>
<ul>
<li>Inital commit.</li>
</ul>