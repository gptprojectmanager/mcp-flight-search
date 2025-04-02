# MCP Flight Search

A flight search service built with MCP (Model Context Protocol).

## Installation

```bash
# Install from PyPI
pip install mcp-flight-search

# Or install from the project directory (development mode)
pip install -e .
```

## Usage

Start the server:

```bash
# Using the command-line entry point
mcp-flight-search --connection_type http

# Or run directly
python main.py --connection_type http
```

You can also specify a custom port:
```bash
python main.py --connection_type http --port 5000
```

## Environment Variables

Set the SerpAPI key as an environment variable:
```bash
export SERP_API_KEY="your-api-key-here"
```

## Features

- Search for flights using SerpAPI Google Flights
- Support for one-way and round-trip flights
- Rich logging with structured output
- Modular, maintainable code structure

## API Tools

- `search_flights_tool`: Search for flights between airports
- `server_status`: Check if the server is running

## Project Structure

```
mcp-flight-search/
├── mcp_flight_search/
│   ├── __init__.py              # Package initialization and exports
│   ├── config.py                # Configuration variables (API keys)
│   ├── models/
│   │   ├── __init__.py          # Models package init
│   │   └── schemas.py           # Pydantic models (FlightInfo)
│   ├── services/
│   │   ├── __init__.py          # Services package init
│   │   ├── search_service.py    # Main flight search logic
│   │   └── serpapi_client.py    # SerpAPI client wrapper
│   ├── utils/
│   │   ├── __init__.py          # Utils package init
│   │   └── logging.py           # Logging configuration
│   └── server.py                # MCP server setup and tools
├── main.py                      # Main entry point
├── pyproject.toml               # Python packaging configuration
├── LICENSE                      # MIT License
└── README.md                    # Project documentation
```

## Building and Publishing

Build the package:
```bash
python -m build
```

Upload to PyPI:
```bash
python -m twine upload dist/*
```

## License

This project is licensed under the MIT License - see the LICENSE file for details. 