import requests
from bs4 import BeautifulSoup
import re


def extract_text(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        html = response.text
        soup = BeautifulSoup(html, "html.parser")

        content = soup.find("div", {"id": "mw-content-text"})

        if not content:
            return "Could not find article content."

        for tag in content(["sup", "table", "style", "script"]):
            tag.decompose()

        paragraphs = content.find_all("p")

        text = " ".join(p.get_text() for p in paragraphs)

        text = re.sub(r"\[\d+\]", "", text)

        text = " ".join(text.split())

        return text

    except Exception as e:
        return f"Error: {e}"