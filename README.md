<h1>OpenSea automatic uploader using Python Selenium</h1>

<h2>Instructions:</h2>

<ul>
  <li><h3>Basic installation of Python for beginners:</h3>
    <ul>
      <li>Download this repository.</li>
      <li>It requires <a href="https://www.python.org/" target="_blank">Python</a> 3.7 or a newest version.</li>
      <li>Install <a href="https://pip.pypa.io/en/stable/installation/" target="_blank">pip</a> to be able to have needed Python modules.</li>
      <li>Open a command prompt in repository folder and type <code>pip install -r requirements.txt</code>.</li>
    </ul>
  </li>
  <li><h3>Configuration of bot:</h3>
    <ul>
      <li>Download and install <a href="https://www.google.com/intl/en_en/chrome/">Google Chrome</a></li>
      <li>Download the <a href="https://chromedriver.chromium.org/downloads">chromedriver executable</a> that is compatible with the actual version of your Google Chrome browser and your OS (Operating System). Refer to: <i><a href="https://www.whatismybrowser.com/detect/what-version-of-chrome-do-i-have">What version of Google Chrome do I have?</a></i></li>
      <li>Extract the executable from the ZIP file and copy/paste it in the assets folder of the repository.</li>
      <li>Optional:
        <ul>
          <li>Open the assets/password.txt file and write your MetaMask password.</li>
          <li>Open the assets/recovery_phrase.txt file and write your recovery phrase.</li>
        </ul>
      <li>Create your NFTs data file containing all details of each NFT. It can be a CSV of JSON file.
        <br><strong><a href="">What structure should the files have?</a></strong></li>
    </ul>
  <li><h3>Data files structure:</h3>
    <ul>
      <li>CSV file:
        <br><ul>
        <li><strong>required value *</strong></li>
        <li><i>default value</i></li>
        </ul>
        <br><table>
          <tbody>
            <tr>
              <td>Settings</td>
              <td>Types</td>
              <td>Examples</td>
            </tr>
            <tr>
              <td><strong>File Path *</strong></a></td>
              <td>String</td>
              <td>C:/Users/Admin/Desktop/MyNFTs/nft_0001.png;</td>
            </tr>
            <tr>
              <td><strong>NFT Name *</strong></td>
              <td>String</td>
              <td>NFT #1;</td>
            </tr>
            <tr>
              <td>External Link</td>
              <td>String</td>
              <td>https://www.google.com/;</td>
            </tr>
            <tr>
              <td>Description</td>
              <td>String</td>
              <td>This is my first NFT.;</td>
            </tr>
            <tr>
              <td>Collection</td>
              <td>String</td>
              <td>My First NFT;</td>
            </tr>
            <tr>
              <td>Properties</td>
              <td>List[[String, String], ...]</td>
              <td>["Dog", "Male"];</td>
            </tr>
            <tr>
              <td>Levels</td>
              <td>List[[String, Integer, Integer], ...]</td>
              <td>[["Speed", 2, 5], ["Width", 1, 10]];</td>
            </tr>
            <tr>
              <td>Stats</td>
              <td>List[[String, Integer, Integer], ...]</td>
              <td>[["Strenght", 10, 100], ["Age", 1, 99]];</td>
            </tr>
            <tr>
              <td>Unlockable Content
                <br><i>False</i></td>
              <td>List[Boolean, String]</td>
              <td>[True, "Thank you for purchasing my NFT!"];</td>
            </tr>
            <tr>
              <td>Explicit And Sensitive Content
                <br><i>False</i></td>
              <td>Boolean</td>
              <td>True;</td>
            </tr>
            <tr>
              <td>Supply
                <br><i>1</i></td>
              <td>Integer</td>
              <td>5;</td>
            </tr>
            <tr>
              <td>Blockchain
                <br><i>Ethereum</i></td>
              <td>String</td>
              <td>Polygon</td>
            </tr>
          </tbody>
        </table>
        <h4>And it gives you something like <a href="">this</a>.</h4>
      </li>
      <li>JSON file:
        <br><ul>
        <li><strong>required value *</strong></li>
        <li><i>default value</i></li>
        </ul>
        <br><table>
          <tbody>
            <tr>
              <td>Settings</td>
              <td>Types</td>
              <td>Examples</td>
            </tr>
            <tr>
              <td><strong>File Path *</strong></a></td>
              <td>String</td>
              <td>"file_path": "C:/Users/Admin/Desktop/MyNFTs/nft_0001.png",</td>
            </tr>
            <tr>
              <td><strong>NFT Name *</strong></td>
              <td>String</td>
              <td>"nft_name": "NFT #1",</td>
            </tr>
            <tr>
              <td>External Link</td>
              <td>String</td>
              <td>"external_link": "https://www.google.com/",</td>
            </tr>
            <tr>
              <td>Description</td>
              <td>String</td>
              <td>"description": "This is my first NFT.",</td>
            </tr>
            <tr>
              <td>Collection</td>
              <td>String</td>
              <td>"collection": "My First NFT",</td>
            </tr>
            <tr>
              <td>Properties</td>
              <td>List[[String, String], ...]</td>
              <td>"properties": [{"type": "Dog", "name": "Male"}, {"type": "Cat", "name": "Female"}],</td>
            </tr>
            <tr>
              <td>Levels</td>
              <td>List[[String, Integer, Integer], ...]</td>
              <td>"levels": [{"name": "Speed", "from": 2, "to": 5}, {"name": "Width", "from": 1, "to": 10}],</td>
            </tr>
            <tr>
              <td>Stats</td>
              <td>List[[String, Integer, Integer], ...]</td>
              <td>"stats": [{"name": "Strenght", "from": 10, "to": 100}, {"name": "Age", "from": 1, "to": 99}],</td>
            </tr>
            <tr>
              <td>Unlockable Content
                <br><i>False</i></td>
              <td>List[Boolean, String]</td>
              <td>"unlockable_content": [true, "Thank you for purchasing my NFT!"],</td>
            </tr>
            <tr>
              <td>Explicit And Sensitive Content
                <br><i>False</i></td>
              <td>Boolean</td>
              <td>"explicit_and_sensitive_content": true,</td>
            </tr>
            <tr>
              <td>Supply
                <br><i>1</i></td>
              <td>Integer</td>
              <td>"supply": 5,</td>
            </tr>
            <tr>
              <td>Blockchain
                <br><i>Ethereum</i></td>
              <td>String</td>
              <td>"blockchain": "Polygon",</td>
            </tr>
          </tbody>
        </table>
        <h4>And it gives you something like <a href="">this</a>.</h4>
      </li>
    </ul>
</ul>
