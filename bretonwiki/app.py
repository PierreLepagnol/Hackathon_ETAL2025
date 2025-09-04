import wikipedia
import wikipediaapi

wikipedia.set_lang("br")  # set language to Breton

HEADERS = {
    "User-Agent": "MyBretonWikiScraper/1.0 (contact: youremail@example.com)"
}


def extract_sections(sections, level=0):
    """
    Recursively extract section title and text with hierarchy level.
    """
    data = []
    for section in sections:
        if section.text.strip():  # only keep non-empty
            data.append({
                "title": section.title,
                "level": level,
                "text": section.text.strip()
            })
        data.extend(extract_sections(section.sections, level=level + 1))
    return data


def level_to_label(level: int) -> str:
    """
    Converts numeric level to a readable label for LLM-friendly formatting.
    """
    if level == 0:
        return "Section"
    else:
        return "Sub" * level + "section"


def get_wikipedia(title: str, is_only_summary=True) -> str:
    """
    Fetches a Breton Wikipedia page and returns a formatted string:
    [Title], [Summary], [Section/Subsection ...]
    """
    wiki = wikipediaapi.Wikipedia(
        language="br",
        user_agent=HEADERS["User-Agent"]
    )
    page = wiki.page(title)

    # If exact page not found, try wikipedia.search fallback
    if not page.exists():
        search_results = wikipedia.search(title, results=5)
        if search_results:
            page = wiki.page(search_results[0])
            if not page.exists():
                return f"[ERROR]\nPage '{title}' not found (even after search fallback)."
        else:
            return f"[ERROR]\nPage '{title}' not found (no search results)."

    # Extract sections
    sections = extract_sections(page.sections)

    # Build formatted string
    formatted = []
    formatted.append(f"[Title]\n{page.title}")
    if page.summary.strip():
        formatted.append(f"\n[Summary]\n{page.summary.strip()}")
    if not is_only_summary:
        for sec in sections:
            label = level_to_label(sec["level"])
            formatted.append(f"\n[{label}: {sec['title']}]\n{sec['text']}")
    return "\n".join(formatted)


def get_page(query: str, is_only_summary=False):
    """
    Searches for a page by query and returns its formatted content.
    """
    top = wikipedia.search(query, results=1)
    if not top:
        return f"[ERROR]\nNo results found for query '{query}'."
    title = top[0]
    return get_wikipedia(title, is_only_summary)
