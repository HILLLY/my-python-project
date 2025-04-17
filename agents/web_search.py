from duckduckgo_search import DDGS

def search_web(query: str, max_results: int = 5) -> str:
    try:
        results_text = ""
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=max_results)
            if not results:
                return "No results found."
            
            for res in results:
                title = res.get("title", "No title")
                href = res.get("href", "")
                body = res.get("body", "")
                results_text += f"- [{title}]({href}): {body}\n"
        return results_text
    except Exception as e:
        return f"Error during DuckDuckGo search: {e}"
