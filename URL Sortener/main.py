import pyshorteners


def shorten_url(url):
    return pyshorteners.Shortener().tinyurl.short(url)


url = input("Please Enter URL: ")
print("URL after Shortening : ", shorten_url(url))
