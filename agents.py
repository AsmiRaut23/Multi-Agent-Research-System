from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search, scrape_url

from dotenv import load_dotenv
load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0,timeout=120,max_retries=3)

# first agent
def build_search_agent():
    return create_agent(
        model = llm,
        tools= [web_search]
    )

#second agent
def build_search_reader_agent():
    return create_agent(
        model = llm,
        tools = [scrape_url]
    )

# writer chain
writer_prompt = ChatPromptTemplate.from_messages([
    ('system', "You are an expert research writer. Write clear, structured and insightful reports."),
     ('human', """Write a detailed research report on the topic below.
     Topic: {topic}
     
     Research Gathered:
     {research}

     Structure the report as:
     - Introduction
     - Key Findings (minimum 3 well-explained points)
     - Conclusion
     - Sources (list all URLs found in the research)

     Be detailed, factual and professional."""),
])

writer_chain = writer_prompt | llm | StrOutputParser()

# Critic Chain
critic_prompt = ChatPromptTemplate.from_messages([
    ('system', """You are a strict research evaluator.
    Evaluate the report based on factual accuracy, evidence, and source quality.
    Do not assume that a claim is true simply because it appears in the report.
    Identify claims that are unsupported by the provided research.
    Do not invent facts or sources."""),
    
    ('human', """Evaluate the research report using the original research evidence.

    Original Research Evidence:
    {research}

    Research Report:
    {report}

    Evaluate:
    1. Factual accuracy and support from the provided evidence.
    2. Source quality and whether source URLs are available.
    3. Unsupported claims or information that needs verification.
    4. Missing important information.

    Respond in this exact format:

    Score: X/10

    Strengths:
    - ...

    Areas to Improve:
    - ...

    Unsupported Claims:
    - ...

    One line verdict:
    ..."""),
])

critic_chain = critic_prompt | llm | StrOutputParser()