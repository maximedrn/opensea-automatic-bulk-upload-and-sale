<br />
<p align="center">

<a href="https://maximedrn.gumroad.com/l/opensea-file-compatibilizer">
<img src="https://i.ibb.co/FKdMyRV/Wiki-File-Compatibilizer-Converter.png" alt="File Compatibilizer & Converter" border="0">
</a>
<br /><br /><strong>This tool can be <a href="https://maximedrn.gumroad.com/l/opensea-file-compatibilizer">purchased on Gumroad</a> by using PayPal or a credit card.</strong>
<br /><i>If you cannot purchase on Gumroad or if you want to pay using crypto-currencies,
<br />contact me on <a href="https://t.me/maximedrn">Telegram</a> or send me an email at <a href="mailto:maxime_drean@yahoo.com">maxime_drean@yahoo.com</a>.
<br /><br />

</p>

<hr />

<h2>What does this tool do?</h2>

<p>
Using the <strong>File Compatibilizer and Converter</strong>, you can <strong>convert all JSON files generated with the <a href="https://github.com/HashLips/hashlips_art_engine">HashLips Art Engine</a> tool into a single compatible file</strong>. The tool ignores the file named <code>_metadata.json</code> and focuses on all other files listed. It <strong>retrieves each of the information containing them such as attributes</strong> and properties and adds them into a single file.
</p>

<p>Moreover, in case you decided to create your file manually or with another script and you forgot some mandatory details, it is possible to add them automatically.
<br>On the other hand, if your file contains all the necessary details but they are not in the right order, it is possible to automatically <strong>rearrange them so that the file is readable and compatible</strong>.</p>

<p>Finally, you can <strong>convert your file from one structure to another</strong>. The term structure defines here the different possibilities that the <strong>Upload and Listing bot</strong> offers:
<ul>
<li><code>Upload and Sale</code> to transfer and list your NFTs to the OpenSea marketplace,</li>
<li><code>Upload Only</code> to transfer only your NFTs to OpenSea without putting them on sale,</li>
<li><code>Sale Only</code> to put them up for sale if the NFTs are already transferred to OpenSea.</li>
</ul>
</p>


<h2>Installation of this tool</h2>

<i>After acquiring this tool, be sure to download all the files and save the key to a file so as not to lose it.
<br>This key and the files are available in your Library on Gumroad or in the email receipt.</i>

<ul>

<li>Before proceeding to these steps, make sure that <a href="Installation-and-configuration#installation-of-python">Python is installed</a>.</li>

<li><strong>Extract the tool folder from the ZIP archive file. Make sure all files are in the same parent folder.</strong></li>

<li><strong>Open a command prompt as administrator</strong> and type this command <i>(change the path with your own)</i>:<br /><br />
<pre><code>cd "path/to/opensea-file-compatibilizer-and-converter/"</code></pre>
<i>Example for the path: <code>"C:/Users/Administrator/Desktop/opensea-file-compatibilizer-and-converter/"</code></i></li>
</li>

<li>Then, in the same command prompt, <strong>type one of these commands</strong> <i>(may require the <code>sudo</code> command on macOS and Linux)</i>:<br /><br />
<pre><code>pip install -r requirements.txt</code></pre>
<pre><code>pip3 install -r requirements.txt</code></pre>
<pre><code>python -m pip install -r requirements.txt</code></pre>
<pre><code>python3 -m pip install -r requirements.txt</code></pre>
<pre><code>py -m pip install -r requirements.txt</code></pre>
</li>

</ul>


<h2>How to use this tool?</h2>

<ul>

<li><strong>Open a command prompt as administrator</strong> and type this command <i>(change the path with your own)</i>:<br /><br />
<pre><code>cd "path/to/opensea-file-compatibilizer-and-converter/"</code></pre>
<i>Example for the path: <code>"C:/Users/Administrator/Desktop/opensea-file-compatibilizer-and-converter/"</code></i></li>
</li>

<li>Then, in the same command prompt, <strong>type one of these commands</strong> <i>(may require the <code>sudo</code> command on macOS and Linux)</i>:<br /><br />
<pre><code>python converter.py</code></pre>
<pre><code>python3 converter.py</code></pre>
<pre><code>py converter.py</code></pre>
</li>

<li>Press <code>Enter</code> and type your licence key (<code>XXXXXXXX-XXXXXXXX-XXXXXXXX-XXXXXXXX</code>).</li>

<li>Then choose from what you want to convert.
<ul>
<li>First option: from a compatible metadata file in order to add missing details or to reorganize them.</li>
<li>Second option: from JSON metadata files generated using the HashLips Art Engine.</li>
</ul>

<li><strong>If you chose the first option</strong>, select your metadata file from the list or browse it on your computer.</li>

<li><strong>If you chose the second option</strong>, type the path to the <code>build/json</code> folder of the HashLips Art Engine that contains all the JSON metadata files.</li>

<li>Finally, select the output structure of the metadata file.</li>

<li>Your metadata file is now generated in the <code>data/</code> folder of the tool folder.</li>

<li>If you have converted JSON metadata files generated with the HashLips Art Engine, your file is incomplete and needs to be completed with more details.
<br />You can use the <a href="Generic-File-Maker"><strong>Generic File Maker</strong></a> tool.</li>

</ul>


<h2>Changelog</h2>

<h3>Version 1.5.0</h3>
<ul>
<li>You can now convert the <code>_metadata.json</code> file from the HashLips Art Engine.</li>
</ul>

<h3>Version 1.4.0</h3>
<ul>
<li>Major fixes about the folder path for MacOS users.</li>
<li>Minor fix about the <code>file_path</code> value. It now skips it when it doesn't present in the metadata files.</li>
</ul>

<h3>Version 1.3.0</h3>
<ul>
<li>The tool now automatically orders files generated by the HashLips Art Engine.</li>
</ul>

<h3>Versions 1.2.0 and 1.2.1</h3>
<ul>
<li>Major fixes for MacOS.</li>
</ul>

<h3>Versions 1.1.0 and 1.1.1</h3>
<ul>
<li>Added the Hashlips Art Engine files conversion.</li>
<li>It no longer reads the <code>_metadata.json</code> file.</li>
</ul>

<h3>Version 1.0.0</h3>
<ul>
<li>Initial commit.</li>
</ul>

<h2>Purchase</h2>

<p>This tool is available on Gumroad as an add-on. <strong><a href="https://maximedrn.gumroad.com/l/opensea-file-compatibilizer">Purchase this tool</a></strong>.
<br /><i>Make sure the bot works on your system before purchasing any tools.</i></p>