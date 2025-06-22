from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    max_tokens=10000,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

server_params = StdioServerParameters(
    command="npx",
    env={
        "FIRECRAWL_API_KEY": os.getenv("FIRECRAWL_API_KEY"),
    },
    args=["firecrawl-mcp"]
)


def manage_message_history(messages, max_messages=6):
    """Keep only the most recent messages to prevent context length issues"""
    if len(messages) > max_messages:
        # Keep system message and the most recent messages
        system_message = messages[0]
        recent_messages = messages[-max_messages+1:]
        return [system_message] + recent_messages
    return messages


async def main():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)
            agent = create_react_agent(model, tools)

            messages = [
                {
                    "role": "system",
                    "content": "You are a helpful assistant that can scrape websites, crawl pages, and extract data using Firecrawl tools. Think step by step and use the appropriate tools to help the user. Use emojis frequently to make your responses more engaging and friendly! 🚀✨. Keep responses concise."
                }
            ]

            print("🛠️ Available Tools -", *[tool.name for tool in tools])
            print("-" * 60)

            while True:
                user_input = input("\n👤 You: ")
                if user_input.lower() in ["quit", "exit", "bye"]:
                    print("👋 Goodbye! Have a great day! ✨")
                    break

                # Limit user input to prevent context issues
                user_input = user_input[:2000]  # Much smaller limit
                messages.append({"role": "user", "content": user_input})
                
                try:
                    agent_response = await agent.ainvoke({"messages": messages})

                    ai_message = agent_response["messages"][-1].content
                    print("\n🤖 Agent:", ai_message)    
                except Exception as e:
                    print("❌ Error:", e)
                    # Remove the last user message if it caused an error
                    if messages and messages[-1]["role"] == "user":
                        messages.pop()


if __name__ == "__main__":
    asyncio.run(main())