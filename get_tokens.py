import os
import sys
from pocket import Pocket


def gain_access():
    redirect_uri = os.environ.get("REDIRECT_URI")
    consumer_key = os.environ.get("CONSUMER_KEY")

    print redirect_uri
    print consumer_key

    request_token = Pocket.get_request_token(consumer_key=consumer_key,
                                             redirect_uri=redirect_uri)
    auth_url = Pocket.get_auth_url(code=request_token,
                                   redirect_uri=redirect_uri)
    print auth_url, "\n"
    raw_input("Please Enter after Authorization")
    user_credentials = Pocket.get_credentials(consumer_key=consumer_key,
                                              code=request_token)
    access_token = user_credentials['access_token']
    return access_token

if __name__ == '__main__':
    sys.exit(gain_access())
