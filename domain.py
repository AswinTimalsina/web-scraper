from urllib.parse import urlparse

# www.mail.gov.ny.lottery.thenewboston.com
# we are just going to get thenewboston.com


# get domain name (example.com)
def get_domain_name(url):
    try:
        name = get_sub_domain_name(url).split('.')
        return name[-2]+'.'+name[-1]
    except:
        return ''


# get subdomain name (name.example.com)
def get_sub_domain_name(url):
    try:
        # it returns just the subdomain. eg if the link is 'https://www.youtube.com/watch?v=PPonGS2RZNc'
        # it returns www.youtube.com
         return urlparse(url).netloc
    except:
        return ''
