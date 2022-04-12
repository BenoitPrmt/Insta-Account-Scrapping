import unicodedata
import json
from settings import BANNED_CHARS

def clean_username(username: str)->str:
    """Clean instagram username to get sexe of the user

    Args:
        username (str): username to clean

    Returns:
        username(str): cleaned username
    """

    for char in BANNED_CHARS:
        username = username.replace(char, "")

    # final = ''.join((c for c in unicodedata.normalize('NFD', username) if unicodedata.category(c) != 'Mn'))
    
    return username


def get_sexe(username: str)->str:
    """Get sexe of the user

    Args:
        username (str): username to get sexe

    Returns:
        sexe (str): sexe of the user
    """

    data = open("./data/first-name-complete.json", encoding='utf-8')
    names_data = json.load(data)

    for names in names_data:
        if names["fields"]["prenoms"].lower() in username:
            return names["fields"]["sexe"]
    
    return "ND"

assert clean_username("username_1234") == "username"