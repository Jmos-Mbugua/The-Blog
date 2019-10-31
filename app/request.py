import requests, json
from .models import Quote


quote_url  = "http://quotes.stormconsultancy.co.uk/random.json"

def get_quote():
    """
    Function to consume http request and return a Quote class instance
    """
    response = requests.get(quote_url).json()

    random_quote = Quote(response.get("author"), response.get("quote"))
    return random_quote