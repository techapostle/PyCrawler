import re
from crawler.data_extractor import DataExtractor


def test_data_extractor():
    # Create an instance of DataExtractor
    data_extractor = DataExtractor()

    # Define a pattern
    pattern = re.compile(r'<title>(.*?)</title>')

    # Add the pattern to the list of patterns
    data_extractor.add_pattern('title', pattern)

    # Define a sample content
    content = '<html><head><title>Sample Title</title></head></html>'

    # Extract data using the pattern
    extracted_data = data_extractor.extract_data(content, 'title')

    # Verify the extracted data
    assert extracted_data == {'title': ['Sample Title']}

test_data_extractor()