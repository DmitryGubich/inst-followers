import os

from dotenv import load_dotenv
from instagrapi import Client

load_dotenv()
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
VERIFICATION_CODE = os.getenv("VERIFICATION_CODE")


def main():
    cl = Client()
    cl.login(username=USERNAME, password=PASSWORD, verification_code=VERIFICATION_CODE)

    user_id = cl.user_id_from_username(username=USERNAME)
    followers = {f.username for f in cl.user_followers(user_id=user_id).values()}
    followings = {f.username for f in cl.user_following(user_id=user_id).values()}

    print("Your bros: ", followers - followings)
    print("Not your bros: ", followings - followers)


if __name__ == "__main__":
    main()
