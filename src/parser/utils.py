import requests
from urllib.parse import urlparse
from typing import Dict, Optional
from defusedxml import ElementTree as ET
from .exceptions import NetworkError
import re
from html import unescape


def validate_url(url):
    """Validate if the given string is a proper URL.
    
    Args:
        url: The URL string to validate

    Returns:
        bool: True if valid URL, False otherwise
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

# Fetch the XML content
def fetch_feed(url, session=None):
    headers = {
    'User-Agent': 'RSS Reader/1.0 (Python/3.x)',
    'Accept': 'application/rss+xml, application/atom+xml'
    }
    timeout = 10
    if session is None:
        session = requests.Session()
    close_session = session is None

    try:
        if not validate_url(url):
            raise ValueError(f"Invalid URL format: {url}")
        response = session.get(
            url,
            headers=headers,
            timeout=timeout,
            verify=True
        )
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        raise NetworkError(f"Failed to fetch feed: {e}") from e
    finally:
        if close_session:
            session.close()



# Extract namespaces for dynamic namespaces handling
def extract_namespaces(xml_text):
    try:
        root = ET.fromstring(xml_text)
        # namespaces dict to use for extraction
        ns = {}
        # Capture all namespaces from root
        for key,value in root.attrib.items():
            if key.startswith('xmlns'):
                # Extract namespace prefix after colon
                prefix = key.split(':')[-1] if ':' in key else 'atom'
                ns[prefix] = value
        
        if 'atom' not in ns:
            ns['atom'] = 'http://www.w3.org/2005/Atom'

        return ns
    except ET.ParseError as e:
        raise NetworkError(f"Failed to parse XML: {e}") from e


def clean_description(html_content):
    """Clean HTML content from description"""
    if not html_content:
        return "No description"
    
    # Remove HTML tags
    clean_text = re.sub(r'<[^>]+>', '', html_content)
    # Unescape HTML entities
    clean_text = unescape(clean_text)
    # Remove extra whitespace
    clean_text = ' '.join(clean_text.split())
    # Truncate if too long
    max_length = 500
    if len(clean_text) > max_length:
        return clean_text[:max_length] + '...'
    return clean_text
