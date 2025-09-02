import os
import requests
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("TAVILY_API_KEY")

def web_search(query: str, num_results: int = 3):
    """
    Function to fetch web search results from Tavily API.
    """
    url = "https://api.tavily.com/search"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}" 
    }
    payload = {
        "query": query,
        "num_results": num_results
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        print("Raw response text:", response.text) 
        response.raise_for_status()
        data = response.json()

        results = data.get("results", [])
        if not results:
            return "No results found for your query."

        output = ""
        for i, item in enumerate(results[:num_results], start=1):
            title = item.get("title", "No Title")
            snippet = item.get("content", "No Snippet")
            link = item.get("url", "#")
            output += f"{i}. {title}\n{snippet}\nLink: {link}\n\n"

        return output

    except requests.exceptions.RequestException as e:
        return f"Error fetching data: {e}"


#   Test run
if __name__ == "__main__":
    if len(sys.argv) > 1:
        query ="".join(sys.argv[1:])
    else:
        query="Latest AI news"
    
    result = web_search(query, num_results=3)
    print(result)
