# ⚡ Orchestrix AI

### Multi-Agent Research Pipeline

Orchestrix AI is a Python-based multi-agent research system that automates the research process using specialized AI agents. It searches the web for relevant information, extracts content from selected sources, generates a structured research report, and evaluates the report using a critic agent.

## 🚀 Live Demo

**Try Orchestrix AI:** [Launch the Live App](https://orchestrix-ai.streamlit.app/)

Explore the application by entering a research topic and letting the AI agents work through the research pipeline.

## ✨ Features

- **Web Research:** Searches the web for relevant information using Tavily.
- **Content Extraction:** Retrieves and extracts useful content from selected web pages.
- **AI-Powered Report Generation:** Uses Google Gemini to generate structured research reports.
- **Report Evaluation:** A critic agent evaluates the generated report against the collected research.
- **Multi-Agent Workflow:** Separates searching, reading, writing, and reviewing into distinct stages.
- **Interactive Interface:** Provides a Streamlit-based interface for running research tasks.
- **Error Handling:** Includes handling for search, scraping, and model request failures.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web application |
| LangChain | LLM integration and prompt management |
| LangGraph | Multi-agent workflow orchestration |
| Google Gemini | AI-powered report generation and evaluation |
| Tavily Search API | Web search and research discovery |
| Beautiful Soup | HTML content extraction |
| Requests | HTTP requests and webpage retrieval |
| python-dotenv | Local environment variable management |
| Git and GitHub | Version control and source code hosting |

## 🏗️ Project Structure

```text
multi-agent-research-system/
│
├── app.py              # Streamlit user interface
├── agents.py           # AI model configuration and agent prompts
├── pipeline.py         # Research pipeline orchestration
├── tools.py            # Web search and webpage extraction tools
├── requirements.txt    # Python dependencies
├── .env.example        # Example environment configuration
├── .gitignore          # Files excluded from version control
└── README.md           # Project documentation
```

## 🔄 How It Works

Orchestrix AI follows a multi-stage research workflow.

### 1. Search Agent

Uses the Tavily Search API to discover relevant web pages and gather information related to the user's research topic.

### 2. Reader Agent

Retrieves and extracts useful text from a selected webpage using Requests and Beautiful Soup.

### 3. Writer Agent

Uses Google Gemini to synthesize the collected information into a structured research report.

### 4. Critic Agent

Reviews the generated report against the research material to identify unsupported claims and suggest improvements.

### Workflow Overview

```text
Research Topic
      │
      ▼
  Search Agent
      │
      ▼
  Reader Agent
      │
      ▼
  Writer Agent
      │
      ▼
  Critic Agent
      │
      ▼
Final Research Report
```

## 💻 Getting Started

Follow these instructions to run Orchestrix AI locally.

### Prerequisites

Install the following:

- Python
- Git
- Visual Studio Code or another Python IDE
- Google Gemini API key
- Tavily API key

### 1. Clone the Repository

```bash
git clone https://github.com/asmiraut23/multi-agent-research-system.git
```

Navigate to the project directory:

```bash
cd multi-agent-research-system
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

Install the packages listed in `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

If you use `uv`, you can install the dependencies with:

```bash
uv pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root directory.

Add your API keys:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Replace the placeholder values with your actual API keys.

**Security:** Never commit your `.env` file or publish your API keys to GitHub.

### 5. Run the Application

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal, usually:

```text
http://localhost:8501
```

## 🔑 API Configuration

Orchestrix AI requires API credentials for its external services.

| Environment Variable | Purpose |
|---|---|
| `GOOGLE_API_KEY` | Authenticates requests to Google Gemini |
| `TAVILY_API_KEY` | Authenticates web search requests through Tavily |

For Streamlit Community Cloud, configure these values in the application's **Secrets** settings rather than committing them to the repository.

## ☁️ Deployment

Orchestrix AI is configured for deployment using Streamlit Community Cloud.

**Live application:** [https://orchestrix-ai.streamlit.app/](https://orchestrix-ai.streamlit.app/)

The deployed application requires the correct entry-point file, installed dependencies, and valid API credentials.

## ⚠️ Limitations

- Research quality depends on the relevance and availability of search results.
- The Reader Agent extracts content from a selected webpage, so the report may not reflect every available source.
- Some websites may block automated requests or restrict access to their content.
- AI-generated reports may contain inaccuracies and should be checked against the cited research.
- API availability, rate limits, and network errors can affect execution.
- The Critic Agent provides an additional review but does not guarantee that every factual error will be detected.

## 🔮 Future Improvements

Potential enhancements include:

- Extracting information from multiple sources in a single research run.
- Adding direct source links and citations throughout the generated report.
- Implementing automatic retries and improved recovery from API failures.
- Adding report export options such as PDF and Markdown.
- Introducing source relevance scoring and more detailed evidence verification.
- Providing execution timing and agent-level status information in the interface.

## 👩‍💻 Author

**Asmi Raut**

