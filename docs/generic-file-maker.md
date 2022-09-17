<br />
<p align="center">

<a href="https://maximedrn.gumroad.com/l/opensea-generic-file">
<img src="https://i.ibb.co/c3TRqdm/Wiki-Generic-File-Maker.png" alt="Generic File Maker" border="0">
</a>
<br /><br /><strong>This tool can be <a href="https://maximedrn.gumroad.com/l/opensea-generic-file">purchased on Gumroad</a> by using PayPal or a credit card.</strong>
<br /><i>If you cannot purchase on Gumroad or if you want to pay using crypto-currencies,
<br />contact me on <a href="https://t.me/maximedrn">Telegram</a> or send me an email at <a href="mailto:maxime_drean@yahoo.com">maxime_drean@yahoo.com</a>.
<br /><br />

</p>

<hr />

<h2>What does this tool do?</h2>

<p>
Using the <strong>Generic File Maker</strong>, you can <strong>complete your JSON metadata file using a simple generic file that contains 21 details</strong>, 18 about NFTs and 3 about how the tool works. It supports increment value, for example if you name your assets (images or videos) from 1 to 10000, you can <strong>in one line complete all the file paths of the metadata file</strong>.</p>

<p>You can complete and <strong>massively edit some details</strong> of your metadata file. And if you already uploaded a collection and scraped it using the <a href="../Collection-Scraper">Collection Scraper</a> tool, you can <strong>complete the generated metadata file with sale details</strong>.</p>
</p>


<h2>Installation of this tool</h2>

<i>After acquiring this tool, be sure to download all the files and save the key to a file so as not to lose it.
<br>This key and the files are available in your Library on Gumroad or in the email receipt.</i>

<ul>

<li>Before proceeding to these steps, make sure that <a href="Installation-and-configuration#installation-of-python">Python is installed</a>.</li>

<li><strong>Extract the tool folder from the ZIP archive file. Make sure all files are in the same parent folder.</strong></li>

<li><strong>Open a command prompt as administrator</strong> and type this command <i>(change the path with your own)</i>:<br /><br />
<pre><code>cd "path/to/opensea-generic-file-maker/"</code></pre>
<i>Example for the path: <code>"C:/Users/Administrator/Desktop/opensea-generic-file-maker/"</code></i></li>
</li>

<li>Then, in the same command prompt, <strong>type one of these commands</strong> <i>(may require the <code>sudo</code> command on macOS and Linux)</i>:<br /><br />
<pre><code>pip install -r requirements.txt</code></pre>
<pre><code>pip3 install -r requirements.txt</code></pre>
<pre><code>python -m pip install -r requirements.txt</code></pre>
<pre><code>python3 -m pip install -r requirements.txt</code></pre>
<pre><code>py -m pip install -r requirements.txt</code></pre>
</li>

</ul>


<h2>How to complete the generic file?</h2>

<p><i>If the <code>generic/</code> folder does not contain a <code>generic-file-blank.json</code> file after acquiring this tool, you can download it <a href="https://www.mediafire.com/file/ov16pfgs4g8wh4t/generic-file-blank.json/file">here</a> (MediaFire) or <a href="https://mega.nz/file/BPZQRbKa#Q2H-HDvfSB3xkOEXVCDZxambpaUIu4gGpt45iEp8FKE">here</a> (MEGA).</i></p>

<h3>Details part</h3>
In the details part of the generic file, you have to complete with the value you want to put in your metadata file.<br />
However if you want to use specific things in this file, read this:

<ul>
<li>To use backspaces in the description, add <code>\\n</code> for one <code>\n</code> (break a line).</li>
<li>If you want to use quotes in the description, add <code>\\\"</code> for one <code>"</code>.</li>
<li>If you want to use backslashes in in the description, add <code>\\\\</code> for one <code>\</code>.</li>
</ul>


<h3>What does the <code>incrementation</code> value mean?</h3>
You may have different file names, URLs or descriptions for each of your NFTs, so these details will be different for each NFT.

<ul>
<li><code>number</code>: it will use a numeric value for incrementing (<code>1</code>, <code>2</code>, <code>3</code>, <code>4</code>, etc).</li>
<li><code>letter</code>: it will use the alphabet for incrementing (<code>A</code> to <code>Z</code>, then <code>AA</code> to <code>AZ</code>, etc).</li>
</ul>
This value (<code>number</code> or <code>letter</code>) will be added wherever you place <code>{}</code> in your detail.


<h3>What does the <code>format</code> value mean?</h3>
This is the way <code>"increment": "number",</code> will work.

<ul>
<li><code>0</code>: default value, numbers will be incremented in a basic way.
<li><code>-1</code>: it will add a specific number of digits depending on the number of NFTs (10000 NFTs ➜ <code>00001</code>, <code>00002</code>, etc).</li>
<li>Any strictly positive number: number of digits (3 digits ➜ <code>001</code>, ... <code>100</code>, etc).</li>
</ul>

<h3>Settings part</h3>

<li><code>overwrite</code>: it will overwrite the entire contents of a metadata file. Set it to <code>true</code> if you want this.</li>
<li><code>overwrite_empty</code>: it will overwrite the details of a metadata file only if they are as default value. Set it to <code>true</code> if you want this.</li>
<li><code>append</code>: it will append the value of any list of dictionary details (properties, levels, stats). Set it to <code>true</code> if you want this.</li>


<h2>How to run this tool?</h2>

<ul>

<li><strong>Open a command prompt as administrator</strong> and type this command <i>(change the path with your own)</i>:<br /><br />
<pre><code>cd "path/to/opensea-generic-file-maker/"</code></pre>
<i>Example for the path: <code>"C:/Users/Administrator/Desktop/opensea-generic-file-maker/"</code></i></li>
</li>

<li>Then, in the same command prompt, <strong>type one of these commands</strong> <i>(may require the <code>sudo</code> command on macOS and Linux)</i>:<br /><br />
<pre><code>python generic.py</code></pre>
<pre><code>python3 generic.py</code></pre>
<pre><code>py generic.py</code></pre>
</li>

<li>Press <code>Enter</code> and type your licence key (<code>XXXXXXXX-XXXXXXXX-XXXXXXXX-XXXXXXXX</code>).</li>

<li>If you already have a compatible file with missing or incorrect details, select the <code>Duplicate from existing file.</code> option, else select <code>Generate a new file.</code> to generate a new file from the generic file completed.</li>

<li>Select the output structure of the metadata file.</li>

<li>Select the completed generic file from the list or browse it on your computer.</li>

<li>If you selected the <code>Duplicate from existing file.</code> option, select the completed metadata file from the list or browse it on your computer.</li>

<li>Finally, type the starting number for the increment.</li>

<li>Your metadata file is now generated in the <code>data/</code> folder of the tool folder.</li>

<li>Your metadata file is now ready to be used by the bot!</li>

</ul>


<h2>Changelog</h2>

<h3>Versions 1.3.0 to 1.3.3</h3>
<ul>
<li>Fixed recursion error when <code>Sale</code> option is selected.</li>
<li>Fixed <code>specific_buyer</code> value always set to <code>[true, ""]</code>.</li>
<li>You can now select <code>0</code> as the first value for your metadata file.</li>
</ul>

<h3>Versions 1.2.0 to 1.2.2</h3>
<ul>
<li>Important fixes and improvements.</li>
<li>Added a start value for incrementing.</li>
</ul>

<h3>Version 1.1.0</h3>
<ul>
<li>Added support for preview file in the generic file.</li>
<li>Fixed the problem of <code>unlockable_content</code> set to <code>false</code> when set to <code>true</code> in the data file.</li>
</ul>

<h3>Version 1.0.0</h3>
<ul>
<li>Initial commit.</li>
</ul>

<h2>Purchase</h2>

<p>This tool is available on Gumroad as an add-on. <strong><a href="https://maximedrn.gumroad.com/l/opensea-generic-file">Purchase this tool</a></strong>.
<br /><i>Make sure the bot works on your system before purchasing any tools.</i></p>