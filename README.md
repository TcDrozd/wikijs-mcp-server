# Wiki.js MCP Server

A Model Context Protocol (MCP) server for integrating Wiki.js documentation with local LLMs (e.g., Ollama).  
Provides tools for searching, retrieving, creating, updating, and deleting Wiki.js pages via a standardized MCP interface.

## Features

- Secure, authenticated access to your Wiki.js instance
- Exposes MCP tools for documentation management
- Designed for integration with Ollama, Cursor, Claude Desktop, and more
- Easy local deployment (Python or Docker)

## Quickstart

1. Copy `.env.example` to `.env` and fill in your Wiki.js and Ollama details.
2. Install dependencies:
pip install -r requirements.txt

text
3. Run the server:
python -m mcp_server.server

text
4. (Optional) Build and run with Docker:
docker-compose up --build

text
## Configuration

See `.env.example` for required environment variables.

## Project Structure

See the repo for code organization.

## License

MIT License.
