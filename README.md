<h1 align="center">Automatically and massively upload and list your non-fungible tokens on the OpenSea marketplace using Python Selenium.</h1>

<p align="center"><i>A Selenium Python bot to automatically and bulky upload and list your NFTs on OpenSea.
<br />All metadata integrated - Ethereum and Polygon supported - reCAPTCHA solver services included.</i>
<br><strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/wiki/Changelog">Version 1.10.8</a> (August 30, 2022).</strong></p>

<p align="center" width="50%"><strong>Need help or have a specific request?</strong>
<br />Look at my offers on <strong><a href="https://fiverr.com/maximedrn/">Fiverr <img src="https://user-images.githubusercontent.com/91475935/169694667-68824ed9-10a3-46ee-9fc1-23ec91496121.png" height="15px" /></a></strong> to help you to create your metadata file and install the bot.  
<br />Contact me via <strong><a href="https://t.me/maximedrn">Telegram</a></strong> or e-mail me at <strong><a href="mailto:maxime_drean@yahoo.com">maxime_drean@yahoo.com</a></strong>.<p>

<div align="center"><hr width="30%" /></div>

<h2>OpenSea Workshop - <i><a href="https://www.youtube.com/watch?v=V3PojmcPoCI">Demonstration video</a></i> <img src="https://user-images.githubusercontent.com/91475935/187707252-3a304735-6a88-46c4-8c17-af882eb8b4bd.png" height="16px" /></h2>

<a href="https://maximedrn.gumroad.com/l/opensea-workshop"><img src="https://user-images.githubusercontent.com/91475935/187708584-ad849d7b-f247-40c3-b6ed-63b61f83e337.png"></a>


<h3>You find the installation of this tool too complicated?</h3>
<p>Well, with the <a href="https://maximedrn.gumroad.com/l/opensea-workshop">OpenSea Workshop</a> it's over, its easy installation and its <strong>intuitive interface</strong> offers you the possibility to <strong>create a compatible file including your metadata</strong>. You can <strong>upload</strong>, <strong>put on sale</strong> and <strong>delete</strong> NFTs, but also <strong>scrape your collection(s) in order to find duplicates and missing items</strong>.
<br /><i><strong><a href="https://maximedrn.gumroad.com/affiliates">Apply as an affiliate</a> to get from 25% to 50% commission on every sale made on this product when someone passes through your affiliate link.</strong> The commission increases by 1% for each sale up to a maximum of 50%.</i></p>

<br />
<h2>Table of contents - <a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/wiki">Documentation</a> - <i><a href="https://www.youtube.com/watch?v=DdqGEz0BCQ8">Complete tutorial</a></i> <img src="https://user-images.githubusercontent.com/91475935/187707252-3a304735-6a88-46c4-8c17-af882eb8b4bd.png" height="16px" /></h2>

<ul>
<li><strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/wiki/Home#introduction">Introduction</a>, what does this bot do and how does it works?</strong></li>
<li><strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/wiki/Home#frequently-asked-questions">Frequently Asked Questions</a> about the creation of the metadata file and reCAPTCHA solver services.</strong></li>
<li><strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/wiki/Installation-and-configuration">Installation and configuration</a> of Python, the required modules and the bot.</strong></li>
<li><strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/wiki/Creation-of-the-metadata-file">Creation of the metadata file</a>, discover its structure.</strong></li>
<li><strong>➜ <a href="#useful-tools-to-have-for-this-bot">Useful tools to have for this bot</a></strong></li>
<ul>
<li><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/wiki/File-Compatibilizer-&-Converter">File Compatibilizer & Converter</a>, from the HashLips Art Engine metadata files to one compatible file.</li>
<li><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/wiki/Generic-File-Maker">Generic File Maker</a>, complete your metadata file easily and quickly.</li>
<li><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/wiki/Collection-Scraper">Collection Scraper</a>, retrieve the URLs of your NFTs and get the duplicates and missing.</li>
<li><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/wiki/reCAPTCHA-Bypasser">reCAPTCHA Bypasser</a>, instantly solve the reCAPTCHAs.</li>
<li><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/wiki/Multiprocessing">Multiprocessing</a>, for lightning-fast uploading.</li>
<li><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/wiki/Deletion">Deletion</a>, delete all the duplicate and unwanted NFTs.</li>
</ul>
<li><strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/wiki/Changelog">Changelog</a>, new fixes and features.</strong></li>
</ul>

<h2>Introduction</h2>

<p>With this bot, <strong>you can choose to upload, list or even both your non-fungible tokens</strong> on the OpenSea marketplace.</p>

<p>You just have to <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/wiki/Creation-of-the-metadata-file">create or convert a metadata file</a></strong> following the requested structure, JSON, CSV and XLSX (Excel file) formats are available. This file will include every detail for each NFT. Then, you just have to <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/wiki/Installation-and-configuration">launch the bot</a></strong> and <strong>select the action you want to perform</strong>, as well as the metadata file created. Finally, <strong>the bot will automate the tedious task of uploading or listing NFTs, one by one by hand, for several days</strong>.</p>

<ul>
<li>Absolutely <strong>all upload details are supported</strong>, you can add as many properties as you want.</li>
<li><strong>All file formats</strong> offered by OpenSea <strong>are compatible</strong>, including images, videos or even 3D models.</li>
<li><strong>Ethereum and Polygon blockchains are supported</strong>, and the switch between these two blockchains is also supported.</li>
<li>In case of failure during an upload, a listing or when you only want to upload your NFTs on OpenSea, <strong>a file is generated with details already filled</strong> in or to be filled in.</li>
</ul>

<h2>Useful tools to have for this bot</h2>

<ul>
<li>
<h3>File Compatibilizer & Converter</h3>

<p>Using the <strong><a href="https://maximedrn.gumroad.com/l/opensea-file-compatibilizer">File Compatibilizer and Converter</a></strong>, you can <strong>convert all JSON files generated with the <a href="https://github.com/HashLips/hashlips_art_engine">HashLips Art Engine</a> tool into a single compatible file</strong>. The tool ignores the file named <code>_metadata.json</code> and focuses on all other files listed. It <strong>retrieves each of the information containing them such as attributes</strong> and properties and adds them into a single file.</p>

<div align="center"><hr width="30%" /></div>

<li>
<h3>Generic File Maker</h3>

<p>Using the <strong><a href="https://maximedrn.gumroad.com/l/opensea-generic-file">Generic File Maker</a></strong>, you can <strong>complete your JSON metadata file using a simple generic file that contains 21 details</strong>, 18 about NFTs and 3 about how the tool works. It supports increment value, for example if you name your assets (images or videos) from 1 to 10000, you can <strong>in one line complete all the file paths of the metadata file</strong>.</p>
</li>

<div align="center"><hr width="30%" /></div>

<li>
<h3>Collection Scraper</h3>

<p>Using the <strong><a href="https://maximedrn.gumroad.com/l/opensea-collection-scraper">Collection Scraper</a></strong>, you can <strong>retrieve the URLs of the NFTs of any collection</strong>. It makes it easier to manage your collection, you can now know which NFTs are missing, which ones are duplicated. It facilitates the listing of your NFTs by <strong>creating different files compatible with the <code>Sale Only</code> option.</strong></p>

<p>Thus a <code>full</code> file containing all NFTs, a <code>unique</code> file containing each NFT individually based on their names, a <code>duplicate</code> file containing all duplicated NFTs of the collection and a <code>missing</code> file containing all missing NFTs will be created, and these in all formats compatible with the bot (JSON, CSV and XLSX).</p>
</li>

<div align="center"><hr width="30%" /></div>

<li>
<h3>reCAPTCHA Bypasser</h3>

<p>Using the <strong><a href="https://maximedrn.gumroad.com/l/opensea-no-recaptcha">reCAPTCHA Bypasser</a></strong>, you can <strong>instantly solve reCAPTCHAs when uploading to OpenSea</strong>. This maximizes the upload speed on OpenSea, <strong>the average 30 second wait time of other solvers no longer exists with this solver</strong>. It uses an exploit to bypass the reCAPTCHA. The upload speed is such that there would be no reCAPTCHA.</p>

<p>The <a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/wiki/reCAPTCHA-Bypasser">reCAPTCHA Bypasser</a> allows an instant solve of the reCAPTCHAs. Up to <strong>400 NFTs per hour</strong>, or <strong>10,000 NFTs in one day</strong> with one process. Watch this <a href="https://www.youtube.com/watch?v=oSqIqbuFnn0">video</a> to see <strong>how fast</strong> the upload is with this exploit!</p>

https://user-images.githubusercontent.com/91475935/177582923-2ea6cf2b-17a4-4cf0-ba00-49410cde6fc1.mp4
</li>

<div align="center"><hr width="30%" /></div>

<li>
<h3>Multiprocessing</h3>

<p>Using the <strong><a href="https://maximedrn.gumroad.com/l/opensea-multiprocessing">Multiprocessing</a></strong> tool, you can upload your NFTs faster and with several processes running at the same time. You can have up to 5 simultaneous processes depending on the power of your computer. It splits your file into several sub-files, then opens several command prompts that work like the main bot but at the same time: it connects to your wallet, connects to OpenSea and starts the upload or listing task.</p>
</li>

<div align="center"><hr width="30%" /></div>

<li>
<h3>Deletion</h3>

<p>Using the <strong><a href="https://maximedrn.gumroad.com/l/opensea-deletion">Deletion</a></strong> tool, you can <strong></strong> delete any NFT on OpenSea. It is compatible with the <a href="https://maximedrn.gumroad.com/l/opensea-collection-scraper">Collection Scraper</a> which creates files for duplicated NFTs or for an entire collection.</p>
</li>

<div align="center"><hr width="30%" /></div>

<p align="center">If you like 💚 my work and this tool, do not hesitate to
<br /><strong>fork 🍴</strong> this repository and <strong>add a star ⭐</strong> to this repository.</p>
