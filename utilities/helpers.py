# return the correct url if it comes without prefix
def correct_url(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
    return url