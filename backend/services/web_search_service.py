import re

import requests

from backend.config import settings

# DuckDuckGo's lite/text-only HTML endpoint. No API key required, and the
# markup is simple enough to parse without adding an HTML-parsing dependency.
_SEARCH_URL = "https://lite.duckduckgo.com/lite/"

_RESULT_LINK_RE = re.compile(
    r'<a[^>]+class="result-link"[^>]*href="([^"]+)"[^>]*>(.*?)</a>',
    re.IGNORECASE | re.DOTALL,
)
_SNIPPET_RE = re.compile(
    r'<td class="result-snippet">(.*?)</td>',
    re.IGNORECASE | re.DOTALL,
)


def _strip_tags(html: str) -> str:
    return re.sub(r"<[^>]+>", " ", html).strip()


def search_web(query: str, max_results: int = 3) -> list[dict]:
    """
    Best-effort general-web fallback search.

    Used only when the local knowledge base has no strong match for a
    troubleshooting/lab question, so the copilot can still offer general
    guidance instead of a dead end. Never raises -- returns [] if disabled,
    given an empty query, or if the request fails for any reason, so a
    network hiccup never breaks the chat response.
    """
    if not settings.ENABLE_WEB_SEARCH or not query or not query.strip():
        return []

    try:
        response = requests.post(
            _SEARCH_URL,
            data={"q": query},
            timeout=settings.WEB_SEARCH_TIMEOUT,
            headers={"User-Agent": "Mozilla/5.0 (compatible; BrainyLabCopilot/1.0)"},
        )
        response.raise_for_status()
    except requests.RequestException as ex:
        print(f"[Web Search Error] {ex}")
        return []

    links = _RESULT_LINK_RE.findall(response.text)
    snippets = _SNIPPET_RE.findall(response.text)

    results = []

    for index, (href, title_html) in enumerate(links):
        if len(results) >= max_results:
            break

        title = _strip_tags(title_html)
        if not title:
            continue

        snippet = _strip_tags(snippets[index]) if index < len(snippets) else ""

        results.append({
            "title": title,
            "url": href,
            "snippet": snippet,
        })

    return results
