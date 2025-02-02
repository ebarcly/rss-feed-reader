class RSSReaderError(Exception):
    """Base class for all package exceptions"""
    pass

class NetworkError(RSSReaderError):
    """Failed to fetch feed from network"""
    def __init__(self, url):
        super().__init__(f"Failed to reach {url}")
        self.url = url

class ParsingError(RSSReaderError):
    """Failed to parse feed content"""
    def __init__(self, element):
        super().__init__(f"Failed to parse {element}")
        self.element = element

class InvalidFeedError(RSSReaderError):
    """Invalid or unrecognized feed format"""
    def __init__(self, feed_type):
        super().__init__(f"Unsupported feed type: {feed_type}")
        self.feed_type = feed_type