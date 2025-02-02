from defusedxml import ElementTree as ET
from src.parser.exceptions import InvalidFeedError, ParsingError
from src.parser.utils import fetch_feed, extract_namespaces, clean_description

class RSSParser:
    
    def __init__(self, url):
        self.url = url
        self.xml_text = fetch_feed(url)
        try:
            self.root = ET.fromstring(self.xml_text)
        except ET.ParseError as e:
            raise ParsingError(f"Failed to parse XML: {e}")
            
        self.ns = extract_namespaces(self.xml_text)
        self.feed_type = self._detect_feed_type()
        
    def _detect_feed_type(self):
        if self.root.tag.endswith('feed'):
            return 'atom'
        elif self.root.tag == 'rss':
            return 'rss'
        raise InvalidFeedError(f"Unsupported feed type: {self.root.tag}")
    
    def parse_items(self):
        if self.feed_type == 'atom':
            items = self._parse_atom()
        else:
            items = self._parse_rss()
            
        return items
    
    def _parse_atom(self):
        items = []
        entries = self.root.findall('.//atom:entry', namespaces=self.ns)
        
        for entry in entries:
            title = entry.find('atom:title', namespaces=self.ns)
            content = entry.find('atom:content', namespaces=self.ns)
            link = entry.find('atom:link', namespaces=self.ns)
            
            if title is not None:
                description_text = clean_description(content.text if content is not None else None)
                link_url = link.attrib.get('href') if link is not None else "No links"
                
                items.append({
                    'title': title.text,
                    'description': description_text,
                    'link': link_url
                })
        return items
        
    def _parse_rss(self):
        items = []
        feed_items = self.root.findall('.//item')
        
        for item in feed_items:
            title = item.find('title')
            description = item.find('description')
            link = item.find('link')
            if title is not None and link is not None:
                items.append({
                    'title': title.text if title is not None else "No title",
                    'description': clean_description(description.text if description is not None else "No description"),
                    'link': link.text if link is not None else "No link"
                })
        return items