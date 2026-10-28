# Multi-Agent Research System

An AI-powered research application that automates web research, extracts webpage content, generates structured research reports, and evaluates report quality using an AI critic.

## Features

- **Web Research:** Retrieves relevant information using Tavily Search.
- **Web Scraping:** Extracts readable content from webpages using Requests and BeautifulSoup.
- **AI Report Generation:** Uses Google Gemini to generate structured research reports.
- **AI Critic:** Evaluates reports for factual accuracy, source quality, unsupported claims, and missing information.
- **Interactive Interface:** Uses Streamlit to run the research pipeline and display results.
- **Error Handling:** Includes API retries, timeout configuration, and error handling for web requests.

## Tech Stack

- **Language:** Python
- **LLM:** Google Gemini
- **AI Frameworks:** LangChain, LangGraph
- **Search API:** Tavily
- **Web Scraping:** BeautifulSoup, Requests
- **Frontend:** Streamlit
- **Environment Management:** Python virtual environment, python-dotenv

## System Workflow

1. **Search Agent:** Searches the web for relevant research information.
2. **Reader Agent:** Selects a relevant URL and extracts webpage content.
3. **Writer Chain:** Generates a structured research report using the gathered information.
4. **Critic Chain:** Evaluates the report against the supplied research evidence and provides a score and feedback.

## Project Structure

```text
multi-agent-research-system/
├── .streamlit/
│   └── config.toml
├── agents.py
├── app.py
├── pipeline.py
├── tools.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Prerequisites

- Python 3.10 or later
- Google Gemini API key
- Tavily API key

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/multi-agent-research-system.git
cd multi-agent-research-system
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root using `.env.example` as a reference.

Add your API keys:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Replace the placeholder values with your actual API keys.

**Security:** Never commit your `.env` file or expose your API keys publicly.

### 5. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal to access the application.

## Example Use Case

Enter a research topic, such as:

`Applications of Multi-Agent AI Systems in Healthcare`

The application searches for relevant information, extracts webpage content, generates a research report, and evaluates the report using the AI critic.

## Future Improvements

- Gather evidence from multiple relevant webpages.
- Improve source citations and claim-level traceability.
- Add report download functionality.
- Enhance research evaluation and reporting.

## Security and Limitations

- API keys must be configured securely through environment variables or the deployment platform's secrets manager.
- Web scraping results depend on website accessibility and content structure.
- Report accuracy depends on the quality and coverage of the retrieved evidence.
- The AI critic provides automated feedback; its score should not be treated as a guarantee of factual correctness.

## Author

**Asmi Raut**
