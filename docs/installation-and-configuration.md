<br />
<p align="center">
<img src="https://i.ibb.co/HzwxLFR/python.png" alt="Python illustration">
</p>

<p align="center"><strong>In addition to this documentation, you can watch this <a href="https://www.youtube.com/watch?v=jtERa6i9e1k">video</a> on YouTube.</strong></p>

<hr />

<h2>Installation of Python</h2>

<ul>

<li>Go to the official website of the <a href="https://www.python.org/downloads">Python Software Foundation</a> and <strong>download a recent version of Python</strong>, <strong>version 3.9.11</strong> is recommended.
<br><i>Make sure you <strong>add Python in path by checking the checkbox</strong> when you run the installation.</i></li>

<li>In order to verify that Python is properly installed, open as administrator a command prompt <i>(equivalent to Terminal on Linux and MacOS)</i> and type one of the following commands:<br /><br />
<pre><code>python --version</code></pre>
<pre><code>python3 --version</code></pre>
<pre><code>py --version</code></pre>
</li>

<li>Then, in the same command prompt, make sure that the <strong>pip module is installed</strong> with Python by typing one of these commands:<br /><br />
<pre><code>pip --version</code></pre>
<pre><code>pip3 --version</code></pre>
<pre><code>python -m pip --version</code></pre>
<pre><code>python3 -m pip --version</code></pre>
<pre><code>py -m pip --version</code></pre>
If the pip module is not installed, follow this <a href="https://pip.pypa.io/en/stable/installation/">tutorial</a> that explains how to install it.</li>

</ul>

<br />
<h2>Installation and configuration of the bot</h2>

<ul>

<li><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/archive/refs/heads/master.zip"><strong>Download this repository</strong></a>, or clone it by typing this command in your command prompt (it requires <a href="https://git-scm.com/downloads">Git</a>):<br /><br />
<pre><code>git clone https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale.git</code></pre></li>

<li><strong>Extract the repository</strong> folder from the ZIP file, you should have a folder named <code>opensea-automatic-bulk-upload-and-sale-master/</code>.</li>

<li><strong>Open a command prompt as administrator</strong> and type this command <i>(change the path with your own)</i>:<br /><br />
<pre><code>cd "path/to/opensea-automatic-bulk-upload-and-sale/"</code></pre>
<i>Example for the path: <code>"C:/Users/Administrator/Desktop/opensea-automatic-bulk-upload-and-sale/"</code></i></li>
</li>

<li>Then, in the same command prompt, <strong>type one of these commands</strong> <i>(may require the <code>sudo</code> command on macOS and Linux)</i>:<br /><br />
<pre><code>pip install -r requirements.txt</code></pre>
<pre><code>pip3 install -r requirements.txt</code></pre>
<pre><code>python -m pip install -r requirements.txt</code></pre>
<pre><code>python3 -m pip install -r requirements.txt</code></pre>
<pre><code>py -m pip install -r requirements.txt</code></pre>
</li>

<li><strong>Download and install</strong> <a href="https://www.google.com/intl/en_en/chrome/">Google Chrome</a> and/or <a href="https://www.mozilla.org/en-US/firefox/new/">Mozilla Firefox</a>.

</ul>


Now, Python and the bot are installed and configured. All you have to do is <a href="Creation-of-the-metadata-file">create your metadata file</a> or before that, <a href="#configuration-of-the-recaptcha-solver-using-yolov5x6">install and configure the reCAPTCHA solver with Yolov5x6</a> <i><strong>(not recommended for beginners - other reCAPTCHA solver services are available)</strong></i>.


<br />
<h2>Configuration of the reCAPTCHA solver using Yolov5x6</h2>

<p>➜ <i>Yolov5x6 and RealESRGAN, ignore this if you use the <a href="https://2captcha.com/?from=13853725">2Captcha solver</a> (affiliate link), the <a href="reCAPTCHA-Bypasser">reCAPTCHA bypasser</a> or the manual solution.</i>
<br />➜ <i>Only available for Windows and Linux users.</i></p>

<li>You will <strong>need a one of these graphics card (GPU)</strong>:
<ul>
<li>GTX 1080.</li>
<li>RTX 2060, RTX 2070, RTX 2080.</li>
<li>RTX 2050, RTX 3060, RTX 3070, RTX 3080, RTX 3090.</li>
<li>Any Ti version of these graphics cards.</li>
</ul>

<li>Open a command prompt and type this command to check your CUDA version (it must be 11.6 or higher):<br /><br />
<pre><code>nvidia-smi</code></pre>

<li>If your CUDA version is earlier than 11.3, try to update it at the <a href="https://developer.nvidia.com/cuda-downloads">NVIDIA website</a>.

<li>Then type one of these commands to install PyTorch (may require the <code>sudo</code> command on Linux, or administrator privileges for Windows):<br /><br />
<pre><code>pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio===0.11.0+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html</code></pre>
<pre><code>pip3 install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio===0.11.0+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html</code></pre>
<pre><code>python -m pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio===0.11.0+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html</code></pre>
<pre><code>python3 -m pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio===0.11.0+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html</code></pre>
<pre><code>py -m pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio===0.11.0+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html</code></pre>
<p>Or select one of the commands <a href="https://pytorch.org/get-started/locally/">here</a> depending on your computer.  
<br /><i><a href="https://pytorch.org/get-started/previous-versions/">Previous versions of PyTorch</a> with older CUDA version.</i></p>

<li>Install the required modules for the reCAPTCHA solver typing one of these commands (may require the <code>sudo</code> command on Linux, or administrator privileges for Windows):<br /><br />
<pre><code>pip install -r requirements_yolov5x6.txt</code></pre>
<pre><code>pip3 install -r requirements_yolov5x6.txt</code></pre>
<pre><code>python -m pip install -r requirements_yolov5x6.txt</code></pre>
<pre><code>python3 -m pip install -r requirements_yolov5x6.txt</code></pre>
<pre><code>py -m pip install -r requirements_yolov5x6.txt</code></pre>


<br />
<h2>How to run the bot?</h2>

<li><strong>Open a command prompt as administrator</strong> and type this command <i>(change the path with your own)</i>:<br /><br />
<pre><code>cd "path/to/opensea-automatic-bulk-upload-and-sale/"</code></pre>
<i>Example for the path: <code>"C:/Users/Administrator/Desktop/opensea-automatic-bulk-upload-and-sale/"</code></i></li>
</li>

<li>Then, in the same command prompt, <strong>type one of these commands</strong> <i>(may require the <code>sudo</code> command on macOS and Linux)</i>:<br /><br />
<pre><code>python main.py</code></pre>
<pre><code>python3 main.py</code></pre>
<pre><code>py main.py</code></pre>
</li>

<li>Select the action and your file, choose your wallet, your reCAPTCHA solver and a WebDriver.
<br />Type your credentials <strong>or</strong> <a href="Home#how-to-use-a-custom-google-chrome-profile">set your custom Google Chrome profile</a>.</li>

<li>Then it will download a WebDriver according to your choice and your browser version.
<ul>
<li>If the download fails, you can download the <a href="https://chromedriver.chromium.org/downloads">ChromeDriver</a> / <a href="https://github.com/mozilla/geckodriver/releases">GeckoDriver</a> according to your Google Chrome / Mozilla Firefox browser version.</li>
<li>To know the version of your browser, consult these websites: <a href="https://www.whatismybrowser.com/detect/what-version-of-chrome-do-i-have">Google Chrome</a> - <a href="https://www.whatismybrowser.com/detect/what-version-of-firefox-do-i-have">Mozilla Firefox</a></li>
</ul>
<li>If you selected the automatic reCAPTCHA solver using Yolov5, 2 files will be downloaded:
<li><code>realesrgan/RealESRGAN_x4plus.pth</code>: 63.9 MB. Available <a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/releases/tag/RealESRGAN">here</a> if the download fails.</li>
<li><code>yolov5/yolov5x6.pt</code>: 269 MB. Available <a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/releases/tag/Yolov5x6">here</a> if the download fails.</li>
</ul>