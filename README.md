<h1 align="center">Automatically and massively upload and list your non-fungible tokens on the OpenSea marketplace using Python Selenium.</h1>

<p>A Selenium Python bot to automatically and bulk upload and list your NFTs on OpenSea.
<br />All metadata integrated - Ethereum and Polygon supported - reCAPTCHA solver services included.
<br><strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/wiki/Changelog">Version 1.13.0</a> (December 06, 2023)</strong></p>

---

[![CapSolver](https://github.com/user-attachments/assets/7af866a1-99c1-45fc-b62a-22fb8a5e9bc4)](https://www.capsolver.com/?utm_source=github&utm_medium=banner_repo&utm_campaign=scraping&utm_term=maxime)
[CapSolver](https://www.capsolver.com/?utm_source=github&utm_medium=banner_repo&utm_campaign=scraping&utm_term=maxime) is an AI-powered service that automatically solves a range of CAPTCHAs, helping developers tackle CAPTCHA challenges encountered during web scraping. Whether you're extracting data from e-commerce sites, financial platforms, or social media, CapSolver supports CAPTCHAs like [reCAPTCHA V2](https://docs.capsolver.com/guide/captcha/ReCaptchaV2.html?utm_source=github&utm_medium=banner_repo&utm_campaign=scraping&utm_term=maxime), [reCAPTCHA V3](https://docs.capsolver.com/guide/captcha/ReCaptchaV3.html?utm_source=github&utm_medium=banner_repo&utm_campaign=scraping&utm_term=maxime), [hCaptcha](https://docs.capsolver.com/guide/captcha/HCaptcha.html?utm_source=github&utm_medium=banner_repo&utm_campaign=scraping&utm_term=maxime), [ImageToText](https://docs.capsolver.com/guide/recognition/ImageToTextTask.html?utm_source=github&utm_medium=banner_repo&utm_campaign=scraping&utm_term=maxime), [DataDome](https://docs.capsolver.com/guide/antibots/datadome.html?utm_source=github&utm_medium=banner_repo&utm_campaign=scraping&utm_term=maxime), [AWS](https://docs.capsolver.com/guide/captcha/awsWaf.html?utm_source=github&utm_medium=banner_repo&utm_campaign=scraping&utm_term=maxime), [Geetest](https://docs.capsolver.com/guide/captcha/Geetest.html?utm_source=github&utm_medium=banner_repo&utm_campaign=scraping&utm_term=maxime), [Cloudflare Turnstile](https://docs.capsolver.com/guide/antibots/cloudflare_turnstile.html?utm_source=github&utm_medium=banner_repo&utm_campaign=scraping&utm_term=maxime) and more. With API integration and browser extensions options, and flexible pricing packages, CapSolver adapts to diverse web scraping needs and scenarios.

---

<h2>Table of contents - <a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/wiki">Documentation</a></h2>

<ul>
<li><strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/wiki/Home#introduction">Introduction</a>, what does this bot do and how does it works?</strong></li>
<li><strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/wiki/Installation-and-configuration">Installation and configuration</a> of Python, the required modules and the bot.</strong></li>
<li><strong><a href="https://github.com/maximedrn/opensea-automatic-bulk-upload-and-sale/wiki/Creation-of-the-metadata-file">Creation of the metadata file</a>, discover its structure.</strong></li>
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
