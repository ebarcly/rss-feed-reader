import sys
from typing import List, Optional
from .rss_parser import RSSParser
from .exceptions import NetworkError, ParsingError, InvalidFeedError

def get_user_urls() -> List[str]:
    """Prompt user for URLs and return cleaned list"""
    url_input = input("Enter RSS Feed URLs (separate multiple URLs with spaces): ")
    urls = url_input.strip().split()
    return [url for url in urls if url]  # Filter out empty strings

def process_feed(url: str) -> None:
    print(f"\nFeching feed from: {url}")
    parser = RSSParser(url)
    items = parser.parse_items()

    print(f"\nFound {len(items)} items:")
    print("-" * 50)
    
    for item in items:
        print(f"\nTitle: {item['title']}")
        print(f"Description: {item.get('description', 'No description')}")
        print(f"Link: {item['link']}")
        print("-" * 50)

def process_urls(urls: List[str]) -> None:
    for url in urls:
        try:
            process_feed(url)
        except (NetworkError, ParsingError, InvalidFeedError) as e:
            print(f"Error processing {url}: {e}", file=sys.stderr)

def main() -> None:
    try:
        urls = get_user_urls()
        
        if not urls:
            print("No URLs provided. Please try again.")
            return

        process_urls(urls)
                
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)
        
if __name__ == "__main__":
    main()
