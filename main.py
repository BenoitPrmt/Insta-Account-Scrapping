from src.auth import get_target
from src.app import clean_username, get_sexe

print("\nThe target must have a public account or you must follow him/her with the account in settings.py.")
TARGET: str = input("Enter exact username of your target: ")

followings = get_target(TARGET)
clean_list = []

print("\nCleaning data...")
for username in followings:
    clean_list.append(clean_username(username))

sexe = {
    "F": 0,
    "M": 0,
    "ND": 0
}

print("\nGetting sexe of subscriptions...")
for user in clean_list:
    sexe[get_sexe(user)] += 1

print(f"\nResults : {sexe}\nResults are not 100% accurate, as usernames may not contain a first name.\n")