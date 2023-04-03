<h1><b>Walmart Products Data Scraper</b></h1>
<p>This python script is a data pipeline that scrapes product data from <a href="https://www.walmart.com/">Walmart.com</a> based on a specified keyword, and saves the data to an S3 bucket in CSV file format. The data then used to create reports and visualizations using Power BI.</p>
<p>Before running the script, certain changes need to be made in the <b>settings.py</b> file.</p>
<h2><b>Requirements</b></h2>
<ul>
  <li>Python 3.6 or later</li>
  <li><a href="https://scrapy.org/">Scrapy Framework</a></li>
  <li><a href="https://libraries.io/pypi/scrapeops-scrapy-proxy-sdk">ScrapeOps Proxy Rotator</a>- Sign up for a free trial of ScrapeOps Proxy Rotator and get your API key</li>
  <li><a href="https://botocore.amazonaws.com/v1/documentation/api/latest/index.html">Botocore</a></li>
  <li><a href="https://docs.aws.amazon.com/quickstarts/latest/s3backup/step-1-create-bucket.html">Create AWS S3 Bucket</li>
</ul>
<h2><b>Installation</b></h2>
<ol>
  <li>Clone the repository using bash:

```bash
git clone https://github.com/usmananwaar-de/Walmart-Scraper
```

  </li>
  <li>Navigate to the cloned directory in the command line. </li>
  <li>Create a virtual environment by running the command (For Windows): <code>python -m venv [venv name]</code></li>
  <li>Activate the virtual environment by running the command: <code>venv\Scripts\activate</code></li>
  <li>Change the directory using <code>cd</code> command and go into the spiders folder
  <li>Install the required libraries by running the command<code>pip install -r requirements.txt</code></li>
</ol>
<h2><b>Usage</b></h2>
<p>Before running the script, the following changes need to be made in the <b>settings.py</b> file:</p>
<ol>
  <li>Open the <code>settings.py</code> file and replace the <code>YOUR_SCRAPEOPS_API_KEY</code> variable with your ScrapeOps API key</li>
  <li>Replace the <code>YOUR_S3_BUCKET_PATH</code> with the path to your S3 bucket.</li>
  <li>Replace the <code>YOUR_AWS_KEY_ID</code> and <code>YOUR_AWS_SECRET_ACCESS_KEY</code> with your AWS access key ID and secret access key..</li>
</ol>
<p>To run the script, use the following command and write the desired product keyword:</p>

```bash
scrapy crawl walmart
```

<p><h5>**Note: rotating proxies are used because Walmart.com detects scraper bots and blocks their IP addresses.**</h5></p>
<h2><b>Notes</b></h2>
<ul>
  <li>Walmart.com may block your scraper, so it's important to use a proxy service like ScrapeOps to avoid this</li>
</ul>
