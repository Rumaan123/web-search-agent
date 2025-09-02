import string
from tools.web_search import web_search

# Simple static FAQs
FAQS = {
    "what is ai": "AI (Artificial Intelligence) is the simulation of human intelligence in machines.",
    "what is your name": "My name is faq agent.",
    "what is python": "Python is a popular programming language used for AI, web development, and automation."
}

def faq_agent(user_query: str):
    """
    Handles user query:
    - If query matches FAQ, return static answer
    - Otherwise call Tavily web search
    """
    query = user_query.lower().translate(str.maketrans('','', string.punctuation))

    # Check FAQs
    for key, answer in FAQS.items():
        if key in query:
            return answer

    # Otherwise, use Tavily Web Search
    return f"Here are the top results:\n{web_search(user_query, num_results=3)}"
