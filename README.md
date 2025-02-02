# RSS Feed Reader

A command-line RSS feed reader supporting both RSS and Atom formats.

## Features

- Supports both RSS and Atom feed formats
- Clean and formatted output
- Multiple feed support
- Item limit option
- Error handling for invalid feeds
- HTML content cleaning
- Security: XML bomb protection

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ebarcly/rss-feed-reader.git

cd rss-feed-reader
```

2. Set up a virtual environment:

```bash
python -m venv venv

source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Read a single feed:

```bash
python -m src.parser.cli
```

Then enter the feed URL when prompted.

### Read multiple feeds:

```bash
python -m src.parser.cli
```

Enter multiple URLs **separated by spaces** when prompted.

## Tech Stack

- Python 3.9+
- defusedxml for secure XML parsing
- requests for HTTP requests
- typing for type hints
- pytest for testing

## Example Output

```bash
...
Fetching feed from: https://hnrss.org/frontpage
Found 30 items:
--------------------------------------------------
Title: Show HN: We're building a desktop app for browser agents
Description: What's up HN! This is Jared and Art. We met on HN and started building together...
Link: https://meha.ai
--------------------------------------------------
...
```

## Demo

Check out the [live demo](https://screen.studio/share/vDNeo9iv) to see the RSS Feed Reader in action.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

[MIT](https://github.com/ebarcly/rss-feed-reader/blob/main/LICENSE)
