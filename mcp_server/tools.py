from fastmcp import Tool
from .graphql_client import WikiJSGraphQLClient
from .utils import get_logger

logger = get_logger()

class SearchPagesTool(Tool):
    name = "search_pages"
    description = "Search Wiki.js pages by query string."

    async def run(self, query: str):
        client = WikiJSGraphQLClient()
        logger.info(f"Searching Wiki.js pages with query: {query}")
        result = await client.search_pages(query)
        return result["pages"]

class GetPageTool(Tool):
    name = "get_page"
    description = "Retrieve a Wiki.js page by path."

    async def run(self, path: str):
        client = WikiJSGraphQLClient()
        logger.info(f"Getting Wiki.js page at path: {path}")
        result = await client.get_page(path)
        return result["page"]

class CreatePageTool(Tool):
    name = "create_page"
    description = "Create a new Wiki.js page."

    async def run(self, title: str, content: str, path: str):
        client = WikiJSGraphQLClient()
        logger.info(f"Creating Wiki.js page: {title} at {path}")
        result = await client.create_page(title, content, path)
        return result["createPage"]

class UpdatePageTool(Tool):
    name = "update_page"
    description = "Update the content of an existing Wiki.js page by ID."

    async def run(self, id: str, content: str):
        client = WikiJSGraphQLClient()
        logger.info(f"Updating Wiki.js page ID: {id}")
        result = await client.update_page(id, content)
        return result["updatePage"]

class DeletePageTool(Tool):
    name = "delete_page"
    description = "Delete a Wiki.js page by ID."

    async def run(self, id: str):
        client = WikiJSGraphQLClient()
        logger.info(f"Deleting Wiki.js page ID: {id}")
        result = await client.delete_page(id)
        return result["deletePage"]
