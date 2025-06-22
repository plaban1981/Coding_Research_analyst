## Code Run
```
uv run main.py
```
### Response from GROQ Models
```
(simple-agent) C:\Users\nayak\Documents\coding_assistant\simple_agent>uv run main.py
🛠️ Available Tools - firecrawl_scrape firecrawl_map firecrawl_crawl firecrawl_check_crawl_status firecrawl_search firecrawl_extract firecrawl_deep_research firecrawl_generate_llmstxt
------------------------------------------------------------

👤 You: which is the best agentic ai framework for building complex projects

🤖 Agent: The best agentic AI frameworks for building complex projects are:

1. LangChain
2. AutoGen
3. Semantic Kernel
4. Atomic Agents
5. CrewAI
6. RASA
7. Hugging Face Transformers Agents
8. Langflow
9. Lyzer
10. Microsoft AutoGen
11. LangGraph
12. Microsoft Semantic Kernel
13. Botpress
14. AutoGPT
15. Autogen
16. LlamaIndex
17. n8n
18. PydanticAI
19. Smolagents

These frameworks provide a range of features and capabilities for building AI agents, including workflow automation, natural language understanding, and machine learning. They can be used for various applications, such as customer support, virtual assistants, and data analysis.

👤 You:
```

## Response from Openai GPT4O
```
(simple-agent) C:\Users\nayak\Documents\coding_assistant\simple_agent>uv run main.py

🛠️ Available Tools - firecrawl_scrape firecrawl_map firecrawl_crawl firecrawl_check_crawl_status firecrawl_search firecrawl_extract firecrawl_deep_research firecrawl_generate_llmstxt
------------------------------------------------------------

👤 You: compare crewai and langgraph
🔄 Processing query...
🔧 Using Firecrawl tool: firecrawl_search
🔧 Using Firecrawl tool: firecrawl_search

🤖 Agent: Here's a quick comparison of CrewAI and LangGraph based on the latest information:

### CrewAI 🚀
- **Purpose**: CrewAI is a platform designed to streamline workflows across industries using powerful AI agents. It allows users to build and deploy automated workflows using any LLM and cloud platform.
- **Features**:
  - Multi-agent platform for building and orchestrating workflows.
  - Offers no-code tools and templates for quick setup.
  - Provides tools for deployment, monitoring, and iteration of AI agents.
  - Supports cloud, self-hosted, or local deployment.
  - Integrates easily with various applications.
- **Use Cases**: Widely used in industries like finance, healthcare, marketing, and more for tasks like strategic planning, performance metrics optimization, and AI automation.

### LangGraph 🌐
- **Purpose**: LangGraph, part of the LangChain suite, is a framework for building and scaling AI workloads, including conversational agents and complex task automation.
- **Features**:
  - Supports diverse control flows (single, multi-agent, hierarchical).
  - Offers human-in-the-loop capabilities for moderation and quality control.
  - Provides built-in memory for long-term interactions and statefulness.
  - Designed for human-agent collaboration with customizable workflows.
  - Offers first-class streaming for real-time user experience.
- **Use Cases**: Used by companies for building reliable, stateful, multi-actor applications with LLMs, focusing on agentic workflows and human-agent collaboration.

Both platforms are designed to enhance AI-driven automation and agent-based workflows, but they cater to slightly different needs and industries. CrewAI focuses on multi-agent automation across various sectors, while LangGraph emphasizes building scalable, stateful AI applications with a strong focus on human-agent collaboration.

👤 You:
```

