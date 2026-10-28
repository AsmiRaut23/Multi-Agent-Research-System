from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
from dotenv import load_dotenv
from rich import print # it gets printed in a more readable format
load_dotenv()


tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query: str) -> str:
    """Search the web for relevant information. Returns titles, URLs, and snippets."""
    try:
        results = tavily.search(
            query=query,
            max_results=5,
            search_depth="advanced"
        )

        output = []

        for result in results.get("results", []):
            output.append(
                f"Title: {result.get('title', 'No title')}\n"
                f"URL: {result.get('url', 'No URL')}\n"
                f"Snippet: {result.get('content', 'No content')[:500]}\n"
            )

        if not output:
            return "No search results were found."

        return "\n-----\n".join(output)

    except Exception as e:
        return f"Web search failed: {str(e)}"

#print(web_search.invoke("what is the recent news of protest in India?"))


@tool
def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading."""
    try:
        resp = requests.get(url, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
        resp.raise_for_status()
        
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script","style", "nav", "footer","header", "aside", "noscript"]):
            tag.decompose()
        text = soup.get_text(separator=" ", strip=True)

        if not text:
            return f"No readable text found at: {url}"

        return f"Source URL: {url}\n\n{text[:5000]}"

    except requests.exceptions.Timeout:
        return f"Scraping timed out for URL: {url}"

    except requests.exceptions.HTTPError as e:
        return f"HTTP error while scraping {url}: {e}"

    except requests.exceptions.RequestException as e:
        return f"Request failed for {url}: {e}"

    except Exception as e:
        return f"Could not scrape URL {url}: {e}"

#print(scrape_url.invoke("https://www.bbc.com/news/articles/c64g17jqy5ddo"))





