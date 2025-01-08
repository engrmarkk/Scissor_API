from urllib import request
from urllib.error import HTTPError, URLError
import ssl


def validate_url(url):
    context = ssl._create_unverified_context()
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://' + url
    try:
        request.urlopen(url, context=context)
        return True
    except (HTTPError, URLError):
        return False
