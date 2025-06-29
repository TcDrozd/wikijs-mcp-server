import pytest
import asyncio
from mcp_server.tools import (
    SearchPagesTool,
    GetPageTool,
    CreatePageTool,
    UpdatePageTool,
    DeletePageTool,
)

@pytest.mark.asyncio
async def test_search_pages(monkeypatch):
    class FakeClient:
        async def search_pages(self, query):
            return {"pages": [{"title": "Test", "path": "/test", "id": "1"}]}
    monkeypatch.setattr("mcp_server.tools.WikiJSGraphQLClient", lambda: FakeClient())
    tool = SearchPagesTool()
    result = await tool.run("Test")
    assert result[0]["title"] == "Test"

# Additional tests for GetPageTool, CreatePageTool, etc. can be created similarly.
