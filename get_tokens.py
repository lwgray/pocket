import  os
import sys
from pocket import Pocket
import requests
import urlparse


def gain_access():
    ''' Obtain Access Token from Pocket

    Return (str):  Access Token
    '''

    redirect_uri = os.environ.get("REDIRECT_URI")
    consumer_key = os.environ.get("CONSUMER_KEY")

    request_token = Pocket.get_request_token(consumer_key=consumer_key,
                                             redirect_uri=redirect_uri)
    auth_url = Pocket.get_auth_url(code=request_token,
                                   redirect_uri=redirect_uri)

    # Deconstruct authorization url and send a request with cookies

    # url_parts is the break down of the auth_url into its base components
    url_parts = urlparse.urlparse(auth_url)

    # query_parts is the extraction of the query component from url_parths
    query_parts = dict(urlparse.parse_qsl(url_parts.query))
    url = url_parts.scheme + '://' + url_parts.netloc + url_parts.path
    requests.post(url, params=query_parts, allow_redirects=True, headers={'cookie':'a95b4b6=d90TbA67g9223p9259d091ade0p9g6102d2Ge5N009Rb52I4f441cD74ue4gDf38; d4a79ec=57c5a18e139c66e9ab1340fb0700bda8e5f1a1dd127b52d9ef8b3f4d132b7c38; 159e76e=f05c70d929285a053b6652cccda4b4ad655e5605193ec01ed7078e37276b0e8d'})

    user_credentials = Pocket.get_credentials(consumer_key=consumer_key,
                                              code=request_token)
    access_token = user_credentials['access_token']
    return access_token

if __name__ == '__main__':
    sys.exit(gain_access())
