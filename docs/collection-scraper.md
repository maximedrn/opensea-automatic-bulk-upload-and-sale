<br />
<p align="center">

<a href="https://maximedrn.gumroad.com/l/opensea-collection-scraper">
<img src="https://i.ibb.co/ZYZCz5V/Wiki-Collection-Scraper.png" alt="Collection Scraper" border="0">
</a>
<br /><br /><strong>This tool can be <a href="https://maximedrn.gumroad.com/l/opensea-collection-scraper">purchased on Gumroad</a> by using PayPal or a credit card.</strong>
<br /><i>If you cannot purchase on Gumroad or if you want to pay using crypto-currencies,
<br />contact me on <a href="https://t.me/maximedrn">Telegram</a> or send me an email at <a href="mailto:maxime_drean@yahoo.com">maxime_drean@yahoo.com</a>.
<br /><br />

</p>

<hr />

<h2>What does this tool do?</h2>

<p>
Using the <strong>Collection Scraper</strong>, you can <strong>retrieve the URLs of the NFTs of any collection</strong>. It makes it easier to manage your collection, you can now know which NFTs are missing, which ones are duplicated. It facilitates the listing of your NFTs by <strong>creating different files compatible with the <code>Sale Only</code> option or the <a href="deletion.md">Deletion</a> tool</strong>.</p>

<p>Thus a <code>full</code> file containing all NFTs, a <code>unique</code> file containing each NFT individually based on their names, a <code>duplicate</code> file containing all duplicated NFTs of the collection and a <code>missing</code> file containing all missing NFTs will be created, and these in all formats compatible with the bot (JSON, CSV and XLSX).</p>


<h2>Installation of this tool</h2>

<i>After acquiring this tool, be sure to download all the files and save the key to a file so as not to lose it.
<br>This key and the files are available in your Library on Gumroad or in the email receipt.</i>

<ul>

<li>Before proceeding to these steps, make sure that <a href="installation-and-configuration.md#installation-of-python">Python is installed</a>.</li>

<li><strong>Extract the tool folder from the ZIP archive file. Make sure all files are in the same parent folder.</strong></li>

<li><strong>Download and install</strong> <a href="https://nodejs.org/">Node.js</a> LTS version.</li>

<li><strong>Open a command prompt as administrator</strong> and type this command <i>(change the path with your own)</i>:<br /><br />
<pre><code>cd "path/to/opensea-collection-scraper/"</code></pre>
<i>Example for the path: <code>"C:/Users/Administrator/Desktop/opensea-collection-scraper/"</code></i></li>
</li>

<li>Then, in the same command prompt, <strong>type one of these commands</strong> <i>(may require the <code>sudo</code> command on macOS and Linux)</i>:<br /><br />
<pre><code>pip install -r requirements.txt</code></pre>
<pre><code>pip3 install -r requirements.txt</code></pre>
<pre><code>python -m pip install -r requirements.txt</code></pre>
<pre><code>python3 -m pip install -r requirements.txt</code></pre>
<pre><code>py -m pip install -r requirements.txt</code></pre>
</li>

<li>Finally, <strong>type this command</strong> <i>(may require the <code>sudo</code> command on macOS and Linux)</i>:<br /><br />
<pre><code>npm install</code></pre>
A <code>node_modules/</code> folder should be created.</li>

</ul>


<h2>How to run this tool?</h2>

<ul>

<li><strong>Open a command prompt as administrator</strong> and type this command <i>(change the path with your own)</i>:<br /><br />
<pre><code>cd "path/to/opensea-collection-scraper/"</code></pre>
<i>Example for the path: <code>"C:/Users/Administrator/Desktop/opensea-collection-scraper/"</code></i></li>
</li>

<li>Then, in the same command prompt, <strong>type one of these commands</strong> <i>(may require the <code>sudo</code> command on macOS and Linux)</i>:<br /><br />
<pre><code>python scraper.py</code></pre>
<pre><code>python3 scraper.py</code></pre>
<pre><code>py scraper.py</code></pre>
</li>

<li>Press <code>Enter</code> and type your licence key (<code>XXXXXXXX-XXXXXXXX-XXXXXXXX-XXXXXXXX</code>).</li>

<li>Enter the number of items your collection should contain.</li>

<li>Enter the URL of your collection. <i>Example: <code>https://opensea.io/collection/crypto-parrot-nfts</code></i>.</li>
<li>JSON, CSV and XLSX files will be generated and stored in the <code>data/</code> folder of the repository.</li>
<li><strong>If you get this error <code>Expecting value: line 1 column 1 (char 0)</code>, see this <a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/305#issuecomment-1139566759">comment</a> for this issue which may help you.</strong></li>

</ul>


<h2>Changelog</h2>

<h3>Version 1.8.0</h3>
<ul>
<li>Fixed the timeout and the <code>lifecyclewatcher.js;108</code> errors by adding a a <code>try/catch</code> in a loop. <strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/364">#364</a>, <a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/issues/363">#363</a></strong>.</li>
</ul>

<h3>Versions 1.7.0 and 1.7.1</h3>
<ul>
<li>You can now import a file generated from the <code>node index.js</code> command.</li>
<li>Fixed the random crash error by adding a <code>try/catch</code> handle.</li>
<li>It now displays the error when it fails at the beginning of the scraping.</li>
</ul>

<h3>Version 1.6.0</h3>
<ul>
<li>Fixed a problem that caused no items to be scraped.</li>
<li>It will no longer show the <code>list index out of range</code> when there are no missing items.</li>
</ul>

<h3>Versions 1.5.0 and 1.5.1</h3>
<ul>
<li>It now displays the number of items retrieved.</li>
<li>Change of a value that has been modified by OpenSea.</li>
</ul>

<h3>Versions 1.4.0 and 1.4.1</h3>
<ul>
<li>Important fixes and improvements</li>
</ul>

<h3>Version 1.3.0</h3>
<ul>
<li>Major fixes.</li>
<li>The collection limit is 20,000 NFTs maximum.</li>
<li>The bot now scrapes twice.</li>
</ul>

<h3>Version 1.2.0</h3>
<ul>
<li>Correction of missing name in CSV files.</li>
<li>Correction of the creation of missing files.</li>
<li>Improved functioning of the duplicate detection.</li>
</ul>

<h3>Version 1.1.0</h3>
<ul>
<li>Adding the creation of a file containing duplicates.</li>
<li>Added the creation of a file containing the missing.</li>
<li>Added the name of the NFTs in the files for sale.</li>
</ul>

<h3>Version 1.0.0</h3>
<ul>
<li>Initial commit.</li>
</ul>

<h2>Purchase</h2>

<p>This tool is available on Gumroad as an add-on. <strong><a href="https://maximedrn.gumroad.com/l/opensea-collection-scraper">Purchase this tool</a></strong>.
<br /><i>Make sure the bot works on your system before purchasing any tools.</i></p>
