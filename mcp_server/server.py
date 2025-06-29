from fastmcp import FastMCP
from .tools import (
    SearchPagesTool,
    GetPageTool,
    CreatePageTool,
    UpdatePageTool,
    DeletePageTool,
)
from .auth import check_wikijs_api_key
from .utils import get_logger

logger = get_logger()

def main():
    check_wikijs_api_key()
    logger.info("Starting Wiki.js MCP Server...")

    server = FastMCP(
        tools=[
            SearchPagesTool(),
            GetPageTool(),
            CreatePageTool(),
            UpdatePageTool(),
            DeletePageTool(),
        ],
        name="Wiki.js MCP Server",
        description="MCP server for Wiki.js documentation management.",
        version="0.1.0",
    )
    server.run()

if __name__ == "__main__":
    main()
