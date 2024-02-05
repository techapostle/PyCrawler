import heapq


class URLManager:
    """
    Manages the queue of URLs for the crawler.

    This class is responsible for maintaining a list of URLs to be crawled,
    adding new URLs, and providing the next URL to the crawler while ensuring
    there are no duplicates.

    Attributes:
        to_crawl (priority queue): Queue of URLs to be crawled.
        crawled (set): Set of URLs already crawled.
        self.redirects(map): Map of URLs to their redirected URLs.
    """

    def __init__(self):
        """
        Initializes the URL Manager with necessary data structures.

        This method initializes the URL Manager with an empty set for URLs to be
        crawled and an empty set for URLs already crawled.
        """
        self.to_crawl = []
        self.crawled = set()
        self.redirects = {}

    def add_url(self, url, priority=0):
        """
        Adds a new URL to the queue if it hasn't been crawled.

        Args:
            url (str): The URL to add.
        """
        if url not in self.crawled and url not in (u[1] for u in self.to_crawl):
            heapq.heappush(self.to_crawl, (priority, url))

    def get_next_url(self):
        """
        Retrieves the next URL to crawl.

        Returns:
            str: The next URL to crawl, or None if no URLs are left.
        """
        while self.to_crawl:
            priority, url = heapq.heappop(self.to_crawl)
            if url not in self.crawled:
                self.crawled.add(url)
                return url
        return None

    def add_redirect(self, original_url, redirect_url):
        """
        Adds a redirect URL to the map.

        Args:
            original_url (str): The original URL.
            redirect_url (str): The redirected URL.
        """
        self.redirects[original_url] = redirect_url
        self.crawled.add(redirect_url)  # Mark the redirected URL as crawled
