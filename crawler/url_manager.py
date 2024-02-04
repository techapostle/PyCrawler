class URLManager:
    """
    Manages the queue of URLs for the crawler.

    This class is responsible for maintaining a list of URLs to be crawled,
    adding new URLs, and providing the next URL to the crawler while ensuring
    there are no duplicates.
    """

    def __init__(self):
        """
        Initializes the URL Manager with necessary data structures.
        """
        self.to_crawl = set()
        self.crawled = set()

    def add_url(self, url):
        """
        Adds a new URL to the queue if it hasn't been crawled.

        Args:
            url (str): The URL to add.
        """
        if url not in self.crawled:
            self.to_crawl.add(url)

    def get_next_url(self):
        """
        Retrieves the next URL to crawl.

        Returns:
            str: The next URL to crawl, or None if no URLs are left.
        """
        if self.to_crawl:
            url = self.to_crawl.pop()
            self.crawled.add(url)
            return url
        else:
            return None

    # Additional methods and functionalities can be added as needed.
