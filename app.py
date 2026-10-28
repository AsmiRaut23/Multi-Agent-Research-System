# import time
# import streamlit as st

# from agents import (
#     build_search_agent,
#     build_search_reader_agent,
#     writer_chain,
#     critic_chain,
# )

# st.set_page_config(
#     page_title="Orchestrix AI",
#     page_icon="⚡",
#     layout="wide",
#     initial_sidebar_state="collapsed",
# )

# # ---------------------------------------------------------------------------
# # Styling
# # ---------------------------------------------------------------------------
# CSS = """
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Syne:wght@600;700;800&family=DM+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

# :root {
#     --bg: #070714;
#     --card: #0e0e22;
#     --card-border: #1f1f40;
#     --text: #eef0ff;
#     --muted: #8d8fb5;
#     --accent: #8b5cff;
#     --accent-2: #ff4fd8;
#     --cyan: #22d3ee;
#     --green: #34f5b0;
# }

# /* base */
# .stApp {
#     background:
#         radial-gradient(700px 320px at 20% -60px, rgba(139,92,255,0.28), transparent 70%),
#         radial-gradient(700px 320px at 85% -40px, rgba(34,211,238,0.16), transparent 70%),
#         var(--bg);
#     color: var(--text);
#     font-family: 'DM Sans', sans-serif;
# }
# #MainMenu, footer, header[data-testid="stHeader"], [data-testid="stSidebar"],
# [data-testid="collapsedControl"], [data-testid="stToolbar"] { display: none !important; }
# .block-container { max-width: 1120px; padding-top: 3.2rem; padding-bottom: 4rem; }
# p, li, span, label, div { font-family: 'DM Sans', sans-serif; }
# h1, h2, h3, h4 { font-family: 'Syne', sans-serif !important; color: var(--text) !important; letter-spacing: -0.01em; }

# /* hero */
# .hero h1 { font-size: 3.1rem; font-weight: 800; margin: 0; line-height: 1.05; }
# .hero h1 .accent {
#     background: linear-gradient(90deg, #a78bff, var(--accent-2));
#     -webkit-background-clip: text; background-clip: text; color: transparent;
# }
# .hero p { color: var(--muted); font-size: 1.05rem; margin: 0.9rem 0 2.4rem; max-width: 560px; }

# /* labels */
# .field-label {
#     font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; letter-spacing: 0.14em;
#     text-transform: uppercase; color: var(--cyan); margin: 0 0 0.45rem;
# }
# .try-label {
#     font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; letter-spacing: 0.14em;
#     text-transform: uppercase; color: #5f6190; margin: 1.6rem 0 0.6rem;
# }
# .section-title { font-family: 'Syne', sans-serif; font-weight: 700; font-size: 1.5rem; margin: 0 0 1rem; }

# /* text input */
# [data-testid="stTextInput"] input {
#     background: #12122a !important; color: var(--text) !important;
#     border: 1px solid #2a2a50 !important; border-radius: 12px !important;
#     padding: 0.85rem 1rem !important; font-size: 1rem !important;
# }
# [data-testid="stTextInput"] input:focus {
#     border-color: var(--accent) !important; box-shadow: 0 0 0 3px rgba(139,92,255,0.25) !important;
# }
# [data-testid="stTextInput"] label { display: none; }
# [data-testid="InputInstructions"] { display: none; }

# /* primary button */
# button[data-testid="stBaseButton-primary"] {
#     width: 100%; border: none !important; border-radius: 12px !important;
#     padding: 0.85rem 1rem !important; font-weight: 600 !important; font-size: 1rem !important;
#     background: linear-gradient(90deg, #7c5cff, var(--accent-2)) !important; color: #fff !important;
#     box-shadow: 0 8px 30px rgba(139,92,255,0.40);
#     transition: transform .15s ease, box-shadow .15s ease;
# }
# button[data-testid="stBaseButton-primary"]:hover {
#     transform: translateY(-1px); box-shadow: 0 12px 38px rgba(255,79,216,0.45);
# }

# /* topic chips (secondary buttons) */
# button[data-testid="stBaseButton-secondary"] {
#     background: #13132a !important; color: #c8cae8 !important;
#     border: 1px solid #26264a !important; border-radius: 8px !important;
#     padding: 0.25rem 0.8rem !important; font-size: 0.85rem !important; min-height: 0 !important;
# }
# button[data-testid="stBaseButton-secondary"]:hover {
#     border-color: var(--cyan) !important; color: var(--cyan) !important;
# }
# [data-testid="stDownloadButton"] button {
#     background: #13132a !important; color: var(--text) !important;
#     border: 1px solid #2a2a50 !important; border-radius: 10px !important;
# }

# /* pipeline cards */
# .step {
#     display: flex; justify-content: space-between; align-items: center;
#     background: var(--card); border: 1px solid var(--card-border); border-left: 3px solid #25254a;
#     border-radius: 14px; padding: 1.05rem 1.3rem; margin-bottom: 0.85rem;
#     transition: border-color .3s ease, background .3s ease;
# }
# .step .num { font-family: 'JetBrains Mono', monospace; font-size: 0.78rem; color: var(--cyan); margin-right: 0.8rem; }
# .step .name { font-family: 'Syne', sans-serif; font-weight: 700; font-size: 1.05rem; }
# .step .desc { color: var(--muted); font-size: 0.88rem; margin-top: 0.3rem; }
# .step .status { font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; letter-spacing: 0.14em; color: #5f6190; }
# .step.running { border-left-color: var(--accent-2); background: #12102c; border-color: #3a2d7a; animation: pulse 1.4s ease-in-out infinite; }
# .step.running .status { color: var(--accent-2); }
# .step.done { border-left-color: var(--green); }
# .step.done .status { color: var(--green); }
# .step.error { border-left-color: #ff4d4d; }
# .step.error .status { color: #ff4d4d; }
# @keyframes pulse { 0%,100% { box-shadow: 0 0 0 0 rgba(139,92,255,0.0); } 50% { box-shadow: 0 0 24px 0 rgba(139,92,255,0.35); } }
# @media (prefers-reduced-motion: reduce) { .step.running { animation: none; } }

# /* results */
# .result-head { font-family: 'Syne', sans-serif; font-size: 1.9rem; font-weight: 800; margin: 3rem 0 0.2rem; }
# .result-meta { font-family: 'JetBrains Mono', monospace; font-size: 0.78rem; color: var(--muted); margin-bottom: 1.2rem; }
# [data-baseweb="tab-list"] { gap: 0.4rem; border-bottom: 1px solid var(--card-border); }
# [data-baseweb="tab"] { background: transparent !important; color: var(--muted) !important; }
# [aria-selected="true"][data-baseweb="tab"] { color: var(--cyan) !important; }
# [data-baseweb="tab-highlight"] { background: linear-gradient(90deg, var(--accent), var(--accent-2)) !important; }
# .report-card {
#     background: var(--card); border: 1px solid var(--card-border); border-radius: 16px; padding: 1.6rem 1.8rem;
# }
# .stMarkdown p, .stMarkdown li { line-height: 1.7; }
# </style>
# """
# st.markdown(CSS, unsafe_allow_html=True)

# # ---------------------------------------------------------------------------
# # Helpers
# # ---------------------------------------------------------------------------
# STEPS = [
#     ("Search Agent", "Gathers recent web information"),
#     ("Reader Agent", "Scrapes & extracts deep content"),
#     ("Writer Chain", "Drafts the full research report"),
#     ("Critic Chain", "Reviews & scores the report"),
# ]
# LABELS = {"waiting": "WAITING", "running": "RUNNING", "done": "DONE", "error": "FAILED"}
# EXAMPLES = ["LLM agents 2025", "CRISPR gene editing", "Fusion energy progress"]


# def extract_text(content) -> str:
#     """Agent output can be a string or a list of content blocks."""
#     if isinstance(content, str):
#         return content
#     if isinstance(content, list):
#         parts = [b.get("text", "") if isinstance(b, dict) else str(b) for b in content]
#         return "\n".join(p for p in parts if p)
#     return str(content)


# def pipeline_html(statuses: list) -> str:
#     cards = []
#     for i, ((name, desc), status) in enumerate(zip(STEPS, statuses), start=1):
#         cards.append(
#             f'<div class="step {status}">'
#             f'<div><div><span class="num">0{i}</span><span class="name">{name}</span></div>'
#             f'<div class="desc">{desc}</div></div>'
#             f'<div class="status">{LABELS[status]}</div></div>'
#         )
#     return "".join(cards)


# def set_topic(value: str):
#     st.session_state["topic_input"] = value


# def run_pipeline(topic: str, slot) -> dict:
#     """Same 4 steps as pipeline.py, updating the pipeline cards live."""
#     statuses = ["waiting"] * 4
#     state, t0 = {}, time.time()

#     def show(idx, status):
#         statuses[idx] = status
#         slot.markdown(pipeline_html(statuses), unsafe_allow_html=True)

#     current = 0
#     try:
#         # 1 - search
#         show(0, "running")
#         res = build_search_agent().invoke(
#             {"messages": [("user", f"Find recent, reliable and detailed information about: {topic}")]}
#         )
#         state["search_results"] = extract_text(res["messages"][-1].content)
#         show(0, "done")

#         # 2 - reader
#         current = 1
#         show(1, "running")
#         res = build_search_reader_agent().invoke(
#             {
#                 "messages": [
#                     (
#                         "user",
#                         f"Based on the following search results about '{topic}', "
#                         f"pick the most relevant URL and scrape it for deeper content.\n\n"
#                         f"Search Results:\n{state['search_results'][:800]}",
#                     )
#                 ]
#             }
#         )
#         state["scraped_content"] = extract_text(res["messages"][-1].content)
#         show(1, "done")

#         # 3 - writer
#         current = 2
#         show(2, "running")
#         research = (
#             f"Search Results: \n {state['search_results']} \n\n"
#             f"Detailed scraped content: \n {state['scraped_content']}"
#         )
#         state["report"] = extract_text(writer_chain.invoke({"topic": topic, "research": research}))
#         show(2, "done")

#         # 4 - critic
#         current = 3
#         show(3, "running")
#         state["feedback"] = extract_text(critic_chain.invoke({
#             "research": (
#             f"Search Results:\n{state['search_results']}\n\n"
#             f"Scraped Content:\n{state['scraped_content']}"
#             ),
#             "report": state["report"]
#             })
#             )
#         show(3, "done")
#     except Exception as e:
#         show(current, "error")
#         raise e
#     finally:
#         st.session_state["statuses"] = statuses

#     state["topic"] = topic
#     state["elapsed"] = time.time() - t0
#     return state


# # ---------------------------------------------------------------------------
# # Layout
# # ---------------------------------------------------------------------------
# st.markdown(
#     '<div class="hero"><h1>Multi-agent <span class="accent">research</span> pipeline</h1>'
#     "<p>Four agents search the web, read the best source, write a report and critique it. "
#     "Pick a topic and watch each step run.</p></div>",
#     unsafe_allow_html=True,
# )

# left, spacer, right = st.columns([5, 0.4, 5])

# with left:
#     st.markdown('<div class="field-label">Research topic</div>', unsafe_allow_html=True)
#     topic = st.text_input(
#         "Research topic",
#         key="topic_input",
#         placeholder="e.g. Quantum computing breakthroughs in 2025",
#         label_visibility="collapsed",
#     )
#     run_clicked = st.button("⚡  Run Research Pipeline", type="primary", use_container_width=True)

#     st.markdown('<div class="try-label">Try →</div>', unsafe_allow_html=True)
#     for ex in EXAMPLES:
#         st.button(ex, key=f"ex_{ex}", on_click=set_topic, args=(ex,))

# with right:
#     st.markdown('<div class="section-title">Pipeline</div>', unsafe_allow_html=True)
#     pipeline_slot = st.empty()
#     pipeline_slot.markdown(
#         pipeline_html(st.session_state.get("statuses", ["waiting"] * 4)),
#         unsafe_allow_html=True,
#     )

# # ---------------------------------------------------------------------------
# # Run
# # ---------------------------------------------------------------------------
# if run_clicked:
#     if not topic.strip():
#         st.warning("Enter a topic to start.")
#     else:
#         try:
#             st.session_state["result"] = run_pipeline(topic.strip(), pipeline_slot)
#         except Exception as e:
#             st.error(f"The pipeline failed: {e}")
#             st.caption("Check the API keys in your .env file and your internet connection, then try again.")

# # ---------------------------------------------------------------------------
# # Results
# # ---------------------------------------------------------------------------
# result = st.session_state.get("result")
# if result:
#     st.markdown(f'<div class="result-head">{result["topic"]}</div>', unsafe_allow_html=True)
#     st.markdown(
#         f'<div class="result-meta">Finished in {result["elapsed"]:.0f}s</div>',
#         unsafe_allow_html=True,
#     )

#     tab_report, tab_feedback, tab_search, tab_scraped = st.tabs(
#         ["Report", "Critic feedback", "Search results", "Scraped content"]
#     )
#     with tab_report:
#         with st.container(border=True):
#             st.markdown(result["report"])
#         st.download_button(
#             "Download report (.md)",
#             data=result["report"],
#             file_name="research_report.md",
#             mime="text/markdown",
#         )
#     with tab_feedback:
#         with st.container(border=True):
#             st.markdown(result["feedback"])
#     with tab_search:
#         with st.container(border=True):
#             st.markdown(result["search_results"])
#     with tab_scraped:
#         with st.container(border=True):
#             st.markdown(result["scraped_content"])

































import time
import streamlit as st

from agents import (
    build_search_agent,
    build_search_reader_agent,
    writer_chain,
    critic_chain,
)

st.set_page_config(
    page_title="Orchestrix AI",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------------------------
# Styling
# ---------------------------------------------------------------------------
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@600;700;800&family=DM+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
    --bg: #070a16;
    --card: #0e0e22;
    --card-border: #1f1f40;
    --text: #eef0ff;
    --muted: #8d8fb5;
    --accent: #8b5cff;
    --accent-2: #ff4fd8;
    --cyan: #22d3ee;
    --green: #34f5b0;
}

/* base */
.stApp {
    background:
        radial-gradient(700px 320px at 12% -35px, rgba(139, 45, 190, 0.20), transparent 72%),
        radial-gradient(700px 320px at 92% -35px, rgba(30, 100, 145, 0.13), transparent 72%),
        linear-gradient(180deg, #0b1020 0%, #070914 58%, #070714 100%);
    color: var(--text);
    font-family: 'DM Sans', sans-serif;
}
#MainMenu, footer, header[data-testid="stHeader"], [data-testid="stSidebar"],
[data-testid="collapsedControl"], [data-testid="stToolbar"] { display: none !important; }
.block-container { max-width: 1120px; padding-top: 3.2rem; padding-bottom: 4rem; }
p, li, span, label, div { font-family: 'DM Sans', sans-serif; }
h1, h2, h3, h4 { font-family: 'Syne', sans-serif !important; color: var(--text) !important; letter-spacing: -0.01em; }

/* hero */
.hero .brand-name {
    font-family: 'DM Sans', sans-serif;
    font-size: clamp(3.2rem, 6vw, 5rem);
    font-weight: 800;
    line-height: 1.02;
    margin: 0 0 0.45rem;
    letter-spacing: -0.045em;
    background: linear-gradient(100deg, #ffd0f1 0%, #ed8ce7 30%, #bd55e8 62%, #6818c8 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
}
.hero h1 {
    font-size: clamp(1.8rem, 3.5vw, 2.65rem);
    font-weight: 800;
    margin: 0;
    line-height: 1.12;
    letter-spacing: -0.035em;
}
.hero h1 .accent {
    background: linear-gradient(90deg, #bd79e9 0%, #b66bdf 55%, #a65bd0 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
}
.hero p { display: none; }

/* labels */
.field-label {
    font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; letter-spacing: 0.14em;
    text-transform: uppercase; color: var(--cyan); margin: 0 0 0.45rem;
}
.try-label {
    font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; letter-spacing: 0.14em;
    text-transform: uppercase; color: #5f6190; margin: 1.6rem 0 0.6rem;
}
.section-title { font-family: 'Syne', sans-serif; font-weight: 700; font-size: 1.5rem; margin: 0 0 1rem; }

/* text input */
[data-testid="stTextInput"] input {
    background: #12122a !important; color: var(--text) !important;
    border: 1px solid #2a2a50 !important; border-radius: 12px !important;
    padding: 0.85rem 1rem !important; font-size: 1rem !important;
}
[data-testid="stTextInput"] input:focus {
    border-color: var(--accent) !important; box-shadow: 0 0 0 3px rgba(139,92,255,0.25) !important;
}
[data-testid="stTextInput"] label { display: none; }
[data-testid="InputInstructions"] { display: none; }

/* primary button */
button[data-testid="stBaseButton-primary"] {
    width: 100%; border: none !important; border-radius: 12px !important;
    padding: 0.85rem 1rem !important; font-weight: 600 !important; font-size: 1rem !important;
    background: linear-gradient(90deg, #7c5cff, var(--accent-2)) !important; color: #fff !important;
    box-shadow: 0 8px 30px rgba(139,92,255,0.40);
    transition: transform .15s ease, box-shadow .15s ease;
}
button[data-testid="stBaseButton-primary"]:hover {
    transform: translateY(-1px); box-shadow: 0 12px 38px rgba(255,79,216,0.45);
}

/* topic chips (secondary buttons) */
button[data-testid="stBaseButton-secondary"] {
    background: #13132a !important; color: #c8cae8 !important;
    border: 1px solid #26264a !important; border-radius: 8px !important;
    padding: 0.25rem 0.8rem !important; font-size: 0.85rem !important; min-height: 0 !important;
}
button[data-testid="stBaseButton-secondary"]:hover {
    border-color: var(--cyan) !important; color: var(--cyan) !important;
}
[data-testid="stDownloadButton"] button {
    background: #13132a !important; color: var(--text) !important;
    border: 1px solid #2a2a50 !important; border-radius: 10px !important;
}

/* pipeline cards */
.step {
    display: flex; justify-content: space-between; align-items: center;
    background: var(--card); border: 1px solid var(--card-border); border-left: 3px solid #25254a;
    border-radius: 14px; padding: 1.05rem 1.3rem; margin-bottom: 0.85rem;
    transition: border-color .3s ease, background .3s ease;
}
.step .num { font-family: 'JetBrains Mono', monospace; font-size: 0.78rem; color: var(--cyan); margin-right: 0.8rem; }
.step .name { font-family: 'Syne', sans-serif; font-weight: 700; font-size: 1.05rem; }
.step .desc { color: var(--muted); font-size: 0.88rem; margin-top: 0.3rem; }
.step .status { font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; letter-spacing: 0.14em; color: #5f6190; }
.step.running { border-left-color: var(--accent-2); background: #12102c; border-color: #3a2d7a; animation: pulse 1.4s ease-in-out infinite; }
.step.running .status { color: var(--accent-2); }
.step.done { border-left-color: var(--green); }
.step.done .status { color: var(--green); }
.step.error { border-left-color: #ff4d4d; }
.step.error .status { color: #ff4d4d; }
@keyframes pulse { 0%,100% { box-shadow: 0 0 0 0 rgba(139,92,255,0.0); } 50% { box-shadow: 0 0 24px 0 rgba(139,92,255,0.35); } }
@media (prefers-reduced-motion: reduce) { .step.running { animation: none; } }

/* results */
.result-head { font-family: 'Syne', sans-serif; font-size: 1.9rem; font-weight: 800; margin: 3rem 0 0.2rem; }
.result-meta { font-family: 'JetBrains Mono', monospace; font-size: 0.78rem; color: var(--muted); margin-bottom: 1.2rem; }
[data-baseweb="tab-list"] { gap: 0.4rem; border-bottom: 1px solid var(--card-border); }
[data-baseweb="tab"] { background: transparent !important; color: var(--muted) !important; }
[aria-selected="true"][data-baseweb="tab"] { color: var(--cyan) !important; }
[data-baseweb="tab-highlight"] { background: linear-gradient(90deg, var(--accent), var(--accent-2)) !important; }
.report-card {
    background: var(--card); border: 1px solid var(--card-border); border-radius: 16px; padding: 1.6rem 1.8rem;
}
.stMarkdown p, .stMarkdown li { line-height: 1.7; }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
STEPS = [
    ("Search Agent", "Gathers recent web information"),
    ("Reader Agent", "Scrapes & extracts deep content"),
    ("Writer Chain", "Drafts the full research report"),
    ("Critic Chain", "Reviews & scores the report"),
]
LABELS = {"waiting": "WAITING", "running": "RUNNING", "done": "DONE", "error": "FAILED"}
EXAMPLES = ["LLM agents 2025", "CRISPR gene editing", "Fusion energy progress"]


def extract_text(content) -> str:
    """Agent output can be a string or a list of content blocks."""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = [b.get("text", "") if isinstance(b, dict) else str(b) for b in content]
        return "\n".join(p for p in parts if p)
    return str(content)


def pipeline_html(statuses: list) -> str:
    cards = []
    for i, ((name, desc), status) in enumerate(zip(STEPS, statuses), start=1):
        cards.append(
            f'<div class="step {status}">'
            f'<div><div><span class="num">0{i}</span><span class="name">{name}</span></div>'
            f'<div class="desc">{desc}</div></div>'
            f'<div class="status">{LABELS[status]}</div></div>'
        )
    return "".join(cards)


def set_topic(value: str):
    st.session_state["topic_input"] = value


def run_pipeline(topic: str, slot) -> dict:
    """Same 4 steps as pipeline.py, updating the pipeline cards live."""
    statuses = ["waiting"] * 4
    state, t0 = {}, time.time()

    def show(idx, status):
        statuses[idx] = status
        slot.markdown(pipeline_html(statuses), unsafe_allow_html=True)

    current = 0
    try:
        # 1 - search
        show(0, "running")
        res = build_search_agent().invoke(
            {"messages": [("user", f"Find recent, reliable and detailed information about: {topic}")]}
        )
        state["search_results"] = extract_text(res["messages"][-1].content)
        show(0, "done")

        # 2 - reader
        current = 1
        show(1, "running")
        res = build_search_reader_agent().invoke(
            {
                "messages": [
                    (
                        "user",
                        f"Based on the following search results about '{topic}', "
                        f"pick the most relevant URL and scrape it for deeper content.\n\n"
                        f"Search Results:\n{state['search_results'][:800]}",
                    )
                ]
            }
        )
        state["scraped_content"] = extract_text(res["messages"][-1].content)
        show(1, "done")

        # 3 - writer
        current = 2
        show(2, "running")
        research = (
            f"Search Results: \n {state['search_results']} \n\n"
            f"Detailed scraped content: \n {state['scraped_content']}"
        )
        state["report"] = extract_text(writer_chain.invoke({"topic": topic, "research": research}))
        show(2, "done")

        # 4 - critic
        current = 3
        show(3, "running")
        state["feedback"] = extract_text(critic_chain.invoke({
            "research": (
            f"Search Results:\n{state['search_results']}\n\n"
            f"Scraped Content:\n{state['scraped_content']}"
            ),
            "report": state["report"]
            })
            )
        show(3, "done")
    except Exception as e:
        show(current, "error")
        raise e
    finally:
        st.session_state["statuses"] = statuses

    state["topic"] = topic
    state["elapsed"] = time.time() - t0
    return state


# ---------------------------------------------------------------------------
# Layout
# ---------------------------------------------------------------------------
st.markdown(
    '<div class="hero"><div class="brand-name">Orchestrix AI</div>'
    '<h1>Multi-agent <span class="accent">research</span> pipeline</h1></div>',
    unsafe_allow_html=True,
)

left, spacer, right = st.columns([5, 0.4, 5])

with left:
    st.markdown('<div class="field-label">Research topic</div>', unsafe_allow_html=True)
    topic = st.text_input(
        "Research topic",
        key="topic_input",
        placeholder="e.g. Quantum computing breakthroughs in 2025",
        label_visibility="collapsed",
    )
    run_clicked = st.button("⚡  Run Research Pipeline", type="primary", use_container_width=True)

    st.markdown('<div class="try-label">Try →</div>', unsafe_allow_html=True)
    for ex in EXAMPLES:
        st.button(ex, key=f"ex_{ex}", on_click=set_topic, args=(ex,))

with right:
    st.markdown('<div class="section-title">Pipeline</div>', unsafe_allow_html=True)
    pipeline_slot = st.empty()
    pipeline_slot.markdown(
        pipeline_html(st.session_state.get("statuses", ["waiting"] * 4)),
        unsafe_allow_html=True,
    )

# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------
if run_clicked:
    if not topic.strip():
        st.warning("Enter a topic to start.")
    else:
        try:
            st.session_state["result"] = run_pipeline(topic.strip(), pipeline_slot)
        except Exception as e:
            st.error(f"The pipeline failed: {e}")
            st.caption("Check the API keys in your .env file and your internet connection, then try again.")

# ---------------------------------------------------------------------------
# Results
# ---------------------------------------------------------------------------
result = st.session_state.get("result")
if result:
    st.markdown(f'<div class="result-head">{result["topic"]}</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="result-meta">Finished in {result["elapsed"]:.0f}s</div>',
        unsafe_allow_html=True,
    )

    tab_report, tab_feedback, tab_search, tab_scraped = st.tabs(
        ["Report", "Critic feedback", "Search results", "Scraped content"]
    )
    with tab_report:
        with st.container(border=True):
            st.markdown(result["report"])
        st.download_button(
            "Download report (.md)",
            data=result["report"],
            file_name="research_report.md",
            mime="text/markdown",
        )
    with tab_feedback:
        with st.container(border=True):
            st.markdown(result["feedback"])
    with tab_search:
        with st.container(border=True):
            st.markdown(result["search_results"])
    with tab_scraped:
        with st.container(border=True):
            st.markdown(result["scraped_content"])