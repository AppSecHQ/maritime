# MCP Server Setup for Maritime Application

This repository includes an MCP (Model Context Protocol) server that allows Claude Code to run the maritime application as a tool.

## Prerequisites

1. Python 3.8 or higher
2. Claude Code installed
3. Dependencies installed: `pip install -r requirements.txt`

## Installation

### Step 1: Install Dependencies

First, make sure all Python dependencies are installed including the MCP SDK:

```bash
pip3 install -r requirements.txt
```

### Step 2: Configure the MCP Server

You have two options to configure the maritime MCP server:

#### Option A: Using the CLI (Recommended)

From your project directory, run:

```bash
claude mcp add --transport stdio maritime -- python3 mcp_server.py
```

This will automatically create a `.mcp.json` file in your project with the correct configuration.

#### Option B: Manual Configuration

Create a `.mcp.json` file in the project root with the following content:

```json
{
  "mcpServers": {
    "maritime": {
      "command": "python3",
      "args": ["mcp_server.py"]
    }
  }
}
```

**Note:** The paths are relative to the project root where the `.mcp.json` file is located.

### Step 3: Restart Claude Code

After adding the configuration, restart Claude Code to load the new MCP server.

## Usage

Once configured, Claude Code will have access to a new tool called `run_maritime_app`. You can ask Claude to:

- "Run the maritime app"
- "Execute the maritime application"
- "Show me the maritime demo"

The tool will execute the application and return the output, including:
- A colorful hello world message
- Current timestamp
- A random fun fact fetched from an API

## Testing the MCP Server

You can test the MCP server manually by running:

```bash
python3 mcp_server.py
```

Note: The server uses stdio for communication, so it won't display anything when run directly. It's meant to be used by Claude Code.

## Troubleshooting

### Module not found errors

If you get `ModuleNotFoundError` for `requests`, `colorama`, or other dependencies:
- Make sure you've activated your virtual environment (if using one)
- Reinstall dependencies: `pip3 install -r requirements.txt`

### MCP server not showing up in Claude Code

- Verify the `.mcp.json` file exists in the project root
- Check that the configuration format matches the example above
- Restart Claude Code after adding the configuration
- Run `claude mcp list` to see configured servers
- Check Claude Code logs for any error messages

### Tool execution fails

- Verify that `app.py` is in the same directory as `mcp_server.py`
- Ensure all dependencies are installed in the Python environment being used
- Check that the Python interpreter specified in the config (`python3`) is correct
