import pytest
from src.parser.rss_parser import RSSParser

SAMPLE_RSS = '''<?xml version="1.0"?>
<rss version="2.0">
  <channel>
    <item>
      <title>Test Item</title>
      <description>Test Description</description>
      <link>https://example.com</link>
    </item>
  </channel>
</rss>'''

def test_rss_parsing(monkeypatch):
    def mock_fetch(url):
        return SAMPLE_RSS

    monkeypatch.setattr("src.parser.rss_parser.fetch_feed", mock_fetch)
    parser = RSSParser("http://test.url")
    items = parser.parse_items()
    assert len(items) == 1
    assert items[0]['title'] == "Test Item"
    assert items[0]['description'] == "Test Description"

SAMPLE_ATOM = '''<?xml version="1.0"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <entry>
    <title>Atom Test</title>
    <link href="https://atom-example.com"/>
    <content>Atom Content</content>
  </entry>
</feed>'''

def test_atom_parsing(monkeypatch):
    def mock_fetch(url):
        return SAMPLE_ATOM

    monkeypatch.setattr("src.parser.rss_parser.fetch_feed", mock_fetch)
    parser = RSSParser("http://test.url")
    items = parser.parse_items()
    assert len(items) == 1
    assert items[0]['title'] == "Atom Test"
    assert items[0]['link'] == "https://atom-example.com"