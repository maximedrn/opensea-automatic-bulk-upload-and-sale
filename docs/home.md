<h1 align="center">Automatically and massively upload and list your non-fungible tokens on the OpenSea marketplace using Python Selenium.</h1>

<p align="center"><i>A Selenium Python bot to automatically and bulky upload and list your NFTs on OpenSea
<br />All metadata integrated - Ethereum and Polygon supported - reCAPTCHA solver services included.</i></p>

<div align="center"><hr width="30%" /></div>

<p align="center">If you like :green_heart: my work and this tool, do not hesitate to
<br /><strong>fork :fork_and_knife:</strong> this repository and <strong>add a star :star:</strong> to this repository.</p>

<br />
<h2>Table of contents</h2>

<ul>
<li><strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/wiki/Home#introduction">Introduction</a>, what does this bot do and how does it works?</strong></li>
<li><strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/wiki/Home#frequently-asked-questions">Frequently Asked Questions</a> about the creation of the metadata file and reCAPTCHA solver services.</strong></li>
<li><strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/wiki/Installation-and-configuration">Installation and configuration</a> of Python, the required modules and the bot.</strong></li>
<li><strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/wiki/Creation-of-the-metadata-file">Creation of the metadata file</a>, discover its structure.</strong></li>
<li><strong>Useful tools to have for this bot:</strong></li>
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

<p>You just have to <strong>create a metadata file</strong> following the requested structure, JSON, CSV and XLSX (Excel file) formats are available. This file will include every detail for each NFT. Then, you just have to <strong>launch the bot</strong> and <strong>select the action you want to perform</strong>, as well as the metadata file created. Finally, <strong>the bot will automate the tedious task of uploading or listing NFTs, one by one by hand, for several days</strong>.</p>

<ul>
<li>Absolutely <strong>all upload details are supported</strong>, you can add as many properties as you want.</li>
<li><strong>All file formats</strong> offered by OpenSea <strong>are compatible</strong>, including images, videos or even 3D models.</li>
<li><strong>Ethereum and Polygon blockchains are supported</strong>, and the switch between these two blockchains is also supported.</li>
<li>In case of failure during an upload, a listing or when you only want to upload your NFTs on OpenSea, <strong>a file is generated with details already filled</strong> in or to be filled in.</li>
</ul>


<h2>Frequently asked questions</h2>

<h3>What are the steps to follow to upload my collection to OpenSea using this bot?</h3>

<p>The steps are a bit complicated but <strong>easily understandable and accessible to everyone</strong>.</p>

<ul>
<li><p><strong>First of all</strong>, if Python is not installed on your computer, <strong>follow this <a href="installation-and-configuration.md#installation-of-python">short tutorial</a> to install it.</strong>
<br/>Then, follow this <a href="installation-and-configuration.md#installation-and-configuration-of-the-bot">tutorial</a> in order to install and configure the bot.</p></li>

<li><p><strong>The second step</strong> is to <strong>generate your NFTs</strong>, if this is not done. I advice to use the <a href="https://github.com/HashLips/hashlips_art_engine">HashLips Art Engine</a> which <strong>support the metadata</strong>.</p></li>

<li><p><strong>The third step</strong> is to create your metadata file which is the heart of your collection, it contains all the information required by OpenSea. You have two ways to do this.
<ul>
<li>The first one can be a <strong>bit long</strong>, you create manually (or with your own script) the metadata file following the procedure <a href="creation-of-the-metadata-file.md">structure</a>.</li>
<li>The second and <strong>fastest way</strong> to create your metadata file is to use 2 tools that will convert and complete the JSON metadata files generated by the <a href="https://github.com/HashLips/hashlips_art_engine">HashLips Art Engine</a>. <strong>They are called the <a href="file-compatibilizer-and-converter.md">File Compatibilizer & Converter</a> and the <a href="generic-file-maker.md">Generic File Maker</a> - <i>More details on how this step works <a href="https://www.youtube.com/watch?v=DdqGEz0BCQ8">here</a></i></strong>.</li>
</ul></p></li>

<li><p><strong>Finally</strong>, <a href="installation-and-configuration.md#how-to-run-the-bot">run the bot</a> and type the <a href="#should-i-be-worried-about-using-my-wallet-credentials">wallet credentials</a> required to connect to OpenSea, select the action depending on your choices (if you want to upload and list your NFTs, or only upload them), and select your metadata file. <strong>You will be asked to select a reCAPTCHA solver, I advise you to read this <a href="#which-recaptcha-solver-is-the-best">section</a> about it.</strong></p></li>
</ul>

<h3>Should I be worried about using my wallet credentials?</h3>

<p>According to the <strong>Rule #1</strong> of the MetaMask "Safety Tips", it is requested to <strong><code>Never share your 12-word Secret Recovery Phrase (SRP) or private keys</code></strong>.
<br /><strong>However</strong>, your wallet credentials are <strong>only used</strong> for the purpose of connecting to your wallet extension. The bot follows the procedure for the first connection to a wallet on a new browser (importing from a recovery phrase followed by creating a new password). Thus, none of this information is recovered, everything happens on your side. Moreover, you are free to choose whether or not to save your credentials in text files in the <code>assets/</code> folder.</p>

<h3>Which reCAPTCHA solver is the best?</h3>

<table>
<tbody>
<tr>
<td>&nbsp;</td>
<td><strong>reCAPTCHA bypasser</strong></td>
<td><strong>2Captcha solver</strong></td>
<td><strong>Yolov5x6 solver *</strong></td>
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
<td>From $2.99 to $4.99 per month <strong>(unlimited calls)</strong></td>
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

<p><strong>* Not compatible on MacOS and with computer that doesn't have the one of the graphics cards required.</strong></p>

<h3>Is there an easy way to get the URLs of already uploaded NFTs?</h3>

<p>A tool to retrieve URLs from NFTs is available. You can learn more about this tool <a href="collection-scraper.md">here</a>.</p>

<h3>How to find missing and duplicates NFTs in my collection?</h3>

<p>A tool to extract NFTs to get the missing and duplicates is available. You can learn more about this tool <a href="collection-scraper.md">here</a>.
<br />Then if you want to remove duplicates, you can use this tool <a href="deletion.md">here</a>.</p>

<h3>Is there a quick way to create my metadata file?</h3>

<p>A tool to generate a complete metadata file from a single file is available.
<br />You can learn more about this tool <a href="generic-file-maker.md">here</a>.</p>

<h3>I'm coming from the Hashlips Art Engine tool, how to make my files compatible?</h3>

<p>You have just generated your images and associated metadata but notice that these files are not compatible with this tool. Well, don't worry! Two tools will allow you to transform these files into one complete file compatible with this tool.
<br /><ul>
<li>The <a href="file-compatibilizer-and-converter.md">File Compatibilizer & Converter</a> will transform your files into a single compatible file.</li>
<li>However, some essential information is missing from this file. For example, if you want to add the price, the duration of the sale or the path to the generated images, videos or 3D objects, you will need the <a href="generic-file-maker.md">Generic File Maker</a>.</li>
</ul></p>

<p><strong>Watch this <a href="https://www.youtube.com/watch?v=DdqGEz0BCQ8">video</a> on YouTube, it explains step by step the process to convert and fill your metadata file.</strong></p>

<h3>How to use a custom Google Chrome profile?</h3>

<p>First of all, you need the path to <code>User Data/</code> folder which can be found <a href="https://chromium.googlesource.com/chromium/src/+/master/docs/user_data_dir.md#Default-Location">here</a> depending on your operating system, and the Profile name (default is <code>Default</code>).</strong> Then, make sure <strong>the browser and all its tabs are closed, and you are disconnected from OpenSea</strong>.</p>
