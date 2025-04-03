FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy package files
COPY mcp_flight_search/ ./mcp_flight_search/
COPY main.py pyproject.toml README.md LICENSE ./

# Install the package
RUN pip install -e .

# Run in stdio mode by default
ENTRYPOINT ["python", "-m", "mcp_flight_search.server", "--connection_type", "stdio"] 