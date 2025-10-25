#!/usr/bin/env python3
"""
MCP Server for Maritime Application - A helloworld python application
Exposes the maritime demo app as an MCP tool
"""

import asyncio
import subprocess
import sys
from pathlib import Path

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent


# Create server instance
app = Server("maritime-server")


@app.list_tools()
async def list_tools() -> list[Tool]:
      """List available tools."""
      return [
          Tool(
              name="run_maritime_app",
              description="Runs the maritime demo application which displays a hello world message, current timestamp, and fetches a random fun fact",
              inputSchema={
                  "type": "object",
                  "properties": {},
                  "required": []
              }
          )
      ]


@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
      """Handle tool calls."""
      if name == "run_maritime_app":
          try:
              # Get the directory where this script is located
              script_dir = Path(__file__).parent
              app_path = script_dir / "app.py"

              # Run the maritime app
              result = subprocess.run(
                  [sys.executable, str(app_path)],
                  capture_output=True,
                  text=True,
                  timeout=10,
                  cwd=script_dir
              )

              output = result.stdout
              if result.stderr:
                  output += f"\n\nErrors:\n{result.stderr}"

              return [TextContent(
                  type="text",
                  text=output if output else "Application ran but produced no output"
              )]

          except subprocess.TimeoutExpired:
              return [TextContent(
                  type="text",
                  text="Error: Application timed out after 10 seconds"
              )]
          except Exception as e:
              return [TextContent(
                  type="text",
                  text=f"Error running application: {str(e)}"
              )]
      else:
          return [TextContent(
              type="text",
              text=f"Unknown tool: {name}"
          )]


async def main():
      """Run the MCP server."""
      async with stdio_server() as (read_stream, write_stream):
          await app.run(
              read_stream,
              write_stream,
              app.create_initialization_options()
          )


if __name__ == "__main__":
      asyncio.run(main())

