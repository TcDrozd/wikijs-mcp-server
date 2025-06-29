FROM python:3.11-slim

WORKDIR /mcp_server

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY mcp_server/ mcp_server/

CMD ["python", "-m", "mcp_server.server"]
