import re

class DataExtractor:
    """
    Extracts data from web pages.

    This class handles parsing the content of web pages and extracting useful
    information based on predefined rules or patterns.
    """

    def __init__(self):
        # Initialize any required resources or configurations
        self.patterns = {} # Example: {'title': re.compile(r'<title>(.*?)</title>')}

    def extract_data(self, content, pattern_key):
        """
        Extracts data from the given content of a web page.

        Args:
            content (str): The content of a web page.
            pattern_key (str): The key to identify the pattern to be used for extraction.

        Returns:
            dict: Extracted data in a structured format.
        """

        # Extract data based on the pattern_key
        pattern = self.patterns.get(pattern_key)
        if pattern:
            matches = pattern.findall(content)
            return {pattern_key: matches}
        else:
            return {}
        
    def add_pattern(self, key, pattern):
        """
        Adds a new pattern to the list of patterns.

        Args:
            key (str): The key to identify the pattern.
            pattern (re.Pattern): The pattern to be added.
        """

        self.patterns[key] = pattern
