import httpx
from .config import Config

class WikiJSGraphQLClient:
    def __init__(self):
        self.url = f"{Config.WIKIJS_URL}/graphql"
        self.headers = {
            "Authorization": f"Bearer {Config.WIKIJS_API_KEY}",
            "Content-Type": "application/json"
        }

    async def query(self, query: str, variables: dict = None):
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                self.url,
                json={"query": query, "variables": variables or {}},
                headers=self.headers
            )
            resp.raise_for_status()
            data = resp.json()
            if "errors" in data:
                raise Exception(f"GraphQL error: {data['errors']}")
            return data["data"]

    # Example methods
    async def search_pages(self, query_str: str):
        query = """
        query SearchPages($query: String!) {
          pages(query: $query) {
            id
            title
            path
            content
            createdAt
            updatedAt
          }
        }
        """
        return await self.query(query, {"query": query_str})

    async def get_page(self, path: str):
        query = """
        query GetPage($path: String!) {
          page(path: $path) {
            id
            title
            path
            content
            createdAt
            updatedAt
          }
        }
        """
        return await self.query(query, {"path": path})

    async def create_page(self, title: str, content: str, path: str):
        mutation = """
        mutation CreatePage($title: String!, $content: String!, $path: String!) {
          createPage(input: {title: $title, content: $content, path: $path}) {
            id
            title
            path
          }
        }
        """
        return await self.query(mutation, {"title": title, "content": content, "path": path})

    async def update_page(self, id: str, content: str):
        mutation = """
        mutation UpdatePage($id: String!, $content: String!) {
          updatePage(id: $id, input: {content: $content}) {
            id
            title
            path
            content
          }
        }
        """
        return await self.query(mutation, {"id": id, "content": content})

    async def delete_page(self, id: str):
        mutation = """
        mutation DeletePage($id: String!) {
          deletePage(id: $id) {
            id
          }
        }
        """
        return await self.query(mutation, {"id": id})
