from urllib import request
from urllib.error import HTTPError, URLError
import ssl


from urllib import request
from urllib.error import HTTPError, URLError
import ssl


def validate_url(url):
    print("I got the url")
    # Create an unverified SSL context
    context = ssl._create_unverified_context()

    # Ensure the URL has a scheme (http or https)
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url  # Default to HTTPS for security

    try:
        # Try opening the URL with a timeout
        print(f"Validating URL: {url}")
        request.urlopen(url, context=context, timeout=10)
        print("URL is valid")
        return True
    except HTTPError as e:
        print(f"HTTPError: {e.code} - {e.reason}")
        return False
    except URLError as e:
        print(f"URLError: {e.reason}")
        return False
    except ValueError:
        print("Invalid URL format")
        return False
