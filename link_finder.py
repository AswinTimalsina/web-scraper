from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):
    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

# we are overriding the method in the class HTMLParser    
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value) #if the value is full url then doesnot do any thing but if it is the relative url then it is going to add the base_url
                    self.links.add(url)

    def page_links(self):
        return self.links

    def error(self, message):
        pass

