import sys
from dotenv import load_dotenv

from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_toolset import StdioServerParameters
from google.adk.models.lite_llm import LiteLlm
import sys

# --- Load Environment Variables (If ADK tools need them, e.g., API keys) ---
load_dotenv() # Create a .env file in the same directory if needed
 
root_agent = LlmAgent(
    # model=LiteLlm(model="openai/qwen3:0.6b"),
    model='gemini-2.5-pro-preview-05-06',
    name='mcp_server_client',
    instruction="You are a helpful assistant that has access to tools, only use your tools to get help the user",
    tools=[
        MCPToolset(
            connection_params=StdioServerParameters(
                command='python3',
                args=["/Users/jvillarreal/Documents/playground/markmap_mcp_server/mcp_stdio_mindmap_mcp_server/mcp_server.py"],
                # args=["mcp_stdio_mindmap_mcp_server/mcp_server.py"],
            )
            ,errlog=sys.stderr
        ),
        # MCPToolset(
        #     connection_params=StdioServerParameters(
        #         command='npx',
        #         args=["-y", "@jinzcdev/markmap-mcp-server"],
        #         env={"MARKMAP_DIR": "/Users/jvillarreal/Documents/playground/markmap_mcp_server"},
        #     )
        #     ,errlog=sys.stderr
        # )
    ],
)

 