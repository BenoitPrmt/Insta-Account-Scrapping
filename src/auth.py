from instagrapi import Client

from settings import INSTA_USERNAME, INSTA_PASSWORD

cl = Client()

def auth():
    """Authenticate with instagram
    
    Returns:
        client (Client): authenticated client
    """

    print("\nAuthenticating...")
    cl.login(INSTA_USERNAME, INSTA_PASSWORD)
    print("Authenticated !\n")


def get_target(username: str)->list:
    """Get sexe of the user
    
    Args:
        username (str): username to get sexe
    
    Returns:
        sexe (str): sexe of the user
    """
    auth()

    data = []

    print("Getting target...")
    target_id = cl.user_id_from_username(username)

    print("Getting target's subscription (this step may take some time)...")
    followers = cl.user_following(target_id)

    for follower in followers:
        data.append(followers[follower].username)

    return data