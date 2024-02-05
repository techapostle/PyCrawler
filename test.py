# Assuming you have the CrawlerEngine, URLManager, and DataExtractor implemented as discussed

from crawler.engine import CrawlerEngine
from crawler.url_manager import URLManager
from crawler.data_extractor import DataExtractor

# Create instances of URLManager and DataExtractor
url_manager = URLManager()
data_extractor = DataExtractor()

# Add some sample URLs
sample_urls = ["http://google.com", "http://bing.com"]
for url in sample_urls:
    url_manager.add_url(url)

# Create an instance of CrawlerEngine
crawler_engine = CrawlerEngine(url_manager, data_extractor)

# Simulating the crawling process
while True:
    # Fetch a URL
    url = crawler_engine.fetch_url()
    if url is None:
        break  # Break if there are no more URLs to crawl

    print(f"Crawling URL: {url}")

    # Simulate fetching content (here we use dummy content)
    content = "<html><body>Sample Content for " + url + "</body></html>"

    # Process and extract data from the content
    extracted_data = crawler_engine.handle_data(content)
    print(f"Extracted Data: {extracted_data}")
